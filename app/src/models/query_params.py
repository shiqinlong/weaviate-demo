from uuid import UUID
import uuid as uuid_lib
from pydantic import BaseModel
from typing import Optional, List, Dict, Union, Sequence
from weaviate import ConsistencyLevel


class QueryParams(BaseModel):
    uuid: Union[str, uuid_lib.UUID, None] = None,
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
    vector: Optional[Sequence] = None