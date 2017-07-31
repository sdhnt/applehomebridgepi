import tornado.ioloop
import tornado.web
from sense_hat import SenseHat

sense = SenseHat()


lamp = 0

def lamp_on():
	print("Lamp is turned ON")
	lamp = 1
	sense.clear((255,255,255))

def lamp_off():
	print("Lamp is turned OFF")
	lamp = 0
	sense.clear((0,0,0))


def read_lamp():
	return str(lamp)

class LampHandler(tornado.web.RequestHandler):
	def get(self, action):
		if action == "/on":
			# /lamp/on
			lamp_on()
		elif action == "/off":
			# /lamp/off
			lamp_off()
		elif action == "":
			# /lamp
			self.write(read_lamp())

def make_app():
	return tornado.web.Application([
		(r"/lamp(.*)", LampHandler),
	])

if __name__ == "__main__":
	app = make_app()
	app.listen(80)
	tornado.ioloop.IOLoop.current().start()