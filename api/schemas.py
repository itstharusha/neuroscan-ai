
from pydantic import BaseModel
from typing import Any

class PredictRequest(BaseModel):
    __root__: dict[str, Any]
