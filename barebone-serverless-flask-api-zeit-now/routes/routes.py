

from flask import Flask
from flask_restplus import Resource, reqparse
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from index import api

print ('inside routes.py')


parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate cannot be converted')
parser.add_argument('name')
args = parser.parse_args()



upload_parser = api.parser()

upload_parser.add_argument('file', location='uploads',
                           type=FileStorage, required=True) 


@api.route('/hello_routes')
class HelloRoutes(Resource):
    def get(self):
        return {'hello': 'routes'}

@api.route('/uploads')
@api.expect(upload_parser)
class Upload(Resource):
    def post(self):
        uploaded_file = args['file']  # This is FileStorage instance
        return {'file': 'uploaded'}
