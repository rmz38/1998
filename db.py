from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


db = SQLAlchemy()

association_faculty_class = db.Table('association_faculty_class',
    db.Column('faculty_id', db.Integer, db.ForeignKey('faculty.id')),
    db.Column('class_id', db.Integer, db.ForeignKey('class.id'))
)
association_faculty_research = db.Table('association_faculty_research',
    db.Column('faculty_id', db.Integer, db.ForeignKey('faculty.id')),
    db.Column('research_id', db.Integer, db.ForeignKey('research.id'))
)

class Faculty(db.Model):
    __tablename__ = 'faculty'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    netid = db.Column(db.String, nullable = False)
    faculty_classes = db.relationship("Class", secondary = association_faculty_class, backref = 'faculty')
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.netid = kwargs.get('netid', '')

    def serializeall(self):
        return {
            'id':self.id,
            'name': self.name,
            'netid': self.netid,
            'classes': [i.serialize() for i in self.faculty_classes]
        }

    def serialize(self):
        return {
            'id':self.id,
            'name': self.name,
            'netid': self.netid
        }

class Class(db.Model):
    __tablename__ = 'class'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable = False)
    name = db.Column(db.String, nullable = False)
    url = db.Column(db.String, nullable = False)
    def __init__(self, **kwargs):
        self.code = kwargs.get('code', '')
        self.name = kwargs.get('name', '')
        self.url = kwargs.get('url', '')

    def serialize(self):
        return {
            'code': self.code,
            'name': self.name,
            'url': self.url
        }
    def serializeid(self):
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'url': self.url
        }
    def serializeall(self):
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'url': self.url,
            'faculty': [i.serialize() for i in self.faculty]
            
        }

class Research(db.Model):
    __tablename__ = 'research'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable = False)
    subject = db.Column(db.String, nullable = False)
    def __init__(self, **kwargs):
        self.description = kwargs.get('description')
        self.subject = kwargs.get('subject')

    def serialize(self):
        return{
            'id': self.id,
            'description': self.description,
            'subject': self.subject
        }


