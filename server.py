from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_users():
    name = request.form['name']
    locaiton = request.form['location']
    language = request.form['language']
    text = request.form['text']
    return render_template('/result.html')
    return redirect('/')
# @app.route('/return')
# def goback():
#     return render_template('/')
app.run(debug=True)
