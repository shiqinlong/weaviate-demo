import os
from uuid import UUID

from weaviate import Client
from models.query_params import QueryParams
from models.object_payload import ObjectPayload
from enum import Enum
import json


class ObjectOperation(Enum):
    LIST_OBJECT = "LIST_OBJECT"
    LIST_OBJECT_TENANT = "LIST_OBJECT_TENANT"
    LIST_ALL = "LIST_ALL"
    LIST_OBJECT_WITH_TENANT = "LIST_OBJECT_WITH_TENANT"
    GET_OBJECT_BY_ID = "GET_OBJECT_BY_ID"
    CREATE_OBJECT = "CREATE_OBJECT"
    DELETE_OBJECT = "DELETE_OBJECT"


async def object_call(client: Client, operation: ObjectOperation, query_params: QueryParams):
    if operation == ObjectOperation.LIST_OBJECT_WITH_TENANT:
        return client.data_object.get(class_name=query_params.class_name, tenant=query_params.tenant,
                                      offset=query_params.offset, limit=query_params.limit)

    if operation == ObjectOperation.LIST_ALL:
        return client.data_object.get(class_name=query_params.class_name)

    if operation == ObjectOperation.LIST_OBJECT_TENANT:
        if query_params.near_text is not None and len(query_params.near_text) != 0:
            near_texts = query_params.near_text.split(",")
            near_text_filter = {
                "concepts": near_texts
            }
            return client.query.get(query_params.class_name, ["question", "answer", "age", "category"])\
                .with_tenant(query_params.tenant) \
                .with_near_text(near_text_filter).with_limit(query_params.limit).do()

        return client.data_object.get(class_name=query_params.class_name, tenant=query_params.tenant,
                                      limit=query_params.limit)

    if operation == ObjectOperation.LIST_OBJECT:

        if query_params.properties is not None and len(query_params.properties) != 0:
            attributes = query_params.properties.split(",")
        if query_params.near_text is not None and len(query_params.near_text) != 0:
            near_texts = query_params.near_text.split(",")
            near_text_filter = {
                "concepts": near_texts
            }
            return client \
                .query \
                .get(query_params.class_name, attributes) \
                .with_near_text(near_text_filter) \
                .with_limit(query_params.limit) \
                .with_offset(query_params.offset).do()

        if query_params.additional_attr is not None and len(query_params.additional_attr) != 0:
            additional_attr = query_params.additional_attr.split(",")
            default = ["basedOn", "classifiedFields", "completed", "id"]
            return client \
                .query \
                .get(query_params.class_name, attributes) \
                .with_additional(additional_attr) \
                .with_limit(query_params.limit) \
                .with_offset(query_params.offset).do()

        return client \
            .query \
            .get(query_params.class_name, attributes) \
            .with_limit(query_params.limit) \
            .with_offset(query_params.offset).do()

    if operation == ObjectOperation.GET_OBJECT_BY_ID:
        return client.data_object.get_by_id(uuid=query_params.uuid,
                                            class_name=query_params.class_name)

    if operation == ObjectOperation.DELETE_OBJECT:
        return client.data_object.delete(uuid=query_params.uuid, class_name=query_params.class_name,
                                         consistency_level=query_params.consistency_level,
                                         tenant=query_params.tenant)


async def innit_objects(client: Client, class_name: str):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/init_data.json') as f:
        data = json.load(f)
        with client.batch(
                batch_size=100
        ) as batch:
            for i, d in enumerate(data):
                print(f"importing question: {i + 1}")

                properties = {
                    "answer": d["Answer"],
                    "question": d["Question"],
                    "category": d["Category"],
                    "age": d["Age"],
                }

                client.batch.add_data_object(data_object=properties, class_name=class_name)

    return "ok"


async def innit_objects_a(client: Client, class_name: str):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/init_data.json') as f:
        data = json.load(f)
        with client.batch(
                batch_size=100
        ) as batch:
            for i, d in enumerate(data):
                print(f"importing question: {i + 1}")

                properties = {
                    "answer": d["Answer"],
                    "question": d["Question"],
                    "category": d["Category"],
                    "age": d["Age"],
                }

                client.batch.add_data_object(data_object=properties, class_name=class_name, tenant="TENANTA")

    return "ok"


async def innit_objects_b(client: Client, class_name: str):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/init_data_b.json') as f:
        data = json.load(f)
        with client.batch(
                batch_size=100
        ) as batch:
            for i, d in enumerate(data):
                print(f"importing question: {i + 1}")

                properties = {
                    "answer": d["Answer"],
                    "question": d["Question"],
                    "category": d["Category"],
                    "age": d["Age"],
                }

                client.batch.add_data_object(data_object=properties, class_name=class_name, tenant="TENANTB")

    return "ok"


async def update_object_properties(client: Client, class_name: str, o_id: UUID, properties: dict):
    client.data_object.update(data_object=properties, class_name=class_name, uuid=o_id)
    return "ok"


async def delete_all_objects(client: Client, class_name: str):
    objs = client.data_object.get(class_name=class_name)
    obj = objs['objects']
    for i, d in enumerate(obj):
        client.data_object.delete(
            d['id'],
            class_name=d['class']
        )
    return "ok"


async def delete_all_objects_tenant(client: Client, class_name: str, tenant: str):
    objs = client.data_object.get(class_name=class_name, tenant=tenant)
    obj = objs['objects']
    for i, d in enumerate(obj):
        client.data_object.delete(
            uuid=d['id'],
            class_name=d['class'],
            tenant=tenant
        )
    return "ok"


async def object_call_create(client: Client, object_payload: ObjectPayload):
    return client.data_object.create(data_object=object_payload.data_object,
                                     class_name=object_payload.class_name, uuid=object_payload.uuid,
                                     vector=object_payload.vector,
                                     consistency_level=object_payload.consistency_level)


async def object_call_list(weaviaet_client: Client, class_name: str, tenant: str, limit: int = None,
                           offset: int = None):
    return weaviaet_client.data_object.get(class_name=class_name, tenant=tenant, limit=limit, offset=offset)
