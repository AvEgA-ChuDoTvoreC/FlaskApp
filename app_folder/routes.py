import imghdr
import os
import subprocess
import logging

from flask import render_template, redirect, url_for, request, flash, abort, send_from_directory
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

from app_folder import app, db, login_manager
from app_folder.models import Message, Users


#


@app.route('/', methods=['GET'])
def route_default():
    return render_template('welcome.html')


@app.route('/index', methods=['GET'])
@login_required
def index():
    return render_template('index.html', qq='--> some extra text to form <--')


@app.route('/main', methods=['GET'])
@login_required
def main():
    return render_template('main.html', messages_from_db=Message.query.all())


@app.route('/add_message', methods=['POST'])
@login_required
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    if text:
        # messages.append(Messages(text, tag))
        db.session.add(Message(text, tag))  # , date))
        db.session.commit()
    elif tag and not text:
        pass

    return redirect(url_for('main'))


# ==Authentication==
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:

        #
        user = Users.query.filter_by(login=login).first()

        if not user:
            flash('Please register before login (no such user was found)')

        if user and check_password_hash(user.password, password):
            login_user(user)

            next_user_page_he_choose_b4_login = request.args.get('next')
            if next_user_page_he_choose_b4_login:
                return redirect(next_user_page_he_choose_b4_login)
            else:
                return redirect(url_for('route_default'))

        else:
            flash('Login or password is not correct')
    else:
        flash('Please fill login and password fields')

    if not current_user.is_authenticated:
        return render_template('login.html')

    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    flash('Please fill registration fields')

    if request.method == 'POST':
        if not (login or password or password2):
            flash('Please, fill all fields!')
        elif password != password2:
            flash('Passwords are not equal!')
        else:
            hash_pwd = generate_password_hash(password)
            new_user = Users(login=login, password=hash_pwd)
            db.session.add(new_user)  # , date))
            db.session.commit()

            return redirect(url_for('login_page'))

    return render_template('register.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('route_default'))


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)

    return response


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    file_format = imghdr.what(None, header)
    if not file_format:
        return None
    return '.' + (file_format if file_format != 'jpeg' else 'jpg')


@app.route('/upload', methods=['POST'])
@login_required
def upload_avatar_from_user():
    """
    from flask_wtf import FlaskForm
    from flask_wtf.file import FileField
    from wtforms import SubmitField

    class MyForm(FlaskForm):
        file = FileField('File')
        submit = SubmitField('Submit')


    for uploaded_file in request.files.getlist('file'):
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)

    >> secure_filename('foo.jpg')
    'foo.jpg'
    >> secure_filename('/some/path/foo.jpg')
    'some_path_foo.jpg'
    >> secure_filename('../../../.bashrc')
    'bashrc'
    """
    if request.method == 'POST':
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        print("Filename: ", filename)

        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            print("File_ext: ", file_ext)

            if file_ext not in app.config['UPLOAD_EXTENSIONS'] or file_ext != validate_image(uploaded_file.stream):
                # abort(400)
                return "Invalid image", 400

            filename = str(current_user.id) + str(file_ext)
            print("New_filename: ", filename)

            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))

            # return render_template('upload2.html')

        return '', 204


@app.route('/upload')
@login_required
def before_upload_avatar():
    files = os.listdir(app.config['UPLOAD_PATH'])
    print("Files: ", files)
    return render_template('upload.html', files=files)


@app.route('/upload2', methods=['POST', 'GET'])
@login_required
def before_upload_avatar2():
    # FIXME: need to create new form and good redirection with upload button
    avatar_id = str(current_user.id)
    # file = ''
    file = subprocess.run(['ls', f'{os.path.join(app.config["UPLOAD_PATH"])}', '|', 'grep', f"{avatar_id}"], capture_output=True)
    # print(subprocess.check_output('pwd'))
    # file_ext = os.path.splitext(file)[1]

    print("avatar2 File: ", file)
    return render_template('upload2.html', files=file, avatar_id=avatar_id)


@app.route('/app_folder/static/upload_folder/avatar/<filename>')
@login_required
def upload_avatar_to_server(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413



