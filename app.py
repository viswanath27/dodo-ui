from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
@cross_origin(origin='*')
def index():
  return render_template('main_page.html')


@app.route('/page2')
@cross_origin(origin='*')
def page2():
  return render_template('page2.html')

@app.route('/page3')
@cross_origin(origin='*')
def page3():
  return render_template('page3.html')

@app.route('/page4')
@cross_origin(origin='*')
def page4():
  return render_template('page4.html')

@app.route('/page5')
@cross_origin(origin='*')
def page5():
  return render_template('page5.html')  

@app.route('/page6')
@cross_origin(origin='*')
def page6():
  return render_template('page6.html') 

@app.route('/page7')
@cross_origin(origin='*')
def page7():
  return render_template('page7.html') 


@app.route('/page8')
@cross_origin(origin='*')
def page8():
  return render_template('page8.html') 

@app.route('/page9')
@cross_origin(origin='*')
def page9():
  return render_template('page9.html') 

@app.route('/page10')
@cross_origin(origin='*')
def page10():
  return render_template('page10.html') 

@app.route('/page11')
@cross_origin(origin='*')
def page11():
  return render_template('page11.html') 

if __name__ == '__main__':
   app.run()