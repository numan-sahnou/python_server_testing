from flask import request
import json


def configure_routes(app):

    @app.route('/')
    def hello_world():
        return 'Assignment Numan SAHNOU'

    @app.route('/mean', methods=['GET'])
    def meanOfList():
        l = request.args.getlist('list', type=int)
        
        if len(l) == 0:
            return "No list were given"
        else:
            return "Mean of the list : {}".format(sum(l)/len(l))

