#!/bin/python
from flask import Flask, request, make_response
from flask_restful import Api, Resource, fields, marshal_with, abort, reqparse, marshal
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

Devs_postargs = reqparse.RequestParser()
Devs_upadate_details = reqparse.RequestParser()

Devs_postargs.add_argument("name", type=str, help="Name is needed to add a new Dev", required=True)
Devs_postargs.add_argument("email", type=str, help="email is needed to add a new Dev", required =True)
Devs_postargs.add_argument("password", type=str, help="password is needed to add a new Dev", required=True)
Devs_postargs.add_argument("phone", type=str, help="Phone is needed to add a new Dev", required = True)

Devs_upadate_details.add_argument("name", type=str, help="Name is needed to add a new Dev")
Devs_upadate_details.add_argument("email", type=str, help="email is needed to add a new Dev")
Devs_upadate_details.add_argument("password", type=str, help="password is needed to add a new Dev")
Devs_upadate_details.add_argument("phone", type=str, help="Phone is needed to add a new Dev")

class DevsModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nphome: {self.phone}"

# with  app.app_context():
#     db.create_all()      

resource_fields = {
    "name": fields.String,
    "phone": fields.String,
    "email": fields.String
}  
def checkdb_exist(email):
    check = DevsModel.query.filter_by(email=email).first()
    if check:
        return abort(409, message=f"Developer email already in db {check}")
class DumpDevs(Resource):
    @marshal_with(resource_fields)
    def get(self, email=''):
        result = DevsModel.query.all()
        if not result:
            abort(404, message="Invalid Email")
        if email:
            user = DevsModel.query.filter_by(email=email).first()
            if not user:
                return abort(404, message=f"Invalid Email {email}")  
            return user
        return result
    @marshal_with(resource_fields)  
    def post(self, email=''):
        args = Devs_postargs.parse_args()
        email = args['email']
        checkdb_exist(email)        
        DevInfo = DevsModel(name=args['name'], phone=args['phone'], password=args['password'], email = args['email'])
        db.session.add(DevInfo)
        db.session.commit()        
        return DevInfo, 201

  
    def delete(self, email=''):  
        if email and DevsModel.query.filter_by(email=email):
            user = DevsModel.query.filter_by(email=email).first()
            db.session.delete(user)
            db.session.commit() 
            return {"Deleted user": email}
        else:
            abort(404, message="Please provide just the email of the user to be dropeed")                  
            

api.add_resource(DumpDevs, "/test/", "/test/<string:email>")     

if __name__ == '__main__':
    app.run(debug=True, port=5000)
