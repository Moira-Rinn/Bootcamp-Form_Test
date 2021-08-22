from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "'b'\xc2\xb7\x96\x13fa&\x91\x1c\xc0\xd6\xe7\xc289\xfb"


@app.route('/')
def index():
    session['visits'] = session['visits'] + 1

    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['username'] = request.form['name']
    session['users'].append(session['username'])
    print(session['users'])
    session['useremail'] = request.form['email']
    session['usersEmail'].append(session['useremail'])
    session['count'] = session['count'] + 1

    return redirect('/')


@app.route('/show')
def show_user():
    return render_template('show.html')


@app.route('/clear', methods=['POST'])
def clear_users():
    session['users'] = []
    session['usersEmail'] = []
    session['count'] = 0
    session['visits'] = 0

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
