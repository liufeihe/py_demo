#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tornado.ioloop
import tornado.web
from schedular import get_schedular

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")
        s = get_schedular()
        print(s)

    def post(self, p=None):
        print(p)
        self.write({'data': 1})

def make_app():
    return tornado.web.Application([
        (r"/job/?(list|)", MainHandler)
    ])

def main():
    app = make_app()
    port = 8091
    app.listen(port)
    print('server is running at: {0}'.format(port))
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()