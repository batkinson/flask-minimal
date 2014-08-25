#!/usr/bin/env python3

import os
from flask import Flask, render_template

# Our application
app = Flask(__name__)
app.secret_key = 'this doesn\'t really matter for this example'

# Our route handlers
@app.route('/')
def index():
   return render_template('home.html')

# Run the application as a stand-alone
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

