#!/usr/bin/env python
## -*- coding: utf-8 -*-
##
## invalidate-caches.py
##
## Author:   Toke Høiland-Jørgensen (toke@toke.dk)
## Date:     17 June 2016
## Copyright (c) 2016, Toke Høiland-Jørgensen
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function, unicode_literals

from builtins import str

import logging
import os
import requests
import sys
import time

# Enable verified HTTPS requests on older Pythons
# http://urllib3.readthedocs.org/en/latest/security.html
if sys.version_info[0] == 2:
    requests.packages.urllib3.contrib.pyopenssl.inject_into_urllib3()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
h = logging.StreamHandler()
h.setLevel(logging.INFO)
logger.addHandler(h)

MAX=30 # Max number of URLs in one request

try:
    CF_HEADERS = {
        'X-Auth-Email': os.environ['CF_EMAIL'],
        'X-Auth-Key'  : os.environ['CF_KEY'],
        'Content-Type': 'application/json',
    }
    DOMAIN=os.environ['CF_DOMAIN']
    PREFIX=os.environ['CF_URL_PREFIX']
    if 'CF_LOG_FILE' in os.environ:
        h = logging.FileHandler(os.environ['CF_LOG_FILE'])
        h.setFormatter(logging.Formatter(fmt='%(asctime)s: %(message)s'))
        logger.addHandler(h)
except KeyError:
    logger.error("Unable to locate Cloudflare credentials in environment!")
    sys.exit(1)


# https://api.cloudflare.com/#zone-list-zones
def _get_zone_id(domain):
    url = "https://api.cloudflare.com/client/v4/zones?name={0}".format(domain)
    r = requests.get(url, headers=CF_HEADERS)
    r.raise_for_status()
    return r.json()['result'][0]['id']


# https://api.cloudflare.com/#zone-purge-individual-files-by-url-and-cache-tags
def purge_cache_urls(zone_id, urls):
    for u in urls:
        logger.debug("Purging URL: '{0}'.".format(u))
    url = "https://api.cloudflare.com/client/v4/zones/{0}/purge_cache".format(zone_id)
    payload = {
        'files': urls,
    }
    r = requests.delete(url, headers=CF_HEADERS, json=payload)
    r.raise_for_status()
    logger.info("Purged {0} URLs.".format(len(urls)))

def purge_urls(urls):
    zone_id = _get_zone_id(DOMAIN)
    for i in range(len(urls)//MAX + 1):
        purge_cache_urls(zone_id, urls[i*MAX:(i+1)*MAX])

def main(urlfile):

    urls = []
    with open(urlfile, 'r') as fp:
        for line in fp:
            line = line.strip()
            if line.endswith(".gz"):
                continue
            if line.endswith("index.html"):
                urls.append(PREFIX+"/"+os.path.split(line)[0]+"/")
            else:
                urls.append(PREFIX+"/"+line)
    purge_urls(urls)

if __name__ == '__main__':
    main(sys.argv[1])
