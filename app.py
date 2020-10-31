from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


names = {"yuri": {"age": 30, "gender": "female"},
         "eric": {"age": 31, "gender": "male"}
         }

videos = {}


class Video(Resource):
    def get(selfself, video_id):
        return videos[video_id]

    def put(self, video_id):
        return {}

api.add_resource(Video, '/video/<int:video_id>')


class HelloWorld(Resource):
    def get(self, name):
        return names[name]


api.add_resource(HelloWorld, "/helloworld/<string:name>")


if __name__ == '__main__':
    app.run(debug=True)
