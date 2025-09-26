from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '''<p>Hello, World, I am a Flask app!</p>'''

@app.route('/about')
def link_doc():
	return '''<p>This application is running on the Flask web framework.
		<br><br>
		<a href="https://flask.palletsprojects.com/en/stable">Link to documentation.</a>
		</p>'''

