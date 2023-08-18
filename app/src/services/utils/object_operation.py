from weaviate import Client
from pydantic import BaseModel
from models.query_params import QueryParams
from enum import Enum


class ObjectOperation(Enum):
    LIST_OBJECT = "LIST_OBJECT"
    GET_OBJECT_BY_ID = "GET_OBJECT_BY_ID"
    CREATE_OBJECT = "CREATE_OBJECT"
    DELETE_OBJECT = "DELEET_OBJECT"


async def object_api(weaviaet_client: Client, operation: ObjectOperation, queryParams: QueryParams):
    if operation == ObjectOperation.LIST_OBJECT:
        return weaviaet_client.data_object.get(uuid=queryParams.uuid,
                                               additional_properties=queryParams.additional_properties,
                                               with_vector=queryParams.with_vector,
                                               class_name=queryParams.class_name, node_name=queryParams.node_name,
                                               consistency_level=queryParams.consistency_level,
                                               limit=queryParams.limit, after=queryParams.after,
                                               offset=queryParams.offset,
                                               sort=queryParams.sort, tenant=queryParams.tenant)

    if operation == ObjectOperation.GET_OBJECT_BY_ID:
        return weaviaet_client.data_object.get_by_id(uuid=queryParams.uuid,
                                                     consistency_level=queryParams.consistency_level,
                                                     with_vector=queryParams.with_vector,
                                                     additional_properties=queryParams.additional_properties,
                                                     class_name=queryParams.class_name, node_name=queryParams.node_name,
                                                     tenant=queryParams.tenant)

    if operation == ObjectOperation.DELETE_OBJECT:
        return weaviaet_client.data_object.delete(uuid=queryParams.uuid, class_name=queryParams.class_name,
                                                  consistency_level=queryParams.consistency_level,
                                                  tenant=queryParams.tenant)
