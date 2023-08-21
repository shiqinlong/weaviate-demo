from typing import Any

from fastapi import APIRouter, HTTPException
from models.object_payload import ObjectBatchCreatePayload, ObjectBatchDeletePayload
from services.weaviate.weaviate_template import WeaviateTemplate
from services.weaviate.batch_operation import BatchOperation
from services.batch.batch_services import validation_info

batch_router = APIRouter()
weaviateTemplate = WeaviateTemplate()


@batch_router.post("/{class_name}/{tenant}")
async def batch_create(class_name: str, tenant: str, payload: list[dict[str, Any]]):
    if await validation_info(class_name=class_name, tenant_name=tenant):
        payload = ObjectBatchCreatePayload(class_name=class_name, tenant=tenant, data_objects=payload)
        return await weaviateTemplate.batch_api(BatchOperation.BATCH_CREATE, payload)
    else:
        raise HTTPException(404, "Class {} or tenant {} does not exists.".format(class_name, tenant))
