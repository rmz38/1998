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
def getHello():
    return "HELLOWORLD"
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

@app.route('/api/class/<string:class_code>/')
def getClass(class_code):
    classlist = Class.query.filter_by(code = class_code).first()
    if classlist is None:
         return json.dumps({'success': False, 'error': 'Class not found'}), 404

    return json.dumps ({'success': True, 'data': classlist.serializeall()}), 200
   

@app.route('/api/class/<string:class_code>/', methods= ['DELETE'])
def deleteClass(class_code):
    classlist = Class.query.filter_by(code = class_code).first()
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

@app.route('/api/faculty/<string:faculty_name>/')
def getFaculty(faculty_name):
    faculty = Faculty.query.filter_by(name = faculty_name).first()
    if faculty is None:
         return json.dumps({'success': False, 'error': 'User not found'}), 404

    return json.dumps ({'success': True, 'data': faculty.serialize()}), 200

@app.route('/api/class/<string:class_code>/add_faculty/', methods = ['POST'])
def addFaculty(class_code):
    class_item = Class.query.filter_by(code = class_code).first()
    if class_item is None:
        return json.dumps({'success': False, 'error': 'class not found'}), 404
    post_body = json.loads(request.data)
    faculty_id = post_body.get('faculty_id')
    class_item.faculty.append(Faculty.query.filter_by(id = faculty_id).first())
        
    db.session.commit()
    return json.dumps({'success': True, 'data': class_item.serializeall()}), 200

@app.route('/api/class/<string:class_code>/research/', methods = ['POST'])
def createResearch(class_code):
    post_body = json.loads(request.data)
    class_found = Class.query.filter_by(code = class_code).first()
    if class_found is None:
        return json.dumps({'success': False, 'error': 'class not found'}), 404
    assignment = Research(
        class_id = class_found.id,
        description = post_body.get('description'),
        subject = post_body.get('subject')
    )
    db.session.add(assignment)
    db.session.commit()
    return json.dumps({'success': True, 'data': assignment.serialize()}), 201
@app.route('/api/research/', methods = ['GET'])
def getAllResearch():
    research = Research.query.all()
    res = {'success': True, 'data': [r.serialize() for r in research] }
    return json.dumps(res), 200
@app.route('/api/research/<string:research_name>/', methods = ['GET'])
def getResearch(research_name):
    post_body = json.loads(request.data)
    research_found = Research.query.filter_by(subject = research_name).first()
    if research_found is None:
        return json.dumps({'success': False, 'error': 'research not found'}), 404
    return json.dumps({'success': True, 'data': research_found.serialize()}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)