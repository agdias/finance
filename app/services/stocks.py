import os

import httpx

api_endpoint = os.environ["API_ENDPOINT"]
api_token = os.environ["API_TOKEN"]
quotation_uri = f"{api_endpoint}/api/v2/stocks/quote"


def get_quotation(ticker: str, token: str) -> dict:
    response = httpx.get(
        quotation_uri,
        params={"symbols": ticker},
        headers={"Authorization": f"Bearer {token}"},
    )
    response.raise_for_status()
    return response.json()
