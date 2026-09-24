from fastapi import APIRouter, HTTPException
from httpx import HTTPStatusError, RequestError

from app.services.stocks import api_token, get_quotation

router = APIRouter(prefix="/ticker", tags=["stocks"])


@router.get("/{ticker}")
def read_ticker(ticker: str):
    try:
        return get_quotation(ticker.upper(), api_token)
    except HTTPStatusError as exc:
        raise HTTPException(
            status_code=exc.response.status_code,
            detail=f"Upstream error while requesting {exc.request.url!r}",
        )
    except RequestError as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Could not reach upstream API at {exc.request.url!r}",
        )
