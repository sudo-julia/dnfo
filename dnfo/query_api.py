"""query the api for information on an endpoint"""
from __future__ import annotations
import sys
from typing import TypedDict
import requests
from dnfo import BASE_URL


# pylint: disable=R0903
class EndpointResponse(TypedDict):
    """dictionary typing for the response of any endpoint"""

    count: int
    results: list[dict[str, str]]


def query_endpoint(endpoint: str) -> EndpointResponse:
    """search an endpoint from the API with a given query
    return a dict containing the response
    """
    response = requests.get(f"{BASE_URL}/{endpoint}")
    if response.status_code != 200:
        sys.exit(1)
    response_dict: EndpointResponse = response.json()
    return response_dict


def query_index(endpoint: str, index: str):
    """query an index located at an endpoint of the api"""
    response = requests.get(f"{BASE_URL}/{endpoint}/{index}")
    if response.status_code != 200:
        sys.exit(1)
    return response
