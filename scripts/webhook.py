## -*- coding: utf-8 -*-
##
## webhook.py
##
## Author:   Toke Høiland-Jørgensen (toke@toke.dk)
## Date:     13 June 2016
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


import http.server, sys, os, subprocess, json, hmac

from multiprocessing import Process, Queue

SECRET = os.environ['WEBHOOK_SECRET'].encode()

def run_build(q):
    while q.get():
        c = subprocess.run([os.path.join(os.environ['HOME'], 'build.sh')])
        if c.returncode:
            print("Build failed with code %d" % c.returncode)

class ReqHandler(http.server.BaseHTTPRequestHandler):

    def verify_sig(self, data):
        hm = hmac.new(SECRET, data, 'sha1')
        sig = 'sha1=' + hm.hexdigest()
        return hmac.compare_digest(sig, self.headers['X-Hub-Signature'])

    def run_build(self):
        self.server.q.put(True)

    def error(self, response):
        self.send_response(response)
        self.end_headers()
        self.wfile.flush()

    def do_GET(self):
        self.error(405)

    def do_POST(self):
        try:
            nbytes = int(self.headers.get('content-length'))
            indata = self.rfile.read(nbytes)
        except (TypeError, ValueError):
            nbytes = 0
            indata = None

        if not indata or not 'X-Hub-Signature' in self.headers or not self.verify_sig(indata):
            self.error(401)
            return

        try:
            data = json.loads(indata.decode())
        except (json.decoder.JSONDecodeError, TypeError):
            self.error(400)
            return

        if data.get('ref') == 'refs/heads/master':
            self.run_build()

        self.send_response(200,'OK')
        self.end_headers()
        self.wfile.write(b'OK\n')
        self.wfile.flush()

class Server(http.server.HTTPServer):
    def __init__(self, q, *args):
        self.q = q
        super(Server,self).__init__(*args)

if __name__ == "__main__":
    q = Queue()
    p = Process(target=run_build, args=(q,))
    p.start()

    server_address = ('127.0.0.1', 12012)
    httpd = Server(q, server_address, ReqHandler)
    httpd.serve_forever()
