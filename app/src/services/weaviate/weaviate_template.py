from typing import Tuple, Union

import weaviate
from config.config import weaviate_config
from config.constants import WEAVIATE_BASE_URL, WEAVIATE_API_KEY, WEAVIATE_CONNECTION_TIMEOUT, WEAVIATE_READ_TIMEOUT
from pydantic import BaseModel
from services.weaviate.schema_operation import SchemaOperation, schema_call
from services.weaviate.tenant_operation import TenantOperation, tenant_call
from services.weaviate.object_operation import ObjectOperation, object_call, object_call_list, object_call_create
from services.weaviate.batch_operation import BatchOperation, batch_call
from models.query_params import QueryParams
from models.object_payload import ObjectPayload, ObjectBatchCreatePayload, ObjectBatchDeletePayload


class WeaviateTemplate(BaseModel):

    def __build_weaviate_client(self):
        __base_url = weaviate_config[WEAVIATE_BASE_URL]
        __api_key = weaviate_config[WEAVIATE_API_KEY]
        connection_timeout = int(weaviate_config[WEAVIATE_CONNECTION_TIMEOUT])
        read_timeout = int(weaviate_config[WEAVIATE_READ_TIMEOUT])

        timeout_config = (connection_timeout, read_timeout)
        auth_config = weaviate.AuthApiKey(api_key=__api_key)

        weaviate_client = weaviate.Client(
            url=__base_url,
            auth_client_secret=auth_config,
            timeout_config=timeout_config)
        return weaviate_client

    async def class_api(self, operation: SchemaOperation,
                        class_name: str = None,
                        payload: dict = None) -> dict:
        if operation is None:
            raise Exception("operation can not be empty.")
        client = self.__build_weaviate_client()
        return await schema_call(weaviate_client=client, operation=operation, class_name=class_name, payload=payload)

    async def tenant_api(self, operation: TenantOperation, class_name: str = None, payload: list[str] = None):
        if operation is None:
            raise Exception("operation can not be empty.")
        client = self.__build_weaviate_client()
        return await tenant_call(weaviate_client=client, operation=operation, class_name=class_name, payload=payload)

    async def object_api(self, operation: ObjectOperation, queryParams: QueryParams):
        if operation is None:
            raise Exception("operation can not be empty.")
        client = self.__build_weaviate_client()
        return await object_call(weaviate_client=client, operation=operation, queryParams=queryParams)

    async def object_api_create(self, object_payload: ObjectPayload):
        client = self.__build_weaviate_client()
        return await object_call_create(weaviate_client=client, object_payload=object_payload)

    async def object_api_list(self, class_name: str, tenant: str, limit: int = None, offset: int = None):
        client = self.__build_weaviate_client()
        return await object_call_list(client, class_name, tenant, limit, offset)

    async def batch_api(self, operation: BatchOperation,
                        payload: Union[ObjectBatchCreatePayload, ObjectBatchDeletePayload]):
        client = self.__build_weaviate_client()
        return await batch_call(client, operation, payload)

# def testfun(name:str,age:int,addr:str):
#     print(f"{name},{age},{addr}")
#
#
# if __name__ == '__main__':
#     testfun(name="shi", age=12, addr="test")
#     print(f"test")
