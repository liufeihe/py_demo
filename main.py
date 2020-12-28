#!/usr/bin/python
# -*- coding: UTF-8 -*-

from threading import Thread
import tornado.ioloop
import tornado.web
from schedule.schedular import init_schedular, add_order

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print('get')
        self.write("hello world")

    def post(self, p=None):
        print('post, {0}'.format(p))
        add_order()
        self.write({'data': 1})

def make_app():
    return tornado.web.Application([
        (r"/order/?(list|)", MainHandler)
    ])

def main():
    schedular = init_schedular()
    t1 = Thread(target=schedular.run)
    t1.start()

    app = make_app()
    port = 8091
    app.listen(port)
    print('server is running at: {0}'.format(port))
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()