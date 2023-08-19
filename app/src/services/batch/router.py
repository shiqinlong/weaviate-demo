from typing import Any

from fastapi import APIRouter
from models.object_payload import ObjectBatchCreatePayload, ObjectBatchDeletePayload
from services.weaviate.weaviate_template import WeaviateTemplate
from services.weaviate.batch_operation import BatchOperation

batch_router = APIRouter()
weaviateTemplate = WeaviateTemplate()


@batch_router.post("/{class_name}/{tenant}")
async def batch_create(class_name: str, tenant: str, payload: list[dict[str, Any]]):
    payload = ObjectBatchDeletePayload(class_name=class_name, tenant=tenant, data_objects=payload)
    return await weaviateTemplate.batch_api(BatchOperation.BATCH_CREATE, payload)
