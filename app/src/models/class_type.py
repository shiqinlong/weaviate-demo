from enum import Enum


class ClassType(Enum):
    INVOICE = "invoice"
    CONTRACT = "contract"


def isSupportClassType(class_type: str) -> bool:
    for classType in ClassType:
        if class_type == classType.value:
            return True
    return False
