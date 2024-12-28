from typing import Literal, Union

from monggregate.base import Expression
from monggregate.stages.stage import Stage
from pydantic import Field


class Merge(Stage):
    into: str
    on: Union[str, list[str]] = "_id"
    let: dict = Field(default_factory=lambda: {"new": "$ROOT"})
    when_matched: Literal["merge", "replace", "keepExisting", "fail"] | list[dict] = "merge"
    when_not_matched: Literal["insert", "discard", "fail"] = "insert"

    @property
    def expression(self) -> Expression:
        """Generate statement from arguments"""
        statement = {
            "$merge": {
                "into": self.into,
                "on": self.on,
                "whenMatched": self.when_matched,
                "whenNotMatched": self.when_not_matched,
            }
        }
        if self.let and isinstance(self.when_matched, list):
            statement["$merge"]["let"] = self.let
        return self.express(statement)
