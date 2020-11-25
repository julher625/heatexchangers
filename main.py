from flask import Flask, request, make_response, redirect, render_template,session
from flask_bootstrap import Bootstrap


app = Flask(__name__) 
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = '123456aaa'

todos = ['A','B','C']



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html',error=error)

@app.route('/home')
@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/welcome'))
    session['user_ip'] = user_ip
    #response.set_cookie('user_ip',user_ip)
    return response


@app.route('/welcome')
def welcome():


    #user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    if user_ip:   
        context = {
            'user_ip':user_ip,
            'todos':todos
        }
        return render_template('welcome.html',**context)#** permite expandir el diccionario
    else:
        response = make_response(redirect('/'))
        return response


@app.route('/step/<int:st>')
def steps(st):
    context = {
        'st':st,
    }
    return render_template('steps/step_'+ str(st) +'.html',**context)
