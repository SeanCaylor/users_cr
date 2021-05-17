from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL('users_cr')
    users = mysql.query_db('SELECT id, CONCAT_WS(" ", first_name, last_name) as "name", email FROM users;')
    print(users)
    return render_template('index.html', all_users = users)

@app.route('/new_user')
def new_user_form():
    return render_template('newuser.html')

@app.route('/create_user', methods=['POST'])
def create_friend():
    mysql = connectToMySQL('users_cr')

    query = "INSERT INTO users (first_name, last_name, email) VALUE (%(fn)s, %(ln)s, %(eml)s)"
    data = {
        'fn' : request.form['first_name'],
        'ln' : request.form['last_name'],
        'eml' : request.form['email']
    }
    print('succeed')
    new_friend_id = mysql.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)