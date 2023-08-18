from fastapi import APIRouter
from services.utils.weaviate_template import WeaviateTemplate, SchemaOperation

schema_api = APIRouter()
weaviateTemplate = WeaviateTemplate()


@schema_api.get("")
async def fetch_all_schemas():
    return await weaviateTemplate.class_api(SchemaOperation.GET_CLASS)


@schema_api.get("/{name}")
async def fetch_schema_by_name(name: str):
    return await weaviateTemplate.class_api(operation=SchemaOperation.GET_CLASS,
                                            class_name=name)


@schema_api.post("")
async def create_schema(payload: str):
    await weaviateTemplate.class_api(operation=SchemaOperation.CREATE_CLASS,
                                     payload=payload)


@schema_api.delete("/{name}")
async def delete_schema(name: str):
    return await weaviateTemplate.class_api(operation=SchemaOperation.DELETE_CLASS,
                                            class_name=name)


@schema_api.put("/{name}")
async def update_schema(name: str, payload: str):
    return await weaviateTemplate.class_api(operation=SchemaOperation.UPDATE_CLASS,
                                            class_name=name,
                                            payload=payload)


@schema_api.put("/{class_name}/properties")
async def add_properties(name: str, payload: str):
    return await weaviateTemplate.class_api(operation=SchemaOperation.ADD_PROPER,
                                            class_name=name,
                                            payload=payload)
