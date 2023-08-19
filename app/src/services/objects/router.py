from typing import Union, List, Optional, Dict
from uuid import UUID
import json
from fastapi import APIRouter
from models.query_params import QueryParams
from models.object_payload import ObjectPayload
from services.weaviate.weaviate_template import WeaviateTemplate
from services.weaviate.object_operation import ObjectOperation
from weaviate import ConsistencyLevel

object_router = APIRouter()
weaviateTemplate = WeaviateTemplate()


@object_router.get("/list/{class_name}/{tenant}")
async def list_objects(class_name: str,
                       tenant: str,
                       limit: int = 25,
                       offset: int = 0):
    queryParams = QueryParams(class_name=class_name, tenant=tenant, limit=limit, offset=offset)
    return await weaviateTemplate.object_api(ObjectOperation.LIST_OBJECT, queryParams)


@object_router.post("")
async def create_object(objce_payload: ObjectPayload):
    return await weaviateTemplate.object_api_create(object_payload=objce_payload)
