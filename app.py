from flask import Flask, redirect, render_template, request, url_for
from wtforms import Form, StringField, validators
from passlib.hash import sha256_crypt

from database_connection import add_user

class RegisterFrom(Form):
    username = StringField('Username', [validators.Length(min=1, max = 50)])
    password = StringField('Password', [validators.Length(min = 1)])
    email = StringField('Email', [validators.Length(min = 6)])

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    form = RegisterFrom(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        email = form.email.data
        
        #add_user(username, password, email)
        return redirect(url_for('tanks'))
    
    return render_template('index.html', form=form)

    
@app.route('/tanks')
def tanks():
    return render_template('tanks.html')

if __name__ == '__main__':
    app.run()