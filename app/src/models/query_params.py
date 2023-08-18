from uuid import UUID

from pydantic import BaseModel
from typing import Optional, List, Dict, Union
from weaviate import ConsistencyLevel


class QueryParams(BaseModel):
    uuid: str = None,
    additional_properties: List[str] = None,
    with_vector: bool = False,
    class_name: Optional[str] = None,
    node_name: Optional[str] = None,
    consistency_level: Optional[ConsistencyLevel] = None,
    limit: Optional[int] = None,
    after: Optional[UUID] = None,
    offset: Optional[int] = None,
    sort: Optional[Dict[str, Union[str, bool, List[bool], List[str]]]] = None,
    tenant: Optional[str] = None,
