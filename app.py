# __init__.py section
from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import json
import math

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)


class User(db.Model): #user model, derived from db.model
    id = db.Column(db.Integer, primary_key=True) #makes a column class for id, primary key means unique identifier
    username = db.Column(db.String(80), unique=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poster_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.String)
    title = db.Column(db.String)



# views.py section
@app.route('/')
@app.route('/page/<current_page>')
def index(current_page=1):
    '''Displays index page, with 5 posts'''

    current_page = int(current_page)
    number_of_posts = db.session.query(Post).count()
    number_of_pages = math.ceil(number_of_posts / 5)
    if number_of_pages < 6:
        pages = range(1, 1 + number_of_pages)
    else:
        if current_page <= 2:
            pages = range(1, 6)
        elif current_page >= (number_of_pages - 2):
            pages = range(number_of_pages - 4, number_of_pages + 1)
        else:
            pages = range(current_page - 2, current_page + 3)
    display_post_list = db.session.query(Post).order_by(Post.id)\
                                              .limit(5)\
                                              .offset((current_page - 1) * 5)\
                                              .all()
    for post in display_post_list:
        post.user = db.session.query(User).filter(User.id == post.poster_id).one()
    return render_template('index.html',
                            title = 'Index',
                            display_post_list = display_post_list,
                            current_page = current_page,
                            pages = pages,
                            max_pages = number_of_pages)


@app.route('/login/', methods = ['GET', 'POST'])
def login():
    '''Displays login page'''

    if request.method == 'POST':
        return 'login function'
    else:
        return render_template('login.html',
                                title = 'Login')


@app.route('/users/<userkey>')
def show_user(userkey):
    '''Displays user page, including post history,
    option to edit profile info'''

    return render_template('user.html', user=users[userkey])


@app.route('/users/')
def users_redirect():
    return redirect(url_for('index'))


@app.route('/<postkey>')
def show_post(postkey):
    if postkey in posts:
        return render_template('post.html', post=posts[postkey])
    elif postkey in users:
        return redirect(url_for('show_user', userkey=postkey))
    else:
        return redirect(url_for('index'))


@app.route('/profile/')
def show_profile():
    return render_template('profile.html')


@app.route('/search/')
def search():
    return render_template('search.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404



# run.py section
if __name__ == '__main__':
    app.run(debug=True)




    # with open('db.json', 'r') as f:
#     posts = json.load(f)
# with open('users.json', 'r') as f:
#     users = json.load(f)
