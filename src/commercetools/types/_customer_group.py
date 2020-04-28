# DO NOT EDIT! This file is automatically generated

import datetime
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import (
    BaseResource,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from ._common import CreatedBy, LastModifiedBy
    from ._type import CustomFields, FieldContainer, TypeResourceIdentifier
__all__ = [
    "CustomerGroup",
    "CustomerGroupChangeNameAction",
    "CustomerGroupDraft",
    "CustomerGroupPagedQueryResponse",
    "CustomerGroupReference",
    "CustomerGroupResourceIdentifier",
    "CustomerGroupSetCustomFieldAction",
    "CustomerGroupSetCustomTypeAction",
    "CustomerGroupSetKeyAction",
    "CustomerGroupUpdate",
    "CustomerGroupUpdateAction",
]


class CustomerGroup(BaseResource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupSchema`."
    #: :class:`str`
    id: str
    #: :class:`int`
    version: int
    #: :class:`datetime.datetime` `(Named` ``createdAt`` `in Commercetools)`
    created_at: datetime.datetime
    #: :class:`datetime.datetime` `(Named` ``lastModifiedAt`` `in Commercetools)`
    last_modified_at: datetime.datetime
    #: Optional :class:`commercetools.types.LastModifiedBy` `(Named` ``lastModifiedBy`` `in Commercetools)`
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Optional :class:`commercetools.types.CreatedBy` `(Named` ``createdBy`` `in Commercetools)`
    created_by: typing.Optional["CreatedBy"]
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: :class:`str`
    name: str
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        id: str = None,
        version: int = None,
        created_at: datetime.datetime = None,
        last_modified_at: datetime.datetime = None,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: typing.Optional[str] = None,
        name: str = None,
        custom: typing.Optional["CustomFields"] = None
    ) -> None:
        self.id = id
        self.version = version
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.name = name
        self.custom = custom
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    def __repr__(self) -> str:
        return (
            "CustomerGroup(id=%r, version=%r, created_at=%r, last_modified_at=%r, last_modified_by=%r, created_by=%r, key=%r, name=%r, custom=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.last_modified_by,
                self.created_by,
                self.key,
                self.name,
                self.custom,
            )
        )


class CustomerGroupDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupDraftSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: :class:`str` `(Named` ``groupName`` `in Commercetools)`
    group_name: str
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        group_name: str = None,
        custom: typing.Optional["CustomFields"] = None
    ) -> None:
        self.key = key
        self.group_name = group_name
        self.custom = custom
        super().__init__()

    def __repr__(self) -> str:
        return "CustomerGroupDraft(key=%r, group_name=%r, custom=%r)" % (
            self.key,
            self.group_name,
            self.custom,
        )


class CustomerGroupPagedQueryResponse(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupPagedQueryResponseSchema`."
    #: :class:`int`
    limit: int
    #: :class:`int`
    count: int
    #: Optional :class:`int`
    total: typing.Optional[int]
    #: :class:`int`
    offset: int
    #: List of :class:`commercetools.types.CustomerGroup`
    results: typing.Sequence["CustomerGroup"]

    def __init__(
        self,
        *,
        limit: int = None,
        count: int = None,
        total: typing.Optional[int] = None,
        offset: int = None,
        results: typing.Sequence["CustomerGroup"] = None
    ) -> None:
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    def __repr__(self) -> str:
        return (
            "CustomerGroupPagedQueryResponse(limit=%r, count=%r, total=%r, offset=%r, results=%r)"
            % (self.limit, self.count, self.total, self.offset, self.results)
        )


class CustomerGroupReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupReferenceSchema`."
    #: Optional :class:`commercetools.types.CustomerGroup`
    obj: typing.Optional["CustomerGroup"]

    def __init__(
        self,
        *,
        type_id: "ReferenceTypeId" = None,
        id: str = None,
        obj: typing.Optional["CustomerGroup"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.CUSTOMER_GROUP, id=id)

    def __repr__(self) -> str:
        return "CustomerGroupReference(type_id=%r, id=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.obj,
        )


class CustomerGroupResourceIdentifier(ResourceIdentifier):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupResourceIdentifierSchema`."

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None
    ) -> None:
        super().__init__(type_id=ReferenceTypeId.CUSTOMER_GROUP, id=id, key=key)

    def __repr__(self) -> str:
        return "CustomerGroupResourceIdentifier(type_id=%r, id=%r, key=%r)" % (
            self.type_id,
            self.id,
            self.key,
        )


class CustomerGroupUpdate(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupUpdateSchema`."
    #: :class:`int`
    version: int
    #: :class:`list`
    actions: list

    def __init__(self, *, version: int = None, actions: list = None) -> None:
        self.version = version
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        return "CustomerGroupUpdate(version=%r, actions=%r)" % (
            self.version,
            self.actions,
        )


class CustomerGroupUpdateAction(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupUpdateActionSchema`."
    #: :class:`str`
    action: str

    def __init__(self, *, action: str = None) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "CustomerGroupUpdateAction(action=%r)" % (self.action,)


class CustomerGroupChangeNameAction(CustomerGroupUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupChangeNameActionSchema`."
    #: :class:`str`
    name: str

    def __init__(self, *, action: str = None, name: str = None) -> None:
        self.name = name
        super().__init__(action="changeName")

    def __repr__(self) -> str:
        return "CustomerGroupChangeNameAction(action=%r, name=%r)" % (
            self.action,
            self.name,
        )


class CustomerGroupSetCustomFieldAction(CustomerGroupUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupSetCustomFieldActionSchema`."
    #: :class:`str`
    name: str
    #: Optional :class:`typing.Any`
    value: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        action: str = None,
        name: str = None,
        value: typing.Optional[typing.Any] = None
    ) -> None:
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    def __repr__(self) -> str:
        return "CustomerGroupSetCustomFieldAction(action=%r, name=%r, value=%r)" % (
            self.action,
            self.name,
            self.value,
        )


class CustomerGroupSetCustomTypeAction(CustomerGroupUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupSetCustomTypeActionSchema`."
    #: Optional :class:`commercetools.types.TypeResourceIdentifier`
    type: typing.Optional["TypeResourceIdentifier"]
    #: Optional :class:`commercetools.types.FieldContainer`
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        action: str = None,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ) -> None:
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomType")

    def __repr__(self) -> str:
        return "CustomerGroupSetCustomTypeAction(action=%r, type=%r, fields=%r)" % (
            self.action,
            self.type,
            self.fields,
        )


class CustomerGroupSetKeyAction(CustomerGroupUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupSetKeyActionSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(self, *, action: str = None, key: typing.Optional[str] = None) -> None:
        self.key = key
        super().__init__(action="setKey")

    def __repr__(self) -> str:
        return "CustomerGroupSetKeyAction(action=%r, key=%r)" % (self.action, self.key)
