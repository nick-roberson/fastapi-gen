import pytest

from builder.models.configs import (DatabaseConfig, FieldDefinition,
                                    ModelConfig, ServiceConfig)
from builder.models.enum import FieldDataType


def test_validate_db_type():
    # Invalid
    with pytest.raises(ValueError):
        DatabaseConfig(db_type="alembic", db_uri_env_var="DB_URI")
    # Valid
    DatabaseConfig(db_type="mongo", db_uri_env_var="DB_URI")


def test_model_config():
    # Test simple
    model = ModelConfig(name="User", fields=[FieldDefinition(name="name", type="str")])
    assert model.model_id_var_name == "user_id"
    assert model.manager_name == "UserManager"
    assert model.manager_var_name == "user_manager"


def test_model_config_validate_type():
    # Invalid
    with pytest.raises(ValueError):
        ModelConfig(name="User", fields=[FieldDefinition(name="name", type="string")])
    # Valid
    for choice in FieldDataType:
        ModelConfig(
            name="User", fields=[FieldDefinition(name="name", type=choice.value)]
        )


def test_model_config_validate_default():
    # Invalid
    with pytest.raises(ValueError):
        config = ModelConfig(
            name="User",
            fields=[FieldDefinition(name="name", type="int", default="test")],
        )

    # Valid String
    fd = FieldDefinition(name="name", type="str", default="test")
    assert fd.default == "test"

    # Valid Int
    fd = FieldDefinition(name="name", type="int", default="1")
    assert fd.default == 1
    fd = FieldDefinition(name="name", type="int", default=1)
    assert fd.default == 1

    # Valid Float
    fd = FieldDefinition(name="name", type="float", default="1.0")
    assert fd.default == 1.0
    fd = FieldDefinition(name="name", type="float", default=1.0)
    assert fd.default == 1.0

    # Valid Bool
    fd = FieldDefinition(name="name", type="bool", default="true")
    assert fd.default == True
    fd = FieldDefinition(name="name", type="bool", default=True)
    assert fd.default == True
    fd = FieldDefinition(name="name", type="bool", default="false")
    assert fd.default == False
    fd = FieldDefinition(name="name", type="bool", default=False)
    assert fd.default == False

    # Valid List
    fd = FieldDefinition(name="name", type="list", default=[])
    assert fd.default == []
    fd = FieldDefinition(name="name", type="list", default=[1, 2, 3])
    assert fd.default == [1, 2, 3]

    # Valid Dict
    fd = FieldDefinition(name="name", type="dict", default={})
    assert fd.default == {}
    fd = FieldDefinition(name="name", type="dict", default={"key": "value"})
    assert fd.default == {"key": "value"}

    # Valid None
    fd = FieldDefinition(name="name", type="str", default=None)
    assert fd.default == None
    fd = FieldDefinition(name="name", type="int", default="None")
    assert fd.default == None
