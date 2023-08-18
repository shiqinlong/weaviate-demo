import weaviate
from config.config import weaviate_config
from config.constants import WEAVIATE_BASE_URL, WEAVIATE_API_KEY
from pydantic import BaseModel
from enum import Enum


class SchemaOperation(Enum):
    GET_CLASS = "GET_CLASS"
    GET_CLASS_BY_NAME = "GET_CLASS_BY_NAME"
    CREATE_CLASS = "CREATE_CLASS"
    DELETE_CLASS = "DELETE_CLASS"
    UPDATE_CLASS = "UPDATE_CLASS"
    ADD_PROPER = "ADD_PROPER"


class TenantOperation(Enum):
    ADD_TENANTS = "ADD_TENANTS"
    LIST_TENANTS = "LIST_TENANT"
    DELETE_TENANTS = "DELETE_TENANTS"


class WeaviateTemplate(BaseModel):

    def __build_weaviate_client(self):
        __base_url = weaviate_config[WEAVIATE_BASE_URL]
        __api_key = weaviate_config[WEAVIATE_API_KEY]

        auth_config = weaviate.AuthApiKey(api_key=__api_key)
        weaviate_client = weaviate.Client(
            url=__base_url,
            auth_client_secret=auth_config)
        return weaviate_client

    async def class_api(self, operation: SchemaOperation,
                        class_name: str = None,
                        payload: str = None) -> dict:

        client = self.__build_weaviate_client()
        if operation.name == SchemaOperation.GET_CLASS.value:
            return client.schema.get()
        elif operation.name == SchemaOperation.GET_CLASS_BY_NAME.name:
            if class_name is None:
                raise Exception("Searching schema is failed, The name can not be None")
            else:
                return client.schema.get(class_name)
        elif operation.name == SchemaOperation.CREATE_CLASS.name:
            if payload is None:
                raise Exception("Creation schema is failed, the payload can not be None")
            else:
                return client.schema.create(payload)
        elif operation.name == SchemaOperation.UPDATE_CLASS.name:
            if payload is None or class_name is None:
                raise Exception("Updating class is failed, the payload or class name can not be None")
            else:
                return client.schema.update_config(class_name, payload)
        elif operation.name == SchemaOperation.ADD_PROPER.name:
            if payload is None or class_name is None:
                raise Exception("Updating properties is failed, the payload or class name can not be None")
            else:
                return client.schema.property.create(class_name, payload)


if __name__ == '__main__':
    print(f"test")
