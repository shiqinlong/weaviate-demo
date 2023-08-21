import json

from fastapi import APIRouter, HTTPException,Depends,Request
from services.auth.auth import OAuth2PasswordBearer

from services.weaviate.weaviate_template import WeaviateTemplate
from services.weaviate.schema_operation import SchemaOperation
from services.weaviate.schema_operation import isSchemaExists

schema_router = APIRouter()
weaviateTemplate = WeaviateTemplate()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/schema/token")

@schema_router.get("/list")
async def fetch_all_schemas():
    # print(f"token : {token}")
    return await weaviateTemplate.class_api(SchemaOperation.GET_CLASS)

# @schema_router.post("/token")
# async def fetch_all_schemas(request:Request):
#     print(f"token test{request}",)
#     return "success "

@schema_router.get("/{name}")
async def fetch_schema_by_name(name: str):
    if isSchemaExists(weaviateTemplate.get_weaviate_client(), name):
        return await weaviateTemplate.class_api(operation=SchemaOperation.GET_CLASS_BY_NAME,
                                                class_name=name)
    else:
        raise HTTPException(404, "Not found class by {}".format(name))


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
