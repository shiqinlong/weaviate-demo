import uuid as uuid_lib
from typing import Optional, Sequence, Union, List, Any

from pydantic import BaseModel
from weaviate import ConsistencyLevel


class ObjectPayload(BaseModel):
    data_object: Union[dict, str]
    class_name: str
    tenant: str
    uuid: Union[str, uuid_lib.UUID, None] = None,
    vector: Optional[Sequence] = None,
    consistency_level: Optional[ConsistencyLevel] = None,


class ObjectBatchCreatePayload(BaseModel):
    data_objects: List[dict[str, Any]]
    class_name: str
    tenant: str


class ObjectBatchDeletePayload(BaseModel):
    data_objects: List[dict[str, Any]]
    class_name: str
    tenant: str