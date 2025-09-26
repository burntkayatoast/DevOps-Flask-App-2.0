#! usr/bin/bash

sudo apt update && sudo apt ugrade

sudo apt install nano vim python-is-python3
sudo apt install python3-venv python3-pip

python -m venv .my_venv
source .my_venv/bin/activate

pip install flask

cat > hello.py << 'EOF'
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

EOF

flask --app hello run --host=0.0.0.0
