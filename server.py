from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "'b'\xc2\xb7\x96\x13fa&\x91\x1c\xc0\xd6\xe7\xc289\xfb"


@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] = session['visits'] + 1
    else:
        session['visits'] = 1

    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    if 'users' in session:
        session['users'].append(request.form['name'])
    else:
        session['users'] = []
        session['users'].append(request.form['name'])
    if 'userEmail' in session:
        session['userEmail'].append(request.form['email'])
    else:
        session['userEmail'] = []
        session['userEmail'].append(request.form['email'])

    session['count'] = len(session['users'])

    return redirect('/')


@app.route('/show')
def show_user():
    return render_template('show.html')


@app.route('/clear', methods=['POST'])
def clear_users():
    session.clear()

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
