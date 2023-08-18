from enum import Enum
from weaviate import Client


class TenantOperation(Enum):
    ADD_TENANTS = "ADD_TENANTS"
    LIST_TENANTS = "LIST_TENANT"
    DELETE_TENANTS = "DELETE_TENANTS"
    UPDATE_TENANTS = "UPDATE_TENANTS"


async def tenant_api(weaviate_client: Client, operation: TenantOperation, class_name: str, payload: dict):
    if operation == TenantOperation.LIST_TENANTS:
        if class_name is None:
            raise Exception("Can not list tenants without class name.")
        else:
            return weaviate_client.schema.get_class_tenants(class_name=class_name)
    if operation == TenantOperation.ADD_TENANTS:
        if class_name is None or payload is None:
            raise Exception("Can not add new tenants without class name or tenant info.")
        else:
            return weaviate_client.schema.add_class_tenants(class_name=class_name,tenants=payload)
    if operation == TenantOperation.DELETE_TENANTS:
        if class_name is None or payload is None:
            raise Exception("Can not delete tenants with out class name.")
        else:
            return weaviate_client.schema.remove_class_tenants(class_name=class_name,tenants=payload)
    # if operation == TenantOperation.UPDATE_TENANTS:
    #     if class_name is None or payload is None:
    #         raise Exception("Can not update tenants with out class name.")
    #     else:
    #         return weaviate_client.schema
