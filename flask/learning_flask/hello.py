from flask import Flask, url_for, request, render_template

app = Flask(__name__)


TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello_world():
    return 'hello, world'

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.from['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error = error)


@app.route('/user/<username>')
def profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


# with app.test_request_context():
#     print url_for('index')
#     print url_for('login')
#     print url_for('login', next='/')
#     print url_for('profile', username='John Doe')
