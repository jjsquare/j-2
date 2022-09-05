from flask import Blueprint,render_template,request,flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('logged in succesfully!', category='success')
            else:
                flash('password Error', category='error')
        else:
            flash('email doesn\'t exist', category='error')
    return render_template("login.html",  boolean = True)


@auth.route('/logout')
def logout():
    return render_template("home.html")

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('username')
        firstName = request.form.get('fname')
        lastName = request.form.get('lname')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(email = email).first()
        if user:
            flash('email alerady exits', category='error')
        elif len(email) < 4:
            flash('email must be greater than 4 characters', category='error')
        elif len(firstName) <2:
            flash('first name must be greater than 2 characters', category='error')
        elif len(lastName) <2:
            flash('last name must be greater than 2 characters', category='error')
        elif password != confirm_password:
            flash('password don\'t match', category='error')
        elif len(password) < 8:
            flash('password must be greater than 8 characters', category='error')
        else :
            new_user = User(email = email, first_name = firstName, password = generate_password_hash(password , method='sha256') )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('views.home'))

            flash('account created succesfully ', category='succes')
    return render_template("sign_up.html")
