from uuid import UUID
from fastapi import APIRouter
from models.query_params import QueryParams
from models.object_payload import ObjectPayload
from services.weaviate.weaviate_template import WeaviateTemplate
from services.weaviate.object_operation import ObjectOperation

object_router = APIRouter()
weaviateTemplate = WeaviateTemplate()


@object_router.post("")
async def create_object(object_payload: ObjectPayload):
    return await weaviateTemplate.object_api_create(object_payload=object_payload)


@object_router.put("")
async def init_data(class_name: str):
    return await weaviateTemplate.innit_objects(class_name=class_name)


@object_router.get("/list/{class_name}")
async def fetch_objects_by_condition(class_name: str,
                                     properties: str,
                                     near_text: str = None,
                                     additional_attr: str = None,
                                     limit: int = 3,
                                     offset: int = 0):
    query_params = QueryParams(class_name=class_name, limit=limit, offset=offset,
                               properties=properties, near_text=near_text, additional_attr=additional_attr)
    return await weaviateTemplate.object_api(ObjectOperation.LIST_OBJECT, query_params)


@object_router.get("/all/{class_name}")
async def fetch_all_objects_by_class(class_name: str):
    query_params = QueryParams(class_name=class_name)
    return await weaviateTemplate.object_api(ObjectOperation.LIST_ALL, query_params)


@object_router.get("/{class_name}")
async def get_object_by_id_and_name(class_name: str, o_id: UUID):
    query_params = QueryParams(class_name=class_name, uuid=o_id)
    return await weaviateTemplate.object_api(ObjectOperation.GET_OBJECT_BY_ID, query_params)


@object_router.patch("/update")
async def update_object_properties(class_name: str, o_id: UUID, properties: dict):
    return await weaviateTemplate.update_object_properties(class_name=class_name, o_id=o_id, properties=properties)


@object_router.delete("/clean")
async def delete_all(class_name: str):
    return await weaviateTemplate.delete_all_objects(class_name=class_name)
