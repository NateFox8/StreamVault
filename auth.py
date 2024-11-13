from flask import Blueprint, render_template, redirect, url_for, jsonify, request, session
from models import *
from extensions import bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
                
        user = User.query.filter_by(username=username).first()
            
        if user:
            if bcrypt.check_password_hash(user.password, password):
                session['username'] = username
                print('successful login, user: ' + session['username'])
                return jsonify({'success': True})
            else:
                print('incorrect password')
                return jsonify({'success': False})        
    
    return render_template('login.html')    
    
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':    
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password1')
                
        user = User.query.filter_by(username=username).first()
        
        if user:
            print('username is taken')
            return jsonify({'success': False}), 401           
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(email=email, username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            print('user: ' + username + ' created!')
            session['username'] = username
            return jsonify({'success': True})            
                
    return render_template('signup.html')

@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('auth.login'))