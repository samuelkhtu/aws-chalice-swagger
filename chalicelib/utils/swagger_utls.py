from chalicelib.utils.url_utils import build_api_endpoint
from chalice import Chalice
import logging
from chalicelib.openapi import docs
import boto3
import json
from typing import Dict

logger = logging.getLogger()


def get_swagger_ui(app: Chalice) -> str:
    """Return Swagger UI HTML page

    Args:
        app (Chalice): Pointer to main app.py

    Returns:
        str: Swagger UI HTML
    """
    # Call internal API to retrieve static resource
    ui_bundle_js_url = build_api_endpoint(
        current_request=app.current_request, request_path="ui-bundle-js"
    )
    css_url = build_api_endpoint(
        current_request=app.current_request, request_path="css"
    )
    open_api_url = build_api_endpoint(
        current_request=app.current_request,
        request_path="swagger-url",
        query_params={"api_id": "", "stage": ""},
    )
    logger.info(f"open_api_url: {open_api_url}")
    logger.info(f"swagger_ui_bundle_js url: {ui_bundle_js_url}")
    logger.info(f"swagger_css url: {css_url}")

    html = docs.get_swagger_ui_html(
        openapi_url=open_api_url,
        title=app.app_name + " - Swagger UI",
        swagger_js_url=ui_bundle_js_url,
        swagger_css_url=css_url,
    )
    logger.debug(html)

    return html


def remove_base_path_slash(api_spec_json_dict: Dict) -> Dict:
    """Remove leading slash in basePath property

    Args:
        api_spec_json_dict (Dict): OpenAPI spec in json dictionary format

    Returns:
        Dict: json dictionary with leading slash removed from 'basePath'
    """
    for key, value in api_spec_json_dict.items():
        logger.debug(f"Json spec: {key}:{value}")
        if key == "servers":
            servers = api_spec_json_dict["servers"]
            for i in range(len(servers)):
                if "variables" in servers[i]:
                    variables = servers[i]["variables"]
                    logger.debug(f"servers[{i}]['variables'] = {variables}")
                    if "basePath" in variables:
                        base_path = variables["basePath"]
                        logger.debug(f"variables['basePath'] = {base_path}")
                        if "default" in base_path:
                            default_base_path = base_path["default"]
                            logger.debug(f"base_path['default'] = {default_base_path}")
                            # Remove leading '/' otherwise url will generate incorrect path
                            slash_stripped = default_base_path.strip("/")
                            # update json dictionary
                            api_spec_json_dict["servers"][i]["variables"]["basePath"][
                                "default"
                            ] = slash_stripped
                            logger.info(
                                f"default base_path = {api_spec_json_dict['servers'][i]['variables']['basePath']['default']}"
                            )
    return api_spec_json_dict


def export_api_to_json(app: Chalice, exportType: str = "oas30") -> str:
    """Call AWS API Gateway Export function to generate OAS json document

    Args:
        app (Chalice): Pointer to app.py
        exportType (str, optional): ExportType (oas30 for OpenAPI 3.0,
                    swagger for Swagger/OpenAPI 2.0). Defaults to "oas30".

    Returns:
        str: JSON API document
    """
    # Get query parameters from request
    api_id = app.current_request.query_params["api_id"]
    api_stage = app.current_request.query_params["stage"]

    # send export command
    client = boto3.client("apigateway")
    export_response = client.get_export(
        restApiId=api_id,
        stageName=api_stage,
        exportType=exportType,
        parameters={"extensions": "apigateway"},
    )
    # Get streaming body from response
    streamingBody = export_response["body"]
    # Read and decode the data
    body_data = streamingBody.read()
    decoded_content = body_data.decode("utf8")
    logger.debug(decoded_content)

    # Remove basePath's slash to prevent incorrect url
    api_spec = remove_base_path_slash(json.loads(decoded_content))

    # Load the JSON to a Python list & dump it back out as formatted JSON
    result = json.dumps(api_spec, indent=4, sort_keys=False)
    # print(s)

    return result
