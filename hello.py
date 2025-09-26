from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '''<p>Welcome!<br><br><a href="/about">Go to About page</a><br><br><a href="/contact">go to contact.</a> </p>'''

@app.route('/about')
def link_doc():
	return '''<p>This application is running on the Flask web framework.
		<br><br>
		<a href="https://flask.palletsprojects.com/en/stable">Link to documentation.</a>
		</p>'''

@app.route('/contact')
def contact():
	return '''email: renee1ow007@gmail.com'''

