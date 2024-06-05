import enum


class DatabaseTypes(enum.Enum):
    """Database types"""

    POSTGRES: str = "postgres"
    MYSQL: str = "mysql"

    @classmethod
    def choices(cls):
        return [choice.value for choice in cls]


class FieldDataType(enum.Enum):
    """Field data types"""

    STRING: str = "str"
    INTEGER: str = "int"
    FLOAT: str = "float"
    BOOLEAN: str = "bool"
    LIST: str = "list"
    DICT: str = "dict"
    DATETIME: str = "datetime"

    @classmethod
    def choices(cls):
        return [choice.value for choice in cls]
