from flask.ext.restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate connot be converted')
parser.add_argument('name', type=str, action='append')
args = parser.parse_args()
