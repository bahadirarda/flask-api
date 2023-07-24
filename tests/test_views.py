import unittest
from app import app, db

app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

test_client = app.test_client()

class TestViews(unittest.TestCase):
    def setUp(self):
        # Uygulama bağlantısı oluşturuluyor.
        self.app_context = app.app_context()
        self.app_context.push()

        # Veritabanını oluşturuluyor.
        db.create_all()

    def tearDown(self):
        # Veritabanı bağlantısını kapanıyor.
        db.session.remove()

        # Veritabanını siliniyor.
        db.drop_all()

        # Uygulama bağlantısı kapanıyor.
        self.app_context.pop()

    def test_add_employee(self):
        # Test için gerekli veriler oluşturuluyor.
        data = {
            "name": "Zlatan Ibrahimovic",
            "age": 30,
            "department": "HR"
        }

        # "add_employee" işlevine istek yapılıyor.
        response = test_client.post('/api/employees', json=data)

        # Doğrulama işlemi
        self.assertEqual(response.status_code, 201) # İşlem başarılı olduğu durumda geri bildirimi doğru alabilmek adına burada 200 yerine 201 kullanıyoruz
        self.assertEqual(response.json, {'status': 'success', 'message': 'Employee added successfully'})

if __name__ == '__main__':
    unittest.main()
