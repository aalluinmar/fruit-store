# pylint: disable-all
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from datetime import datetime
from flask import render_template
from flaskext.mysql import MySQL
from mysql.connector import (connection)
from passlib.hash import pbkdf2_sha256
from datetime import datetime
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

#User Registration
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

#User Login
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
            return jsonify({
                'message': '{0}'.format(post_data['email']),
                'access_token': access_token,
                'refresh_token': refresh_token,
                'usertype': post_data['usertype']
            })
        else:
            return jsonify({'result': "Invalid Email / Password / UserType"})
    else:
        return jsonify({'result': msg})

#Adding Fruits To DataBase
@jwt_required
@app.route('/addFruitsToDb', methods=['POST'])
def addFruitsToDb():
    post_data = request.get_json()
    fruitName = post_data['fruitName']
    quantity = post_data['quantity']
    price = post_data['price']
    sellerEmail = post_data['sellerEmail']
    d = db.DB()
    rows = d.get_rows("SELECT FruitName from seller_fruits where sellerEmail='{sellerEmail}' and FruitName='{fruitName}' ".format(**post_data))
    if len(rows) > 0:
        return jsonify({'result': "Fruit already exists!"})
    else:
        d.query_insert( "INSERT INTO seller_fruits (sellerEmail, FruitName, Quantity, Price) VALUES \
            ('{sellerEmail}', '{fruitName}', '{quantity}', '{price}' )".format(**post_data))
    d.close_connection()
    return jsonify({'result':post_data})

#Display existing Fruits to Seller Dashboard
@jwt_required
@app.route('/showAllFruits', methods=['POST'])
def showAllFruits():
    post_data = request.get_json()
    sellerEmail = post_data['sellerEmail']
    d = db.DB()
    rows = d.get_rows("SELECT * from seller_fruits where sellerEmail='{sellerEmail}' ".format(**post_data))
    if len(rows) == 0:
        return jsonify({'result': "No Fruits exists!"})
    else:
        return jsonify({'FruitsFromDB': rows, 'numberOfFruitsFromDB': len(rows) })
    d.close_connection()

#update Seller fruit Quantity or Price
@jwt_required
@app.route('/updateSellerFruit', methods=['POST'])
def updateSellerFruit():
    post_data = request.get_json()
    sellerEmail = post_data['sellerEmail']
    whichType = post_data['whichType']
    enteredThing = post_data['enteredThing']
    fruitName = post_data['fruitName']
    d = db.DB()
    if whichType == "quantity":    
        d.query_insert( "UPDATE seller_fruits set Quantity = {enteredThing} where sellerEmail='{sellerEmail}' and FruitName='{fruitName}'".format(**post_data))
        d.close_connection()
        return jsonify({'result': "quantity updated"})
    elif whichType == "price":
        d.query_insert( "UPDATE seller_fruits set Price = {enteredThing} where sellerEmail='{sellerEmail}' and FruitName='{fruitName}'".format(**post_data))
        d.close_connection()
        return jsonify({'result': "price updated"})
    else:
        d.query_insert( "DELETE from seller_fruits where sellerEmail='{sellerEmail}' and FruitName='{fruitName}'".format(**post_data))
        d.close_connection()
        return jsonify({'result': "fruit deleted"})

#display all retailers to the Customer dashboard
@jwt_required
@app.route('/retailersFromDB', methods=['POST'])
def retailersFromDB():
    post_data = request.get_json()
    usertype = post_data['usertype']
    d = db.DB()
    rows = d.get_rows("SELECT name, email from users where usertype='{usertype}'".format(**post_data))
    if len(rows) == 0:
        return jsonify({'result': "No Retailers found"})
    else:
        return jsonify({'retailersDB': rows, 'numberOfretailersFromDB': len(rows) })
    d.close_connection()

#fetching particular retailer fruits
@jwt_required
@app.route('/displayParticularRetailerFruits', methods=['POST'])
def displayParticularRetailerFruits():
    post_data = request.get_json()
    retailerEmail = post_data['retailerEmail']
    d = db.DB()
    rows = d.get_rows("SELECT * from seller_fruits where sellerEmail='{retailerEmail}'".format(**post_data))
    if len(rows) == 0:
        return jsonify({'result': "No fruits found"})
    else:
        return jsonify({'particularRetailerFruits': rows, 'numberOfParticularRetailerFruitsFromDB': len(rows) })
    d.close_connection()

#deleted Customer particular fruit from cart
#delete Customer particular fruit from cart
@jwt_required
@app.route('/deleteParticularFruitFromCart', methods=['POST'])
def deleteParticularFruitFromCart():
    post_data = request.get_json()
    print(post_data)
    retailerEmail = post_data['retailerEmail']
    customerEmail = post_data['customerEmail']
    fruitName = post_data['fruitName']
    d = db.DB()
    d.query_insert("DELETE FROM customercartitems where retailerEmail='{retailerEmail}' and (customerEmail='{customerEmail}' and custFruitName='{fruitName}')".format(**post_data))
    return jsonify({'particularCustomerCart': 1 })
    d.close_connection()


