import unittest

from app import app, db
import json

app.config['TESTING'] = True

test_client = app.test_client()

class TestViews(unittest.TestCase):
    def setUp(self):
        # Her test çalıştırılmadan önce burası çalışacak
        pass

    def tearDown(self):
        # Her test tamamlandıktan sonra burası çalışacak
        pass

    def test_add_employee(self):
        # Test için gerekli verileri oluşturun
        data = {
            "name": "John Doe",
            "age": 30,
            "department": "HR"
        }

        # "add_employee" işlevine istek yapın
        response = test_client.post('/api/employees', json=data)

        # Doğru cevabı aldığınızı ve çalışanın eklendiğini doğrulayın
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'status': 'success', 'message': 'Employee added successfully'})

if __name__ == '__main__':
    unittest.main()


#Çalıştırmak için python -m unittest tests.test_views
# __init__.py dosyasını oluşturmadıysanız çalıştırmak için python -m unittest discover tests

