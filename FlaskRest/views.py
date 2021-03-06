print('i am alive')
import os
from flask import jsonify, request, Flask
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE'] + '?authSource=admin'
api = Api(app)
mongo = MongoClient(app.config["MONGO_URI"])
db = mongo.Test

class SimpleTask(Resource):
    def dict_to_mass(self, collection, task_id):
        output = []
        for task in collection.find():
            if str(task['_id']) == task_id:
                output.append({'_id': str(task['_id']), 'name': task['name']})
        return output

    def get(self, task_id):
        print("i in get")
        collection = db.dev
        output = self.dict_to_mass(collection, task_id)
        if output:
            return jsonify({'result': output})
        else:
            output = "No such task"
        return jsonify({'result': output})


class PostTask(Resource):
    def post(self):
        print('i in post')
        collection = db.dev
        print(collection)
        name = request.values.get('name')
        print(name)
        collection_id = collection.insert({'name': name})
        print(collection_id)
        output = {'_id': str(collection_id)}
        return jsonify({'result': output})


api.add_resource(SimpleTask, '/task/<task_id>')
api.add_resource(PostTask, '/task')

if __name__ == '__main__':
    app.run('0.0.0.0', '8084',debug=True)
