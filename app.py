import json
from db import db, Faculty, Class, Research
from flask import Flask, request

app = Flask(__name__)
db_filename = 'todo.db'
#Class.students.append(user)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/')
@app.route('/api/classes/')
def getClasses():
    classes = Class.query.all()
    res = {'success': True, 'data': [c.serializeall() for c in classes] }
    return json.dumps(res), 200

@app.route('/api/classes/', methods = ['POST'])
def createClass():
    post_body = json.loads(request.data)

    _class = Class(
        code = post_body.get('code'),
        name = post_body.get('name'),
        url = post_body.get('url')
    )
    db.session.add(_class)
    db.session.commit()
    return json.dumps({'success': True, 'data': _class.serializeall()}), 201

@app.route('/api/class/<int:_id>/')
def getClass(_id):
    classlist = Class.query.filter_by(id = _id).first()
    if classlist is None:
         return json.dumps({'success': False, 'error': 'Class not found'}), 404

    return json.dumps ({'success': True, 'data': classlist.serializeall()}), 200
   

@app.route('/api/class/<int:class_id>/', methods= ['DELETE'])
def deleteClass(class_id):
    classlist = Class.query.filter_by(id = class_id).first()
    if classlist is not None:
        db.session.delete(classlist)
        db.session.commit()
        return json.dumps ({'success': True, 'data': classlist.serializeall()}), 200
    return json.dumps({'success': False, 'error': 'Class not found'}), 404


@app.route('/api/faculty/', methods = ['POST'])
def createFaculty():
    post_body = json.loads(request.data)
    faculty = Faculty(
        name = post_body.get('name'),
        netid = post_body.get('netid')
    )
    db.session.add(faculty)
    db.session.commit()
    return json.dumps({'success': True, 'data': faculty.serializeall()}), 201

@app.route('/api/faculty/<int:faculty_id>/')
def getFaculty(faculty_id):
    faculty = Faculty.query.filter_by(id = faculty_id).first()
    if faculty is None:
         return json.dumps({'success': False, 'error': 'User not found'}), 404

    return json.dumps ({'success': True, 'data': faculty.serializeall()}), 200

@app.route('/api/class/<int:class_id>/add/', methods = ['POST'])
def addFaculty(class_id):
    class_item = Class.query.filter_by(id = class_id).first()
    if class_item is None:
        return json.dumps({'success': False, 'error': 'class not found'}), 404
    post_body = json.loads(request.data)
    faculty_id = post_body.get('faculty_id')
    class_item.faculty.append(Faculty.query.filter_by(id = faculty_id).first())
        
    db.session.commit()
    return json.dumps({'success': True, 'data': class_item.serializeid()}), 200

# @app.route('/api/class/<int:_id>/assignment/', methods = ['POST'])
# def createResearch(_id):
#     post_body = json.loads(request.data)
#     _class = Class.query.filter_by(id = _id).first()
#     if _class is None:
#         return json.dumps({'success': False, 'error': 'class not found'}), 404
#     assignment = Assignment(
#         class_id = _id,
#         description = post_body.get('description'),
#         due_date = post_body.get('due_date')
#     )
#     db.session.add(assignment)
#     db.session.commit()
#     return json.dumps({'success': True, 'data': assignment.serialize()}), 201



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)