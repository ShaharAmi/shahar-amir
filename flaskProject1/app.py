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

@app.route("/assignment8")
def assignment8():
    return render_template('assignment8.html', my_profile={'name': 'Shahar', 'second': 'Amir'},
                           university='BGU', fav_movies=['Spider-Man', 'Shall We Dance', 'Cinderella'],
                           hobbies=('music', 'sport', 'friends','dance'))

if __name__ == '__main__':
    app.run()
