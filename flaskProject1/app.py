from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

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
                           hobbies=('music', 'sport', 'friends','dance'))


@app.route('/assignment9', methods= ['GET','POST'])
def assignment9():
    username = ''
    if session['Logged_in']:
        username = session['username']

    users = [
        {'fullname': 'Shahar Amir', 'email': 'shahar@gmail.com', 'age': '27'},
        {'fullname': 'Sigal Amir', 'email': 'sigal@gmail.com', 'age': '52'},
        {'fullname': 'Din Amir', 'email': 'din@gmail.com', 'age': '27'},
        {'fullname': 'Ziv Amir', 'email': 'ziv@gmail.com', 'age': '57'},
        {'fullname': 'Yahel Amir', 'email': 'yahel@gmail.com', 'age': '16'}
    ]
    fullName = ''
    if request.method == 'GET':
        if 'fullName' in request.args:
            fullname = request.args['fullName']
            email = request.args['email']
            age = request.args['age']
            return render_template('assignment9.html',request_method=request.method, fullname=fullname, email=email, age=age, users=users)
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
    return render_template('assignment9.html', username=username, fullName=fullName, users=users )

@app.route('/log_out')
def log_out():
    session.pop('username')
    session['logged_in'] = False
    return redirect()

if __name__ == '__main__':
    app.run(debug=True)
