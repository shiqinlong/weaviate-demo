from weaviate import Client
from pydantic import BaseModel
from models.query_params import QueryParams
from models.object_payload import ObjectPayload
from enum import Enum


class ObjectOperation(Enum):
    LIST_OBJECT = "LIST_OBJECT"
    GET_OBJECT_BY_ID = "GET_OBJECT_BY_ID"
    CREATE_OBJECT = "CREATE_OBJECT"
    DELETE_OBJECT = "DELEET_OBJECT"


async def object_call(weaviate_client: Client, operation: ObjectOperation, queryParams: QueryParams):
    if operation == ObjectOperation.LIST_OBJECT:
        return weaviate_client.data_object.get(class_name=queryParams.class_name, tenant=queryParams.tenant,
                                               offset=queryParams.offset, limit=queryParams.limit)

    if operation == ObjectOperation.GET_OBJECT_BY_ID:
        return weaviate_client.data_object.get_by_id(uuid=queryParams.uuid,
                                                     class_name=queryParams.class_name,
                                                     tenant=queryParams.tenant)

    if operation == ObjectOperation.DELETE_OBJECT:
        return weaviate_client.data_object.delete(uuid=queryParams.uuid, class_name=queryParams.class_name,
                                                  consistency_level=queryParams.consistency_level,
                                                  tenant=queryParams.tenant)


async def object_call_create(weaviate_client: Client, object_payload: ObjectPayload):
    return weaviate_client.data_object.create(data_object=object_payload.data_object,
                                              class_name=object_payload.class_name, uuid=object_payload.uuid,
                                              vector=object_payload.vector,
                                              consistency_level=object_payload.consistency_level)


async def object_call_list(weaviaet_client: Client, class_name: str, tenant: str, limit: int = None,
                           offset: int = None):
    return weaviaet_client.data_object.get(class_name=class_name, tenant=tenant, limit=limit, offset=offset)
