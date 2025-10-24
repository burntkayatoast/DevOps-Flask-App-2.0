from flask import Flask
import redis
import time 
import json

app = Flask(__name__)
r = redis.Redis(host='redis-server', port=6379, decode_responses=True)

@app.route('/')
def say_hello():
    data = r.get('/')
    if data is not None:
        data = json.loads(data)
        if time.time() - data['time'] <= 600:
            return data['html']
    data = '''<p>Welcome!<br><br><a href="/about">Go to About page</a><br><br><a href="/contact">go to contact.</a> </p>'''
    r.set('/home', json.dumps ({
        'html': data,
        'time': time.time()
    }))
    return data


@app.route('/about')
def link_doc():
    data = r.get('about')
    if data is not None:
        data = json.loads(data)
        if time.time() - data['time'] <= 600:
            return data['html']
    data = '''<p>This application is running on the Flask web framework.
        <br><br>
        <a href="https://flask.palletsprojects.com/en/stable">Link to documentation.</a>
        <a href="https://www.python.org">Link to Python website.</a>
        </p>'''
    r.set('about', json.dumps ({
        'html': data,
        'time': time.time()
    }))
    return data

@app.route('/contact')
def contact():
    data = r.get('contact')
    if data is not None:
        data = json.loads(data)
        if time.time() - data['time'] <= 600:
            return data['html']
    data = '''email: renee1ow007@gmail.com'''
    r.set('contact', json.dumps ({
        'html': data,
        'time': time.time()
    }))
    return data
