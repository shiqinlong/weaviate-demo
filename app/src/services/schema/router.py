import json

from fastapi import APIRouter
from services.weaviate.weaviate_template import WeaviateTemplate
from services.weaviate.schema_operation import SchemaOperation

schema_router = APIRouter()
weaviateTemplate = WeaviateTemplate()


@schema_router.get("")
async def fetch_all_schemas():
    return await weaviateTemplate.class_api(SchemaOperation.GET_CLASS)


@schema_router.get("/{name}")
async def fetch_schema_by_name(name: str):
    result = await weaviateTemplate.class_api(operation=SchemaOperation.GET_CLASS_BY_NAME,
                                              class_name=name)
    print(f"{json.dumps(result)}")
    return result


@schema_router.post("")
async def create_schema(payload: dict):
    await weaviateTemplate.class_api(operation=SchemaOperation.CREATE_CLASS,
                                     payload=payload)


@schema_router.delete("/{name}")
async def delete_schema(name: str):
    return await weaviateTemplate.class_api(operation=SchemaOperation.DELETE_CLASS,
                                            class_name=name)


@schema_router.put("/{name}")
async def update_schema(name: str, payload: dict):
    return await weaviateTemplate.class_api(operation=SchemaOperation.UPDATE_CLASS,
                                            class_name=name,
                                            payload=payload)


@schema_router.put("/{class_name}/properties")
async def add_properties(name: str, payload: dict):
    return await weaviateTemplate.class_api(operation=SchemaOperation.ADD_PROPER,
                                            class_name=name,
                                            payload=payload)
