# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:35:07 2019

@author: Saurabh Sinha
"""
import tornado.ioloop
import tornado.web
import socket

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hostname: " + socket.gethostname())

def make_app():
    return tornado.web.Application([(r"/", MainHandler),])
 
if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
