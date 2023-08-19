from enum import Enum
from typing import Union

from weaviate import Client
from models.object_payload import ObjectBatchCreatePayload, ObjectBatchDeletePayload
from config.constants import WEAVIATE_BATCH_SIZE, WEAVIATE_BATCH_DYNAMIC, WEAVIATE_BATCH_TIMEOUT_RETRIES
from config.config import weaviate_config


class BatchOperation(Enum):
    BATCH_CREATE = "BATCH_CREATE"
    BATCH_DELETE = "BATCH_DELETE"


async def batch_call(weaviate_client: Client, operation: BatchOperation,
                     payload: Union[ObjectBatchCreatePayload, ObjectBatchDeletePayload]) -> str:

    if operation == BatchOperation.BATCH_CREATE and type(payload) == ObjectBatchCreatePayload:
        batch_size = weaviate_config[WEAVIATE_BATCH_SIZE]
        batch_dynamic = bool(weaviate_config[WEAVIATE_BATCH_DYNAMIC])
        batch_timeout_retries = int(weaviate_config[WEAVIATE_BATCH_TIMEOUT_RETRIES])

        weaviate_client.batch.configure(batch_size=batch_size, batch_dynamic=batch_dynamic,
                                        batch_timeout_retries=batch_timeout_retries)
        class_name = payload.class_name
        tenant = payload.tenant
        data_object_list = payload.data_objects

        final_count: int = 0
        with weaviate_client.batch() as batch:
            for data_object in data_object_list:
                uuid = batch.add_data_object(data_object=data_object, class_name=class_name, tenant=tenant)
                if uuid is not None:
                    ++final_count

        return "Batch create data for class_name: {} , tenant : {} successfully, " \
               "result count: {}".format(class_name, tenant, final_count)
    elif payload == BatchOperation.BATCH_DELETE and type(payload) == ObjectBatchDeletePayload:
        pass
    else:
        raise Exception("Operation method or payload typing is incorrect!")
