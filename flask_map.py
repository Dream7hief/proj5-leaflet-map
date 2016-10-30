import flask
import CONFIG
import logging
from flask import render_template, jsonify

app = flask.Flask(__name__)



def parse_data(data):
	
	field = None
	entry = {}
	parsed_data = []
	for i in range(len(data)):
		if len(data)==0:
			continue
		parts = data[i].split(',')
		data[i] = parts


	return data

## add later , coordinates=coordinates
def read(txt):
	poi = txt.readlines()
	return poi

@app.route("/")
@app.route("/index")
def index():
	poi = open("data/poi.txt")
	raw = read(poi)

	location = parse_data(raw)
	poi.close()
	
	return flask.render_template('index.html', location=location)

@app.errorhandler(404)
def error_404(e):
  app.logger.warning("++ 404 error: {}".format(e))
  return flask.render_template('404.html'), 404


@app.errorhandler(500)
def error_500(e):
    app.logger.warning("++ 500 error: {}".format(e))
    assert app.debug == False #  I want to invoke the debugger
    return flask.render_template('500.html'), 500

app.secret_key = CONFIG.secret_key
app.debug=CONFIG.DEBUG
app.logger.setLevel(logging.DEBUG)
if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
