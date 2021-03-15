"""query the api for information on an endpoint"""
from __future__ import annotations
from typing import TypedDict
import requests
from dnfo import BASE_URL


# pylint: disable=R0903
class EndpointResponse(TypedDict):
    """dictionary typing for the response of any endpoint"""

    count: int
    results: list[dict[str, str]]


def query_endpoint(endpoint: str) -> EndpointResponse | int:
    """search an endpoint from the API with a given query
    return a dict containing the response
    """
    response = requests.get(f"{BASE_URL}/{endpoint}")
    if response.status_code != 200:
        return 1
    response_dict: EndpointResponse = response.json()
    return response_dict
