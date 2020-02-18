import flask

APP = flask.Flask(__name__)

@APP.route('/<name>/')
def name(name):
	return name

@APP.route('/sum/<int:a>/<int:b>/')
def sum(a,b):
	return '{} + {} = {}'.format(a,b,a+b)

if __name__ == '__main__':
	APP.debug = True
	APP.run()