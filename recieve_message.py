from tornado.escape import json_decode
import tornado.ioloop
import tornado.web

from push_line import push_line

class PushHander(tornado.web.RequestHandler):
    def post(self):
        body = json_decode(self.request.body)
        print("arguments: {}".format(str(body)))

        msg = body.get("message")
        print("msg: {}".format(msg))
        self.push_line(msg)

    def push_line(self, msg):
        push_line(msg)

application = tornado.web.Application([
    (r"/push", PushHander),
])

def main():
    print("start pusher...")
    application.listen(8091)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
