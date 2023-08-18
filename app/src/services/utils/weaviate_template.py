import weaviate
from config.config import weaviate_config
from config.constants import WEAVIATE_BASE_URL, WEAVIATE_API_KEY
from pydantic import BaseModel
from services.utils.schema_operation import SchemaOperation, schema_api
from services.utils.tenant_operation import TenantOperation, tenant_api
from services.utils.object_operation import ObjectOperation, object_api
from models.query_params import QueryParams

from .tenant_operation import TenantOperation, tenant_api


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
                        payload: dict = None) -> dict:
        if operation is None:
            raise Exception("operation can not be empty.")
        client = self.__build_weaviate_client()
        return await schema_api(weaviate_client=client, operation=operation, class_name=class_name, payload=payload)

    async def tenant_api(self, operation: TenantOperation, class_name: str = None, payload: dict = None):
        if operation is None:
            raise Exception("operation can not be empty.")
        client = self.__build_weaviate_client()
        return await tenant_api(weaviate_client=client, operation=operation, class_name=class_name, payload=payload)

    async def object_api(self, operation: ObjectOperation, queryParams: QueryParams):
        if operation is None:
            raise Exception("operation can not be empty.")
        client = self.__build_weaviate_client()
        return await object_api(weaviate_client=client, operation=operation, queryParams=queryParams)


if __name__ == '__main__':
    print(f"test")
