from flask import app, jsonify, request
from app import app, db
from app.models import Employee

# Çalışan ekleme
@app.route('/api/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    if data is None or not isinstance(data, dict):
        return jsonify({'error': 'Invalid data format'}), 400

    new_employee = Employee(name=data['name'], age=data['age'], department=data['department'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Employee added successfully'}), 201


# Çalışan güncelleme
@app.route('/api/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'status': 'error', 'message': 'Employee not found'})

    data = request.get_json()
    employee.name = data['name']
    employee.age = data['age']
    employee.department = data['department']
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Employee updated successfully'})

# Çalışan silme
@app.route('/api/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'status': 'error', 'message': 'Employee not found'})

    db.session.delete(employee)
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Employee deleted successfully'})

# Tüm çalışanları listeleme
@app.route('/api/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    employee_list = [{"id": employee.id, "name": employee.name, "age": employee.age, "department": employee.department} for employee in employees]
    return jsonify(employee_list)

# Departmanlarına göre çalışan filtreleme
@app.route('/api/employees/filter', methods=['GET'])
def filter_employees_by_department():
    department = request.args.get('department')
    filtered_employees = Employee.query.filter_by(department=department).all()
    employee_list = [{"id": employee.id, "name": employee.name, "age": employee.age, "department": employee.department} for employee in filtered_employees]
    return jsonify(employee_list)