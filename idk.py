from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class androidApi(Resource):
    def get(self):
        return {"Tanush":"IsGay"}

api.add_resource(androidApi, '/')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