#Customer Cart Items
@jwt_required
@app.route('/addItemsTocart', methods=['POST'])
def addItemsTocart():
    post_data = request.get_json()
    print(post_data)
    customerEmail = post_data['customerEmail']
    retailerEmail = post_data['retailerEmail']
    custFruitName = post_data['custFruitName']
    custQuantity = post_data['custQuantity']
    custPrice = post_data['custPrice']
    custEnteredQuantity = post_data['custEnteredQuantity']
    d = db.DB()
    if custEnteredQuantity == 0:
        print("1")
        d.query_insert( "DELETE from customerCartItems where retailerEmail='{retailerEmail}' and custFruitName = '{custFruitName}'".format(**post_data))
        return jsonify({'itemscartDB': post_data, 'numberOfItemsFromCartDBdeleted': 0})
    rows = d.get_rows("SELECT * from customerCartItems where retailerEmail='{retailerEmail}' and custFruitName = '{custFruitName}'".format(**post_data))
    if len(rows) > 0:
        print("2")
        d.query_insert( "UPDATE customerCartItems set custEnteredQuantity = '{custEnteredQuantity}' where retailerEmail='{retailerEmail}' and custFruitName='{custFruitName}'".format(**post_data))
        return jsonify({'itemscartDB': post_data, 'numberOfItemsFromCartDB': 1})
    else:
        print("3")
        d.query_insert( "INSERT INTO customerCartItems (retailerEmail, customerEmail, custFruitName, custQuantity, custPrice, custEnteredQuantity) VALUES \
            ('{retailerEmail}', '{customerEmail}','{custFruitName}', '{custQuantity}', '{custPrice}', '{custEnteredQuantity}' )".format(**post_data))
        return jsonify({'itemscartDB': post_data, 'numberOfItemsFromCartDB': 1 })
    d.close_connection()


#customer purchased fruits from each retailer
@jwt_required
@app.route('/customerTransaction', methods=['POST'])
def customerTransaction():
    post_data = request.get_json()
    customerEmail = post_data['customerEmail']
    d = db.DB()
    transId = str(datetime.now())
    DateAndTime = str(datetime.now())
    newtransId = transId.replace(" ","")
    newtransId = newtransId.replace(".","")
    newtransId = newtransId.replace(":","")
    newtransId = newtransId.replace("-","")
    newtransId = newtransId[0:14]
    for payload in post_data['customerClickedItemsToStoreInDb']:
        print(payload)
        totalPrice = payload['Cust_FruitPrice'] * payload['Cust_FruitEnteredQuantity']
        sellerEmail = payload['Cust_ClickedSellerEmail']
        fruitName = payload['Cust_FruitName']
        quantity = payload['Cust_FruitQuantity']
        purchasedQuantity = payload['Cust_FruitEnteredQuantity']
        price = payload['Cust_FruitPrice']
        d.query_insert( "INSERT INTO customertransaction (sellerEmail, customerEmail, FruitName, Quantity, purchasedQuantity, Price, totalPrice, transactionID, DateAndTime) VALUES \
            ('"+str(sellerEmail)+"', '"+str(customerEmail)+"', '"+str(fruitName)+"', '"+str(quantity)+"', '"+str(purchasedQuantity)+"', '"+str(price)+"', '"+str(totalPrice)+"', '"+str(newtransId)+"', '"+str(DateAndTime)+"' )")
        QuantUpdateSeller = quantity - purchasedQuantity
        print("success")
        d.query_insert(" UPDATE seller_fruits set Quantity='"+str(QuantUpdateSeller)+"' where sellerEmail='"+str(sellerEmail)+"' and FruitName='"+str(fruitName)+"' ")            
    d.query_insert( "DELETE from customerCartItems where customerEmail='{customerEmail}' ".format(**post_data))
    d.close_connection()    
    return jsonify({'result': post_data })

#customer cart details fetching
@jwt_required
@app.route('/customerCartDetails', methods=['POST'])
def customerCartDetails():
    post_data = request.get_json()
    customerEmail = post_data['customerEmail']
    d = db.DB()
    rows = d.get_rows("SELECT * from customerCartItems where customerEmail='{customerEmail}'".format(**post_data))
    if len(rows) == 0:
        return jsonify({'result': "No Items in Cart", 'cartRows': len(rows)})
    else:
        return jsonify({'cartItemsFromDB': rows, 'cartRows': len(rows) })
    d.close_connection()


#fetching transaction details of customer
@jwt_required
@app.route('/transactionHistory', methods=['POST'])
def transactionHistory():
    post_data = request.get_json()
    customerEmail = post_data['customerEmail']
    d = db.DB()
    rows = d.get_rows("SELECT * from customertransaction where customerEmail='{customerEmail}'".format(**post_data))
    if len(rows) == 0:
        return jsonify({'result': "No Transactions found upto date", 'transactionRows': len(rows)})
    else:
        return jsonify({'transactionHistory': rows, 'transactionRows': len(rows) })
    d.close_connection()

#fetching transaction details of retailer
@jwt_required
@app.route('/transactionHistoryRetailer', methods=['POST'])
def transactionHistoryRetailer():
    post_data = request.get_json()
    sellerEmail = post_data['sellerEmail']
    d = db.DB()
    rows = d.get_rows("SELECT * from customertransaction where sellerEmail='{sellerEmail}'".format(**post_data))
    if len(rows) == 0:
        return jsonify({'result': "No Transactions found upto date", 'transactionRows': len(rows)})
    else:
        return jsonify({'transactionHistory': rows, 'transactionRows': len(rows) })
    d.close_connection()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)