from enum import Enum
from typing import List

from weaviate import Client, Tenant


class TenantOperation(Enum):
    ADD_TENANTS = "ADD_TENANTS"
    LIST_TENANTS = "LIST_TENANT"
    DELETE_TENANTS = "DELETE_TENANTS"
    UPDATE_TENANTS = "UPDATE_TENANTS"


async def tenant_call(weaviate_client: Client, operation: TenantOperation, class_name: str, payload: List[str] = None):
    if operation == TenantOperation.LIST_TENANTS:
        tenants = weaviate_client.schema.get_class_tenants(class_name=class_name)
        tenant_josn_list = []
        for i, d in enumerate(tenants):
            tenant_josn_list.append(d.name)
        return tenant_josn_list

    if operation == TenantOperation.ADD_TENANTS:
        if class_name is None or payload is None:
            raise Exception("Can not add new tenants without class name or tenant info.")
        else:
            tenants = []
            for i, d in enumerate(payload):
                tenants.append(Tenant(name=d))
            return weaviate_client.schema.add_class_tenants(class_name=class_name, tenants=tenants)
    if operation == TenantOperation.DELETE_TENANTS:
        if class_name is None or payload is None:
            raise Exception("Can not delete tenants with out class name.")
        else:
            return weaviate_client.schema.remove_class_tenants(class_name=class_name, tenants=payload)

# async def isTenantEsit(weaviate_client:Client,class_name:str,tenant:str):
#     weaviate_client.schema.
