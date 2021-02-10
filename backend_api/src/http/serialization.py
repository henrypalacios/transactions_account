from typing import TypeVar
from flask import make_response, abort, jsonify, Request
from marshmallow import exceptions, Schema
from marshmallow import fields
from marshmallow_dataclass import class_schema

from src.foundation import get_money, Money
from src.account import TypeTransaction

class Currencies(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):  # type: ignore
        return float(value.amount)

    def _deserialize(self, value, attr, data, **kwargs):  # type: ignore
        try:
            return get_money(value)
        except ValueError as exc:
            raise exceptions.ValidationError(str(exc))

class TypeField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):  # type: ignore
        return value.value

    def _deserialize(self, value, attr, data, **kwargs):  # type: ignore
        try:
            return getattr(TypeTransaction, value.upper())
        except ValueError as exc:
            raise exceptions.ValidationError(str(exc))


class BaseSchema(Schema):
    TYPE_MAPPING = {Money: Currencies, TypeTransaction: TypeField}


DataTransferObjectPattern = TypeVar("DataTransferObjectPattern")

def get_dto(data_json: dict, data_to_cls, context:dict={}) -> "DataTransferObjectPattern":
    schema_cls = class_schema(data_to_cls, base_schema=BaseSchema)
    schema = schema_cls()

    try:
        loaded = schema.load(dict(context, **data_json))

        return loaded
    except exceptions.ValidationError as exc:
        abort(make_response(jsonify(exc.messages), 400))


def get_outDto(data: dict, data_to_cls, many:bool=False, context:dict={}) -> "DataTransferObjectPattern":
    schema_cls = class_schema(data_to_cls, base_schema=BaseSchema)
    schema = schema_cls()

    try:
        loaded = schema.dump(data, many=many)

        return loaded
    except exceptions.ValidationError as exc:
        abort(make_response(jsonify(exc.messages), 400))
