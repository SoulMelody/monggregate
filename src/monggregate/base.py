"""
Module defining the base classes of the package.

All the classes of the package inherit from one of the classes defined in this module.
"""

# Standard Library imports
# ----------------------------
from abc import ABC, abstractmethod
from typing import Any, TypeGuard

# 3rd Party imports
# ---------------------------
import pydantic as pyd
from humps.main import camelize
from typing_extensions import Self


class Singleton:
    """Singleton metaclass"""

    _instance = None

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


Expression = dict[str, Any]


class BaseModel(pyd.BaseModel, ABC):
    """Mongreggate base class"""

    def to_expression(self) -> Expression | list[Expression]:
        """Converts an instance of a class inheriting from BaseModel to an expression"""

        return self.express(self)

    @classmethod
    def express(cls, obj: Any) -> Expression | list[Expression]:
        """Resolves an expression encapsulated in an object from a class inheriting from BaseModel"""

        return express(obj)

    @property
    @abstractmethod
    def expression(self) -> Expression:
        """Stage statement absctract method"""

        # this is a lazy attribute
        # what is currently in generate statement should go in here

    def __call__(self) -> Expression | list[Expression]:
        """Makes an instance of any class inheriting from this class callable"""

        return self.to_expression()

    model_config = pyd.ConfigDict(
        populate_by_name=True,
        alias_generator=camelize,
    )


def isbasemodel(instance: Any) -> TypeGuard[BaseModel]:
    """Returns true if instance is an instance of BaseModel"""

    return isinstance(instance, BaseModel)


def express(obj: Any) -> dict | list[dict]:
    """Resolves an expression encapsulated in an object from a class inheriting from BaseModel"""

    if isbasemodel(obj):
        output: dict | list = obj.expression
    elif isinstance(obj, list) and any(map(isbasemodel, obj)):
        output = []
        for element in obj:
            if isinstance(element, BaseModel):
                output.append(element.expression)
            else:
                output.append(element)
    elif isinstance(obj, dict):
        output = {}
        for key, value in obj.items():
            if isinstance(value, BaseModel):
                output[key] = value.expression
            else:
                output[key] = express(value)
    else:
        output = obj

    return output
