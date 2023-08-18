import uvicorn
from fastapi import FastAPI
from services.schema.router import schema_router
from services.tenant.router import tenant_router
from services.objects.router import object_router

path_prefix = "/api/v1"


def get_app() -> FastAPI:
    app: FastAPI = FastAPI()
    app.include_router(schema_router, prefix=path_prefix + "/schema", tags=["SCHEMA"])
    app.include_router(tenant_router, prefix=path_prefix + "/tenant", tags=["TENANT"])
    app.include_router(object_router, prefix=path_prefix + "/object", tags=["OBJECT"])
    return app


if __name__ == '__main__':
    uvicorn.run(app="main:get_app")


