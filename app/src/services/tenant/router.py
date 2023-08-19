from fastapi import APIRouter
from services.weaviate.weaviate_template import WeaviateTemplate
from services.weaviate.tenant_operation import TenantOperation

tenant_router = APIRouter()
weaviateTemplate = WeaviateTemplate()


@tenant_router.get("/{class_name}")
async def get_all_tenant(class_name: str) -> list[str]:
    result = await weaviateTemplate.tenant_api(operation=TenantOperation.LIST_TENANTS, class_name=class_name)
    return result


@tenant_router.post("/{class_name}", summary="add new tenants to specific class by class name")
async def get_tenant_by_name(class_name: str, payload: list[str]):
    result = await weaviateTemplate.tenant_api(operation=TenantOperation.ADD_TENANTS, class_name=class_name,
                                               payload=payload)
    return result


@tenant_router.delete("/{class_name}", summary="delete tenants to specific class by class name")
async def delete_tenants(class_name: str, payload: list[str]):
    result = await weaviateTemplate.tenant_api(operation=TenantOperation.DELETE_TENANTS, class_name=class_name,
                                               payload=payload)
    return result
