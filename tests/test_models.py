import unittest
from app import app, db
from app.models import Employee

app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

test_client = app.test_client()

class TestModels(unittest.TestCase):
    def setUp(self):
        # Uygulama bağlantısı oluşturuluyor
        self.app_context = app.app_context()
        self.app_context.push()

        # Veritabanını oluşturuluyor
        db.create_all()

        # Test için gerekli verileri oluşturuluyor
        self.name = "Zlatan Ibrahimovic"
        self.age = 30
        self.department = "HR"

    def tearDown(self):
        # Veritabanı bağlantısını kapanıyor
        db.session.remove()

        # Veritabanı siliniyor
        db.drop_all()

        # Uygulama bağlantısı kapanıyor
        self.app_context.pop()

    def test_employee_creation(self):
        # Employee sınıfı ile yeni bir çalışan oluşturuluyor
        employee = Employee(name=self.name, age=self.age, department=self.department)

        # Çalışanı veritabanına ekleniyor
        db.session.add(employee)
        db.session.commit()

        # Veritabanından çalışan getiriliyor
        employee_from_db = Employee.query.filter_by(name=self.name).first()

        # Çalışanın veritabanına doğru şekilde eklendiği doğrulanıyor
        self.assertIsNotNone(employee_from_db)
        self.assertEqual(employee_from_db.name, self.name)
        self.assertEqual(employee_from_db.age, self.age)
        self.assertEqual(employee_from_db.department, self.department)

if __name__ == '__main__':
    unittest.main()
