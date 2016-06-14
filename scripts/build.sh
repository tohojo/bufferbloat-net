#!/bin/bash

set -o errexit
set -o nounset

[ -n "$BUFFERBLOAT_NET_DEST" ] || exit 1

LOCKDIR=$HOME/.bufferbloat-build.lock
PIDFILE=$LOCKDIR/PID
SRCDIR=$HOME/bufferbloat-net

cleanup() {
    rm -rf $LOCKDIR $TMPDIR
    rm -f $SRCDIR/static/css/combined.css
}


mkdir $LOCKDIR # fails if it already exists
trap cleanup EXIT
echo $$ > "$PIDFILE"
TMPDIR=$(mktemp -d /tmp/hugo-build-XXXX)
conf=$TMPDIR/config.yaml
target=$TMPDIR/public

cd $SRCDIR

git pull --quiet --ff-only

STYLESHEET_PATHS="static/css"

get_stylesheets()
{
    stylesheets=$(grep 'stylesheets: ' config.yaml | sed -e 's/[",]//g' -e 's/stylesheets: \[//' -e s/\]//)
    for f in $stylesheets; do
        for d in $STYLESHEET_PATHS; do
            if [ -f "$d/$f" ]; then cat "$d/$f"; break; fi
        done
    done
}

get_stylesheets | python -m rcssmin > $SRCDIR/static/css/combined.css

sed 's/stylesheets: .*/stylesheets: ["combined.css"]/' $SRCDIR/config.yaml > $conf

hugo -d $target --config=$conf --logFile=$HOME/hugo.log  > /dev/null

# Remove source css files
find $target -name '*.css' -not -name combined.css -delete

# gzip files so nginx can serve them compressed
find $target \( -name '*.js' -or -name '*.css' -or -name '*.svg' -or -name '*.html' -or -name '*.ttf' \) -exec gzip -k9 '{}' \;

# optimise PNG images
#find public -name '*.png' -exec optipng -silent -preserve '{}' \;

rsync -rtpl --delete --exclude stats/ --exclude /news --exclude /issues --exclude .well-known $target/ $BUFFERBLOAT_NET_DEST/projects/
rsync -rtpl --delete $target/news/ $BUFFERBLOAT_NET_DEST/news/
rsync -rtpl --delete $target/issues/ $BUFFERBLOAT_NET_DEST/issues/

