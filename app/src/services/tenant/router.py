from fastapi import APIRouter

tenant_api = APIRouter()


@tenant_api.get("")
async def get_all_tenant():
    return "success"


@tenant_api.get("/{tenant_id}")
async def get_tenant_by_name(tenant_id: str):
    print(f"tenant id: {tenant_id}")
    return "tenant"