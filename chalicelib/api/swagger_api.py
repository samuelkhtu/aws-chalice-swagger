from chalice import Blueprint
from chalice.app import Response
from chalicelib.utils.file_utils import get_static_file
from chalicelib.utils.swagger_utls import export_api_to_json

import logging

# Get logger
logger = logging.getLogger()
swagger_api = Blueprint(__name__)


@swagger_api.route("/css", methods=["GET"])
def get_css():
    """Get Swagger UI CSS Endpoint

    Returns:
        str: CSS Content from Static folder
    """
    css_file = "swagger-ui.css"
    logger.info(f"Endpoint: Get CSS : {css_file} static file")
    try:
        content = get_static_file(file_name=css_file)
        return Response(
            body=content, status_code=200,
            headers={"Content-Type": "text/css"},
        )
    except Exception as ex:
        return Response(body=f"Failed request: {css_file}. {ex}",
                        status_code=404)


@swagger_api.route("/ui_bundle_js", methods=["GET"])
def get_swagger_ui_bundle():
    """Get Swagger UI Bundle JS Endpoint

    Returns:
        str: Return JavaScript for Swagger UI from static folder
    """
    ui_js_file = "swagger-ui-bundle.js"
    logger.info(f"Endpoint: Get CSS : {ui_js_file} static file")
    content = get_static_file(file_name=ui_js_file)
    try:
        return Response(
            body=content,
            status_code=200,
            headers={"Content-Type": "application/javascript; charset=utf-8"},
        )
    except Exception as ex:
        return Response(body=f"{ui_js_file} not found. {ex}", status_code=404)


@swagger_api.route("/swagger_url", methods=["GET"])
def get_swagger_url():
    return export_api_to_json(swagger_api.current_app)
