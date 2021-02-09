from chalice.app import Response
from chalicelib.api.swagger_api import swagger_api
from chalicelib.utils.swagger_utls import get_swagger_ui

from chalice import Chalice
import logging

# Set application name
app = Chalice(app_name='aws-chalice-template')
# Register blueprint
app.register_blueprint(swagger_api)

# Set logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


@app.route("/", methods=["GET"])
def get_doc():
    """Get Swagger UI Main Page

    Returns:
        str: text/html for Swagger UI page
    """

    html = get_swagger_ui(app)
    return Response(body=html, status_code=200,
                    headers={"Content-Type": "text/html"},)


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
@app.route('/hello/{name}')
def hello_name(name):
    # '/hello/james' -> {"hello": "james"}
    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
