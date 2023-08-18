from typing import Union, List, Optional, Dict
from uuid import UUID
import json
from fastapi import APIRouter
from models.query_params import QueryParams
from services.utils.weaviate_template import WeaviateTemplate
from services.utils.object_operation import ObjectOperation
from weaviate import ConsistencyLevel

object_router = APIRouter()
weaviateTemplate = WeaviateTemplate()


@object_router.get("/list")
async def list_objects(uuid: str = None,
                       additional_properties: str = None,
                       with_vector: bool = False,
                       class_name: Optional[str] = None,
                       node_name: Optional[str] = None,
                       consistency_level: Optional[ConsistencyLevel] = None,
                       limit: Optional[int] = None,
                       after: Optional[UUID] = None,
                       offset: Optional[int] = None,
                       sort: str = None,
                       tenant: Optional[str] = None):
    # queryParams = QueryParams()
    # if check_query_params(uuid):
    #     queryParams.uuid = uuid
    # if check_query_params(additional_properties):
    #     queryParams.additional_properties = additional_properties.split(",")
    # if check_query_params(class_name):
    #     queryParams.class_name = class_name
    # if check_query_params(with_vector):
    #     queryParams.with_vector = with_vector
    # if check_query_params(node_name):
    #     queryParams.node_name = node_name
    # if check_query_params(consistency_level):
    #     queryParams.consistency_level = consistency_level
    # if check_query_params(limit):
    #     queryParams.limit = limit
    # if check_query_params(after):
    #     queryParams.after = after
    # if check_query_params(offset):
    #     queryParams.offset = offset
    # if check_query_params(sort):
    #     queryParams.sort = json.loads(sort)
    # if check_query_params(tenant):
    #     queryParams.tenant = tenant
    # return weaviateTemplate.object_api(ObjectOperation.LIST_OBJECT, queryParams)
    return "success"


def check_query_params(data):
    return data is not None
