from typing import Any, Type, TypeVar

from pydantic import BaseModel, ConfigDict

ExtendsBaseModelV1 = TypeVar("ExtendsBaseModelV1", bound="BaseModelV1")


class BaseModelV1(BaseModel):
    """
    Base pydantic model from which all other domain models should inherit.
    """

    model_config = ConfigDict(from_attributes=True)

    def dict_serialized(self, *args, **kwargs) -> dict:
        """
        Returns a dictionary representation of the model instance.
        """
        return super().model_dump(*args, **kwargs)

    @classmethod
    def from_orm(cls: Type["ExtendsBaseModelV1"], obj: Any) -> "ExtendsBaseModelV1":
        """
        Creates a model instance from an ORM object.
        """
        return cls.model_validate(obj)

    @classmethod
    def parse_obj(cls: Type["ExtendsBaseModelV1"], obj: Any) -> "ExtendsBaseModelV1":
        """
        Creates a model instance from a dictionary.
        """
        return cls.model_validate(obj)
