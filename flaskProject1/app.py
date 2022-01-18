from flask import Flask, redirect, url_for, render_template, request, session
from interact_with_DB import interact_db, query_to_json
import json
import requests
from flask import jsonify

app = Flask(__name__)
app.secret_key = '123456789'

from pages.users.users import users

app.register_blueprint(users)

from pages.assignment10.assignment10 import assignment10

app.register_blueprint(assignment10)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('homepage.html')


@app.route("/redirect")
def index():
    return render_template('CV.html')


@app.route("/you were redirected")
def redirected():
    return "You were redirected! :)"


@app.route("/home")
def home():
    return redirect(url_for('about'))


@app.route("/about")
def about():
    return "redirect work!"


@app.route('/cv')
def CV():
    return render_template('CV.html')


@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html', my_profile={'name': 'Shahar', 'second': 'Amir'},
                           university='BGU', fav_movies=['Spider-Man', 'Shall We Dance', 'Cinderella'],
                           hobbies=('music', 'sport', 'friends', 'dance'))


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    username = ''
    if session['Logged_in']:
        username = session['username']

    my_users = [
        {'fullname': 'Shahar Amir', 'email': 'shahar@gmail.com', 'age': '27'},
        {'fullname': 'Sigal Amir', 'email': 'sigal@gmail.com', 'age': '52'},
        {'fullname': 'Din Amir', 'email': 'din@gmail.com', 'age': '27'},
        {'fullname': 'Ziv Amir', 'email': 'ziv@gmail.com', 'age': '57'},
        {'fullname': 'Yahel Amir', 'email': 'yahel@gmail.com', 'age': '16'}
    ]
    # else
    fullName = ''
    if request.method == 'GET':
        if 'fullName' in request.args:
            fullname = request.args['fullName']
            email = request.args['email']
            age = request.args['age']
            return render_template('assignment9.html', request_method=request.method, fullname=fullname, email=email,
                                   age=age, users=users)
        return render_template('assignment9.html')

    if request.form == 'POST':
        if request.form["btn"]: "log out"
        session['Logged_in'] = False
        session['username'] = ''
        username = ''
        # else
        username = request.form['username']
        password = request.form['password']
        session['Logged_in'] = True
        session['username'] = username
        return render_template('assignment9.html', username=username)


@app.route('/log_out')
def log_out():
    session.pop('username')
    session['logged_in'] = False
    return redirect()


@app.route("/assignment11/users")
def assignment11():
    query = "select * from users"
    query_result = query_to_json(query=query)
    return json.dumps(query_result)


@app.route("/assignment11/outer_source", methods=['GET'])
def assignment11_func():
    if 'number' in request.args:
        number = request.args['number']
        req = requests.get(url=f"https://reqres.in/api/users/{number}")
        req = req.json()
        return render_template('assignment11_outer_source.html', user=req['data'])
    return render_template('assignment11_outer_source.html')


@app.route("/assignment12/restapi_users", defaults={'user_id': 1})
@app.route("/assignment12/restapi_users/<int:user_id>")
def assignment12(user_id):
    query = 'select * from users where id=%s;' % user_id
    query_result = interact_db(query=query, query_type='fetch')
    if len(query_result) == 0:
        return_dict = {'status': 'failed', 'message': 'user not found'}
    else:
        return_dict = {'status': 'success', 'id': query_result[0].id, 'name': query_result[0].name,
                       'email': query_result[0].email}
    return jsonify(return_dict)


# @app.route('/get_users', defaults={'user_id': 32})
# @app.route('/get_users/<user_id>', methods=['GET', 'POST'])
# def get_user(user_id):
#     query = "select * from users where id=%s" % user_id
#     query_result = interact_db(query=query, query_type='fetch')
#     if len(query_result) == 0:
#         return_dict = {'status': 'failed', 'message': 'user not found'}
#     else:
#         return_dict = {'status': 'success', 'name': query_result[0].name, 'email': query_result[0].email}
#
#     return jsonify(return_dict)

if __name__ == '__main__':
    app.run(debug=True)
