from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from datetime import datetime
from flask import render_template
from flaskext.mysql import MySQL
from mysql.connector import (connection)
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
import db
import validationServer
import passwordEncrypt

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
# bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)
# @app.route('/')
# def index():
#     cnx = connection.MySQLConnection(user='root', password='',
#                                  host='127.0.0.1',
#                                  database='nodejs_login1')
#     return "<h1>Hello world</h1>"

@app.route('/register', methods=['POST'])
def register():
    post_data = request.get_json()
    valid, msg = validationServer.validateSignUP(post_data, ['name','email','password','usertype'])
    password = passwordEncrypt.encrypt_password(post_data.get('password'))
    post_data['password'] = password
    if(valid):
        d = db.DB()
        rows = d.get_rows("SELECT email from users where email='{email}' and usertype='{usertype}' ".format(**post_data))
        if len(rows) > 0:
            return jsonify({'result': "email is already exists!"})
        else:
            d.query_insert( "INSERT INTO users (name, email, password, usertype) VALUES \
            ('{name}', '{email}', '{password}', '{usertype}')".format(**post_data))
        d.close_connection()
        return jsonify({'result':post_data})
    else:
        return jsonify({'result': msg})

@app.route('/Login', methods=['POST'])
def Login():
    post_data = request.get_json()
    valid, msg = validationServer.validateSignUP(post_data, ['email','password','usertype'])
    if(valid):
        d = db.DB()
        # hashed =  passwordEncrypt.encrypt_password(post_data.get('password'))
        passFromDb = d.get_rows("SELECT password from users where email='{email}' and usertype='{usertype}' ".format(**post_data))
        if passFromDb:
            passFromDb = ''.join(passFromDb[0])
            if passwordEncrypt.check_encrypted_password(post_data.get('password'),passFromDb):
                d.close_connection()
            else:
                return jsonify({'result': "Invalid Password"})
            access_token = create_access_token(identity = post_data['email'])
            refresh_token = create_refresh_token(identity = post_data['email'])
            print(access_token, refresh_token)
            return jsonify({
                'message': 'User {0} was created'.format(post_data['email']),
                'access_token': access_token,
                'refresh_token': refresh_token,
                'usertype': post_data['usertype']
            })
        else:
            return jsonify({'result': "Invalid Email / Password / UserType"})
    else:
        return jsonify({'result': msg})

   
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)