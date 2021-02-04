from chalice.app import Request
from chalicelib.utils.url_utils import build_api_endpoint
from urllib import parse

MOCK_STAGE = "test"
MOCK_DOMAIN = "fake_domain"
MOCK_API_ID = "fake_api_id"


def test_url_build():

    mock_rq = Request(
        {
            "multiValueQueryStringParameters": None,
            "headers": {"a": "b", "c": "d"},
            "pathParameters": None,
            "body": None,
            "stageVariables": None,
            "requestContext": {
                "resourcePath": None,
                "httpMethod": None,
                "stage": MOCK_STAGE,
                "domainName": MOCK_DOMAIN,
                "apiId": MOCK_API_ID,
            },
        }
    )
    request_dict = mock_rq.to_dict()
    # print(request_dict.keys())
    context = request_dict["context"]
    # print(context)
    stage = context["stage"]
    assert stage == MOCK_STAGE
    # print(stage)
    api_domain = context["domainName"]
    # print(api_domain)
    assert api_domain == MOCK_DOMAIN
    api_id = context["apiId"]
    # print(api_id)
    assert api_id == MOCK_API_ID
    # build url
    url = build_api_endpoint(mock_rq, "/")
    # Is the url valid?
    result = parse.urlparse(url)
    # print(result)
    assert result is not None


def test_url_build_with_param():

    mock_rq = Request(
        {
            "multiValueQueryStringParameters": None,
            "headers": {"a": "b", "c": "d"},
            "pathParameters": None,
            "body": None,
            "stageVariables": None,
            "requestContext": {
                "resourcePath": None,
                "httpMethod": None,
                "stage": MOCK_STAGE,
                "domainName": MOCK_DOMAIN,
                "apiId": MOCK_API_ID,
            },
        }
    )
    request_dict = mock_rq.to_dict()
    # print(request_dict.keys())
    context = request_dict["context"]
    # print(context)
    stage = context["stage"]
    assert stage == MOCK_STAGE
    # print(stage)
    api_domain = context["domainName"]
    # print(api_domain)
    assert api_domain == MOCK_DOMAIN
    api_id = context["apiId"]
    # print(api_id)
    assert api_id == MOCK_API_ID
    # build url
    url = build_api_endpoint(mock_rq, "/", {"q1": "v1", "q2": "v2"})
    # Is the url valid?
    result = parse.urlparse(url)
    # print(f"{result.scheme}//{result.netloc}{result.path}{result.query}{result.params}")
    assert result is not None
