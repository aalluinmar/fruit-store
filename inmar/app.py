import db
import security
from flask import Flask
from mysql.connector import (connection)
from flaskext.mysql import MySQL
from flask import Flask, request, jsonify
from flask_cors import CORS
from passlib.hash import pbkdf2_sha256
app = Flask(__name__)
CORS(app)


@app.route('/register', methods=['POST'])
def register():
    payload = request.get_json()
    name = payload['name']
    email = payload['email']
    usertype = payload['usertype']
    password = payload['password']
    password = security.encrypt_password(password)
    db.cursor.execute(
        "SELECT email from users where email='" + str(email) + "' and usertype='"+str(usertype)+"' ")
    rows = db.cursor.fetchall()
    print(len(rows))
    if len(rows) > 0:
        return jsonify({'result': 0})
    else:
        db.cursor.execute(
            "INSERT INTO users (name, email, usertype, password) VALUES ('"
            + str(name) + "','" + str(email) +
            "','" + str(usertype) +
            "','" + str(password) + "')")
        db.cnx.commit()
        result = {
            'name': name,
            'email': email,
            'usertype': usertype,
            'password': password
        }
        return jsonify({'result': result})


@app.route('/rlogin', methods=['POST'])
def rlogin():
    payload = request.get_json()
    email = payload['email']
    usertype = payload['usertype']
    password = payload['password']
    db.cursor.execute("select password from users where email ='" +
                      str(email) + "' and usertype ='" + str(usertype) + "' ")
    dbpass = db.cursor.fetchall()
    if dbpass:
        dbpass = ''.join(dbpass[0])
        pwd = security.check_encrypted_password(password, dbpass)
        if pwd:
            db.cnx.commit()
            result = {
                'email': email,
                'usertype': usertype,
                'password': password
            }
            return jsonify({'result': result})
        else:
            return jsonify({'result': "INVALID PASSWORD"})
    else:
        return jsonify({'result': "INVALID EMAIL OR USERTYPE"})


@app.route('/adding', methods=['POST'])
def adding():
    payload = request.get_json()
    email = payload['email']
    # email="priya@gmail.com"
    # print(email)
    # usertype="Seller"
    usertype = payload['usertype']
    fruit = payload['fruit']
    quantity = payload['quantity']
    price = payload['price']
    # print(email,price)
    db.cursor.execute(
        "SELECT fruit from fruits_table where fruit='" + str(fruit) + " ' and email ='" + str(email) + "' ")
    # print(cursor)
    rows = db.cursor.fetchall()
    if len(rows) > 0:
        return jsonify({'result': 0})
    else:
        db.cursor.execute(
            "INSERT INTO fruits_table (email,usertype,fruit, quantity, price) VALUES ('"+str(email)+"','"+str(usertype)+"','"+str(fruit)+"','"+str(quantity)+"','" + str(price)+"')")
        db.cnx.commit()
    result = {
        'fruit': fruit,
        'quantity': quantity,
        'price': price,
        'email': email,
        'usertype': usertype
    }
    return jsonify({'result': result})


@app.route('/fetchingfruits', methods=['POST'])
def fetchingfruits():
    payload = request.get_json()
    email = payload['email']
    usertype = payload['usertype']
    db.cursor.execute(
        "SELECT fruit,quantity,price from fruits_table where email ='" + str(email) + "' and usertype ='" + str(usertype) + "' ")
    # print(cursor)
    rows = db.cursor.fetchall()
    db.cnx.commit()
    if len(rows) == 0:
        return jsonify({'result': 0})
    else:
        print(rows)
        result = {
            'fruitDetails': rows,
            'numberOfRows': len(rows)
        }
    return jsonify({'result': result})


@app.route('/updatingQuantity', methods=['POST'])
def updatingQuantity():
    payload = request.get_json()
    fruit = payload['fruit']
    quantity = payload['quantity']
    print(fruit, quantity)
    db.cursor.execute(
        "UPDATE fruits_table set quantity='" + str(quantity) + " ' where fruit='" + str(fruit) + "' ")
    db.cnx.commit()
    result = {
        'fruitName': fruit,
        'quantity': quantity
    }
    return jsonify({'result': result})


@app.route('/updatingPrice', methods=['POST'])
def updatingPrice():
    print("---------------------------")
    payload = request.get_json()
    fruit = payload['fruit']
    price = payload['price']
    print(fruit, price)
    db.cursor.execute(
        "UPDATE fruits_table set price='" + str(price) + " ' where fruit='" + str(fruit) + "' ")
    db.cnx.commit()
    result = {
        'fruitName': fruit,
        'price': price
    }
    return jsonify({'result': result})


@app.route('/fetchingallfruits', methods=['POST'])
def fetchingallfruits():
    payload = request.get_json()
    email = payload['email']
    usertype = payload['usertype']
    db.cursor.execute(
        "SELECT fruit,quantity,price from fruits_table where usertype ='" + str(usertype) + "' and email ='" + str(email) + "' ")
    # print(cursor)
    rows = db.cursor.fetchall()
    db.cnx.commit()
    if len(rows) == 0:
        return jsonify({'result': 0})
    else:
        print(rows)
        result = {
            'fruitDetails': rows,
            'numberOfRows': len(rows)
        }
    return jsonify({'result': result})


@app.route('/fetchingallretailers', methods=['POST'])
def fetchingallretailers():
    payload = request.get_json()
    # email = payload['email']
    usertype = payload['usertype']
    db.cursor.execute(
        "SELECT distinct email from fruits_table where usertype ='" + str(usertype) + "' ")
    # print(cursor)
    rows = db.cursor.fetchall()
    db.cnx.commit()
    if len(rows) == 0:
        return jsonify({'result': 0})
    else:
        print(rows)
        result = {
            'fruitDetails': rows,
            'numberOfRows': len(rows)
        }
    return jsonify({'result': result})


@app.route('/storingItemsInDB', methods=['POST'])
def storingItemsInDB():
    payload = request.get_json()
    email = payload['email']
    Cust_FruitName = "Cust_FruitName",
    Cust_FruitQuantity = 'Cust_FruitQuantity'
    Cust_FruitPrice = 'Cust_FruitPrice'
    Cust_FruitEnteredQuantity = 'Cust_FruitEnteredQuantity'
    Cust_ClickedSellerEmail = 'Cust_ClickedSellerEmail'
    db.cursor.execute(
        "INSERT INTO customer_purchase_table (email,Cust_FruitName, Cust_FruitQuantity, Cust_FruitPrice, Cust_FruitEnteredQuantity, Cust_ClickedSellerEmail ) VALUES ('"+str(email)+"','"+str(Cust_FruitName)+"','"+str(Cust_FruitQuantity)+"','"+str(Cust_FruitPrice)+"','" + str(Cust_FruitEnteredQuantity)+"','"+str(Cust_ClickedSellerEmail)+"')")
    # print(cursor)
    rows = db.cursor.fetchall()
    db.cnx.commit()
    if len(rows) == 0:
        return jsonify({'result': 0})
    else:
        result = {
            'email': email,
            'Cust_FruitName': Cust_FruitName,
            'Cust_FruitQuantity': Cust_FruitQuantity,
            'Cust_FruitPrice': Cust_FruitPrice,
            'Cust_FruitEnteredQuantity': Cust_FruitEnteredQuantity,
            'Cust_ClickedSellerEmail': Cust_ClickedSellerEmail
        }
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000,)
