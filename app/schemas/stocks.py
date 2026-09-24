from pydantic import BaseModel
from decimal import Decimal

class Quotation(BaseModel):
  symbol: str
  longName: str
  currency: str
  quote: Decimal
