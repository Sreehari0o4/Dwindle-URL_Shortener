from pydantic import BaseModel
from typing import Optional

class URLRequest(BaseModel):
    url: str
    custom_code: Optional[str] = None
    expires_in_hours: Optional[int] = None