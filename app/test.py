from services.stocks import Ticker
from httpx import httpx, RequestError, HTTPStatusError
import os

api_endpoint = os.environ("API_ENDPOINT")



def get_quotation(ticker: str, token: str):

    quotation_uri = f"{api_endpoint}"
    response = httpx.get(quotation_uri)
    try:
        response.raise_for_status()
        print(response)
    except HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")

    

    return response