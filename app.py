#!/usr/bin/env python3

import os
from flask import Flask, render_template, session, redirect, url_for


# Our application
app = Flask(__name__)
app.secret_key = 'this doesn\'t really matter for this example'


# Our route handlers
@app.route('/')
def index():
   if 'num' in session:
      return render_template('home.html', num=session['num'])
   return render_template('home.html')


@app.route('/addone')
def addone():
   if not 'num' in session:
      session['num'] = 1
   else:
      session['num'] += 1
   return redirect(url_for('index'))


@app.route('/clear')
def clear():
   session.pop('num')
   return redirect(url_for('index'))


# Run the application as a stand-alone
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

