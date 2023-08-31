from fastapi import APIRouter
from models.query_params import QueryParams
from services.weaviate.weaviate_template import WeaviateTemplate
from services.weaviate.object_operation import ObjectOperation

object_tenant_router = APIRouter()
weaviateTemplate = WeaviateTemplate()


@object_tenant_router.put("/tenant-a")
async def init_data_with_tenant_a(class_name: str):
    return await weaviateTemplate.innit_objects_a(class_name=class_name)


@object_tenant_router.put("/tenant-b")
async def init_data_with_tenant_b(class_name: str):
    return await weaviateTemplate.innit_objects_b(class_name=class_name)


@object_tenant_router.get("/list/{class_name}/{tenant}")
async def fetch_objects_by_condition(class_name: str,
                                     tenant: str,
                                     near_text: str = None,
                                     limit: int = 3):
    query_params = QueryParams(class_name=class_name, limit=limit, near_text=near_text, tenant=tenant)
    return await weaviateTemplate.object_api(ObjectOperation.LIST_OBJECT_TENANT, query_params)


@object_tenant_router.delete("/clean")
async def delete_all(class_name: str, tenant: str):
    return await weaviateTemplate.delete_all_objects_tenant(class_name=class_name, tenant=tenant)

