#!/bin/bash

set -o errexit
set -o nounset

[ -n "$BUFFERBLOAT_NET_DEST" ] || exit 1

LOCKDIR=$HOME/.bufferbloat-build.lock
PIDFILE=$LOCKDIR/PID

mkdir $LOCKDIR # fails if it already exists
echo $$ > "$PIDFILE"

cd $HOME/bufferbloat-net

git pull --quiet --ff-only

rm -rf public

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

get_stylesheets | python -m rcssmin > static/css/combined.css

conf=$(mktemp config-XXXX.yaml)
sed 's/stylesheets: .*/stylesheets: ["combined.css"]/' config.yaml > $conf

hugo -d public --config=$conf --logFile=$HOME/hugo.log > /dev/null
rm -f $conf

# Remove source css files
find public -name '*.css' -not -name combined.css -delete

# gzip files so nginx can serve them compressed
find public \( -name '*.js' -or -name '*.css' -or -name '*.svg' -or -name '*.html' -or -name '*.ttf' \) -exec gzip -k9 '{}' \;

# optimise PNG images
find public -name '*.png' -exec optipng -silent -preserve '{}' \;

rsync -rtpl --delete --exclude stats/ --exclude /news --exclude /issues --exclude .well-known public/ $BUFFERBLOAT_NET_DEST/projects/
rsync -rtpl --delete public/news/ $BUFFERBLOAT_NET_DEST/news/
rsync -rtpl --delete public/issues/ $BUFFERBLOAT_NET_DEST/issues/

rm -rf static/css/combined.css $LOCKDIR
