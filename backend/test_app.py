# pylint: disable-all
from flask import Flask
from flask import jsonify
import unittest
from app import app
import json
from unittest.mock import patch 
import passwordEncrypt

class FlaskTestCase(unittest.TestCase):

    #checking register with no data
    @patch('db.connection', return_value =  True)
    def test_register_with_no_data(self, connection):
        tester = app.test_client(self)
        response = tester.post('/register', data={}, content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

    #checking register with valid data
    @patch('db.connection', return_value =  True)
    def test_register_with_valid_data(self, connection):
        payload = {
            'usertype': 'Retailer',
            'name': 'Test',
            'email': 'alleba@gmail.com',
            'password': 'Test@123'
        }
        payload = json.dumps(payload)
        header={ "Content-Type": "application/json"}
        tester = app.test_client(self)
        response = tester.post('/register', data=payload, headers = header)
        final_output = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(final_output['result']['email'], 'alleba@gmail.com')

    #checking the register by passing wrong Values
    @patch('db.connection', return_value =  True)
    def test_register_with_passing_wrong_data(self, connection):
        payload = {
            'usertype': 'Retailer',
            'name': 'Test',
            'email': 'allebagmail.com',
            'password': 'Test@123'
        }
        payload = json.dumps(payload)
        header={ "Content-Type": "application/json"}
        tester = app.test_client(self)
        response = tester.post('/register', data=payload, headers = header)
        final_output = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(final_output['result'],  'Please provide valid email : allebagmail.com')
    
    #checking the register by missing column Values
    @patch('db.connection', return_value =  True)
    def test_register_with_missing_column_data(self, connection):
        payload = {
            'usertype': 'Retailer',
            'email': 'allebagmail.com',
            'password': 'Test@123'
        }
        payload = json.dumps(payload)
        header={ "Content-Type": "application/json"}
        tester = app.test_client(self)
        response = tester.post('/register', data=payload, headers = header)
        final_output = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(final_output['result'], 'Please provide name')

    #checking the register for checking existing email
    @patch('db.connection', return_value =  True)
    def test_register_with_existing_email_data(self, connection):
        with patch('db.DB.get_rows') as rows:
            rows.return_value = { 'email': 'alleba@gmail.com'}
            payload = {
                'usertype': 'Retailer',
                'name': 'Test',
                'email': 'alleba@gmail.com',
                'password': 'Test@123'
            }
            payload = json.dumps(payload)
            header={ "Content-Type": "application/json"}
            tester = app.test_client(self)
            response = tester.post('/register', data=payload, headers = header)
            final_output = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(final_output['result'], 'email is already exists!')


if __name__ == "__main__":
    unittest.main()