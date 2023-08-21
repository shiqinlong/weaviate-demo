from fastapi import HTTPException
from services.weaviate.weaviate_template import WeaviateTemplate
from services.weaviate.schema_operation import isSchemaExists
from services.weaviate.tenant_operation import TenantOperation, tenant_call

weaviateTemplate = WeaviateTemplate()


async def validation_info(class_name: str, tenant_name: str) -> bool:
    weaviate_client = weaviateTemplate.get_weaviate_client()

    if not await isSchemaExists(weaviate_client=weaviate_client, class_name=class_name):
        return False

    tenant_list = await tenant_call(weaviate_client=weaviate_client, operation=TenantOperation.LIST_TENANTS,
                                    class_name=class_name)
    if tenant_list is None or len(tenant_list) == 0:
        return False
    else:
        for tenant in tenant_list:
            if tenant_name == tenant.name:
                return True
    return False
