from chalice.app import Request
from typing import Optional, Dict
import logging
from urllib.parse import urlencode

logger = logging.getLogger()


def build_api_endpoint(
    current_request: Request, request_path: str, query_params: Optional[Dict] = None
) -> str:
    logger.info(f"Enter build_api_endpoint for {request_path}")
    request_dict = current_request.to_dict()

    context = request_dict["context"]
    stage = context["stage"]
    api_domain = context["domainName"]
    api_id = context["apiId"]

    if query_params is not None:
        if "api_id" in query_params:
            # replace api value with current api id
            query_params["api_id"] = api_id

        if "stage" in query_params:
            query_params["stage"] = stage

    url = f"https://{api_domain}/{stage}/{request_path.strip('/')}/?"
    if query_params is not None:
        url = url + urlencode(query_params)

    # print(url)
    return url
