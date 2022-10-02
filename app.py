from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)


# @app.route('/')
# def index():
#    print('Request for index page received')
#    return render_template('index.html')

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

# @app.route('/hello', methods=['POST'])
# def hello():
#    name = request.form.get('name')

#    if name:
#        print('Request for hello page received with name=%s' % name)
#        return render_template('hello.html', name = name)
#    else:
#        print('Request for hello page received with no name or blank name -- redirecting')
#        return redirect(url_for('index'))


@app.route('/')
@cross_origin(supports_credentials=True)
def index():
  return render_template('main_page.html')


@app.route('/page2')
@cross_origin(supports_credentials=True)
def page2():
  return render_template('page2.html')

@app.route('/page3')
@cross_origin(supports_credentials=True)
def page3():
  return render_template('page3.html')

@app.route('/page4')
@cross_origin(supports_credentials=True)
def page4():
  return render_template('page4.html')

@app.route('/page5')
@cross_origin(supports_credentials=True)
def page5():
  return render_template('page5.html')  

@app.route('/page6')
@cross_origin(supports_credentials=True)
def page6():
  return render_template('page6.html') 

@app.route('/page7')
@cross_origin(supports_credentials=True)
def page7():
  return render_template('page7.html') 


@app.route('/page8')
@cross_origin(supports_credentials=True)
def page8():
  return render_template('page8.html') 

@app.route('/page9')
@cross_origin(supports_credentials=True)
def page9():
  return render_template('page9.html') 

@app.route('/page10')
@cross_origin(supports_credentials=True)
def page10():
  return render_template('page10.html') 

@app.route('/page11')
@cross_origin(supports_credentials=True)
def page11():
  return render_template('page11.html') 

if __name__ == '__main__':
   app.run()