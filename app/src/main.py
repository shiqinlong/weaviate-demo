import uvicorn
from fastapi import FastAPI
from services.schema.router import schema_api
from services.tenant.router import tenant_api

path_prefix = "/api/v1"


def get_app() -> FastAPI:
    app: FastAPI = FastAPI()
    app.include_router(schema_api, prefix=path_prefix + "/schema", tags=["SCHEMA"])
    app.include_router(tenant_api, prefix=path_prefix + "/tenant", tags=["TENANT"])
    return app


if __name__ == '__main__':
    uvicorn.run(app="main:get_app", reload=True)
