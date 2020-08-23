print('i am alive')
from flask import jsonify, request, Flask
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'Test'
app.config['MONGO_URL'] = 'mongodb://localhost:27017/Test'
api = Api(app)
mongo = MongoClient(app.config['MONGO_URL'])


class SimpleTask(Resource):
    def dict_to_mass(self, collection, task_id):
        output = []
        for task in collection.find():
            if str(task['_id']) == task_id:
                output.append({'_id': str(task['_id']), 'name': task['name']})
        return output

    def get(self, task_id):
        print("i in get")
        collection = mongo.Test.dev
        output = self.dict_to_mass(collection, task_id)
        if output:
            return jsonify({'result': output})
        else:
            output = "No such task"
        return jsonify({'result': output})


class PostTask(Resource):
    def post(self):
        print('i in post')
        collection = mongo.Test.dev
        name = request.values.get('name')
        collection_id = collection.insert({'name': name})
        output = {'_id': str(collection_id)}
        return jsonify({'result': output})


api.add_resource(SimpleTask, '/task/<task_id>')
api.add_resource(PostTask, '/task')

if __name__ == '__main__':
    app.run('0.0.0.0', '8084',debug=True)
