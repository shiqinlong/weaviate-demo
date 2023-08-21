from typing import Tuple, Union

import weaviate
from weaviate import Client
from config.config import weaviate_config
from services.common.util_tools import singletonType
from config.constants import WEAVIATE_BASE_URL, WEAVIATE_API_KEY, WEAVIATE_CONNECTION_TIMEOUT, WEAVIATE_READ_TIMEOUT, \
    WEAVIATE_BATCH_SIZE, WEAVIATE_BATCH_DYNAMIC, WEAVIATE_BATCH_TIMEOUT_RETRIES
from pydantic import BaseModel
from services.weaviate.schema_operation import SchemaOperation, schema_call
from services.weaviate.tenant_operation import TenantOperation, tenant_call
from services.weaviate.object_operation import ObjectOperation, object_call, object_call_list, object_call_create
from services.weaviate.batch_operation import BatchOperation, batch_call
from models.query_params import QueryParams
from models.object_payload import ObjectPayload, ObjectBatchCreatePayload, ObjectBatchDeletePayload


@singletonType
class WeaviateTemplate(BaseModel):

    def __init__(self):
        super().__init__()
        self.__weaviate_client = self.__build_weaviate_client()

    def get_weaviate_client(self):
        return self.__weaviate_client

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

        batch_size = int(weaviate_config[WEAVIATE_BATCH_SIZE])
        batch_dynamic = bool(weaviate_config[WEAVIATE_BATCH_DYNAMIC])
        batch_timeout_retries = int(weaviate_config[WEAVIATE_BATCH_TIMEOUT_RETRIES])

        weaviate_client.batch.configure(batch_size=batch_size, dynamic=batch_dynamic,
                                        timeout_retries=batch_timeout_retries)

        return weaviate_client

    async def class_api(self, operation: SchemaOperation,
                        class_name: str = None,
                        payload: dict = None) -> dict:
        if operation is None:
            raise Exception("operation can not be empty.")
        return await schema_call(weaviate_client=self.__weaviate_client, operation=operation, class_name=class_name,
                                 payload=payload)

    async def tenant_api(self, operation: TenantOperation, class_name: str = None, payload: list[str] = None):
        if operation is None:
            raise Exception("operation can not be empty.")
        return await tenant_call(weaviate_client=self.__weaviate_client, operation=operation, class_name=class_name,
                                 payload=payload)

    async def object_api(self, operation: ObjectOperation, queryParams: QueryParams):
        if operation is None:
            raise Exception("operation can not be empty.")
        return await object_call(weaviate_client=self.__weaviate_client, operation=operation, queryParams=queryParams)

    async def object_api_create(self, object_payload: ObjectPayload):
        return await object_call_create(weaviate_client=self.__weaviate_client, object_payload=object_payload)

    async def object_api_list(self, class_name: str, tenant: str, limit: int = None, offset: int = None):

        return await object_call_list(self.__weaviate_client, class_name, tenant, limit, offset)

    async def batch_api(self, operation: BatchOperation,
                        payload: Union[ObjectBatchCreatePayload, ObjectBatchDeletePayload]):
        return await batch_call(self.__weaviate_client, operation, payload)

# def testfun(name:str,age:int,addr:str):
#     print(f"{name},{age},{addr}")
#
#
# if __name__ == '__main__':
#     testfun(name="shi", age=12, addr="test")
#     print(f"test")
