from enum import Enum
from weaviate import Client


class SchemaOperation(Enum):
    GET_CLASS = "GET_CLASS"
    GET_CLASS_BY_NAME = "GET_CLASS_BY_NAME"
    CREATE_CLASS = "CREATE_CLASS"
    DELETE_CLASS = "DELETE_CLASS"
    UPDATE_CLASS = "UPDATE_CLASS"
    ADD_PROPER = "ADD_PROPER"


async def schema_api(weaviate_client: Client,
                     operation: SchemaOperation,
                     class_name: str,
                     payload: dict) -> dict:
    if operation == SchemaOperation.GET_CLASS:
        return weaviate_client.schema.get()
    elif operation == SchemaOperation.GET_CLASS_BY_NAME:
        if class_name is None:
            raise Exception("Searching schema is failed, The name can not be None")
        else:
            return weaviate_client.schema.get(class_name)
    elif operation == SchemaOperation.CREATE_CLASS:
        if payload is None:
            raise Exception("Creation schema is failed, the payload can not be None")
        else:
            return weaviate_client.schema.create(payload)
    elif operation == SchemaOperation.DELETE_CLASS:
        if payload is None:
            raise Exception("Deleting schema is failed, the payload can not be None")
        else:
            return weaviate_client.schema.delete_class(class_name)
    elif operation == SchemaOperation.UPDATE_CLASS:
        if payload is None or class_name is None:
            raise Exception("Updating class is failed, the payload or class name can not be None")
        else:
            return weaviate_client.schema.update_config(class_name, payload)
    elif operation == SchemaOperation.ADD_PROPER:
        if payload is None or class_name is None:
            raise Exception("Updating properties is failed, the payload or class name can not be None")
        else:
            return weaviate_client.schema.property.create(class_name, payload)
