from typing import List

from pydantic import BaseModel


class NodeConnectionRequest(BaseModel):
    nodes: List[str]