from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class Data(Resource):
    def get(self, company):
        return "Echo:" + company, 200

    def post(self, name):
        return "No method error", 404

    def put(self):
        return "No method error", 404

    def delete(self):
        return "No method error", 404
      
api.add_resource(Data, "/data/<string:company>")

app.run(debug=True)