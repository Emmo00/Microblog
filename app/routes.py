from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login successful for {form.username.data}')
        return redirect('/home')
    return render_template('login.html', title='Login', form=form)
