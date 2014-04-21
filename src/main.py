import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world21")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    from tornado import autoreload
    autoreload.start()
    application.listen(8003)
    tornado.ioloop.IOLoop.instance().start()
