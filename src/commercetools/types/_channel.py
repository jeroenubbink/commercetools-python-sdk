# DO NOT EDIT! This file is automatically generated

import datetime
import enum
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import (
    BaseResource,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from ._common import Address, CreatedBy, GeoJson, LastModifiedBy, LocalizedString
    from ._review import ReviewRatingStatistics
    from ._type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )
__all__ = [
    "Channel",
    "ChannelAddRolesAction",
    "ChannelChangeDescriptionAction",
    "ChannelChangeKeyAction",
    "ChannelChangeNameAction",
    "ChannelDraft",
    "ChannelPagedQueryResponse",
    "ChannelReference",
    "ChannelRemoveRolesAction",
    "ChannelResourceIdentifier",
    "ChannelRoleEnum",
    "ChannelSetAddressAction",
    "ChannelSetCustomFieldAction",
    "ChannelSetCustomTypeAction",
    "ChannelSetGeoLocationAction",
    "ChannelSetRolesAction",
    "ChannelUpdate",
    "ChannelUpdateAction",
]


class Channel(BaseResource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ChannelSchema`."
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
    #: :class:`str`
    key: str
    #: List of :class:`commercetools.types.ChannelRoleEnum`
    roles: typing.List["ChannelRoleEnum"]
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.Address`
    address: typing.Optional["Address"]
    #: Optional :class:`commercetools.types.ReviewRatingStatistics` `(Named` ``reviewRatingStatistics`` `in Commercetools)`
    review_rating_statistics: typing.Optional["ReviewRatingStatistics"]
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]
    #: Optional :class:`commercetools.types.GeoJson` `(Named` ``geoLocation`` `in Commercetools)`
    geo_location: typing.Optional["GeoJson"]

    def __init__(
        self,
        *,
        id: str = None,
        version: int = None,
        created_at: datetime.datetime = None,
        last_modified_at: datetime.datetime = None,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: str = None,
        roles: typing.List["ChannelRoleEnum"] = None,
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        address: typing.Optional["Address"] = None,
        review_rating_statistics: typing.Optional["ReviewRatingStatistics"] = None,
        custom: typing.Optional["CustomFields"] = None,
        geo_location: typing.Optional["GeoJson"] = None
    ) -> None:
        self.id = id
        self.version = version
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.roles = roles
        self.name = name
        self.description = description
        self.address = address
        self.review_rating_statistics = review_rating_statistics
        self.custom = custom
        self.geo_location = geo_location
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    def __repr__(self) -> str:
        return (
            "Channel(id=%r, version=%r, created_at=%r, last_modified_at=%r, last_modified_by=%r, created_by=%r, key=%r, roles=%r, name=%r, description=%r, address=%r, review_rating_statistics=%r, custom=%r, geo_location=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.last_modified_by,
                self.created_by,
                self.key,
                self.roles,
                self.name,
                self.description,
                self.address,
                self.review_rating_statistics,
                self.custom,
                self.geo_location,
            )
        )


class ChannelDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ChannelDraftSchema`."
    #: :class:`str`
    key: str
    #: Optional list of :class:`commercetools.types.ChannelRoleEnum`
    roles: typing.Optional[typing.List["ChannelRoleEnum"]]
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.Address`
    address: typing.Optional["Address"]
    #: Optional :class:`commercetools.types.CustomFieldsDraft`
    custom: typing.Optional["CustomFieldsDraft"]
    #: Optional :class:`commercetools.types.GeoJson` `(Named` ``geoLocation`` `in Commercetools)`
    geo_location: typing.Optional["GeoJson"]

    def __init__(
        self,
        *,
        key: str = None,
        roles: typing.Optional[typing.List["ChannelRoleEnum"]] = None,
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        address: typing.Optional["Address"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        geo_location: typing.Optional["GeoJson"] = None
    ) -> None:
        self.key = key
        self.roles = roles
        self.name = name
        self.description = description
        self.address = address
        self.custom = custom
        self.geo_location = geo_location
        super().__init__()

    def __repr__(self) -> str:
        return (
            "ChannelDraft(key=%r, roles=%r, name=%r, description=%r, address=%r, custom=%r, geo_location=%r)"
            % (
                self.key,
                self.roles,
                self.name,
                self.description,
                self.address,
                self.custom,
                self.geo_location,
            )
        )


class ChannelPagedQueryResponse(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ChannelPagedQueryResponseSchema`."
    #: :class:`int`
    limit: int
    #: :class:`int`
    count: int
    #: Optional :class:`int`
    total: typing.Optional[int]
    #: :class:`int`
    offset: int
    #: List of :class:`commercetools.types.Channel`
    results: typing.Sequence["Channel"]

    def __init__(
        self,
        *,
        limit: int = None,
        count: int = None,
        total: typing.Optional[int] = None,
        offset: int = None,
        results: typing.Sequence["Channel"] = None
    ) -> None:
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    def __repr__(self) -> str:
        return (
            "ChannelPagedQueryResponse(limit=%r, count=%r, total=%r, offset=%r, results=%r)"
            % (self.limit, self.count, self.total, self.offset, self.results)
        )


class ChannelReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ChannelReferenceSchema`."
    #: Optional :class:`commercetools.types.Channel`
    obj: typing.Optional["Channel"]

    def __init__(
        self,
        *,
        type_id: "ReferenceTypeId" = None,
        id: str = None,
        obj: typing.Optional["Channel"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.CHANNEL, id=id)

    def __repr__(self) -> str:
        return "ChannelReference(type_id=%r, id=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.obj,
        )


class ChannelResourceIdentifier(ResourceIdentifier):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ChannelResourceIdentifierSchema`."

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None
    ) -> None:
        super().__init__(type_id=ReferenceTypeId.CHANNEL, id=id, key=key)

    def __repr__(self) -> str:
        return "ChannelResourceIdentifier(type_id=%r, id=%r, key=%r)" % (
            self.type_id,
            self.id,
            self.key,
        )


class ChannelRoleEnum(enum.Enum):
    INVENTORY_SUPPLY = "InventorySupply"
    PRODUCT_DISTRIBUTION = "ProductDistribution"
    ORDER_EXPORT = "OrderExport"
    ORDER_IMPORT = "OrderImport"
    PRIMARY = "Primary"


class ChannelUpdate(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ChannelUpdateSchema`."
    #: :class:`int`
    version: int
    #: :class:`list`
    actions: list

    def __init__(self, *, version: int = None, actions: list = None) -> None:
        self.version = version
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        return "ChannelUpdate(version=%r, actions=%r)" % (self.version, self.actions)


class ChannelUpdateAction(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ChannelUpdateActionSchema`."
    #: :class:`str`
    action: str

    def __init__(self, *, action: str = None) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "ChannelUpdateAction(action=%r)" % (self.action,)


class ChannelAddRolesAction(ChannelUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ChannelAddRolesActionSchema`."
    #: List of :class:`commercetools.types.ChannelRoleEnum`
    roles: typing.List["ChannelRoleEnum"]

    def __init__(
        self, *, action: str = None, roles: typing.List["ChannelRoleEnum"] = None
    ) -> None:
        self.roles = roles
        super().__init__(action="addRoles")

    def __repr__(self) -> str:
        return "ChannelAddRolesAction(action=%r, roles=%r)" % (self.action, self.roles)


class ChannelChangeDescriptionAction(ChannelUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ChannelChangeDescriptionActionSchema`."
    #: :class:`commercetools.types.LocalizedString`
    description: "LocalizedString"

    def __init__(
        self, *, action: str = None, description: "LocalizedString" = None
    ) -> None:
        self.description = description
        super().__init__(action="changeDescription")

    def __repr__(self) -> str:
        return "ChannelChangeDescriptionAction(action=%r, description=%r)" % (
            self.action,
            self.description,
        )


class ChannelChangeKeyAction(ChannelUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ChannelChangeKeyActionSchema`."
    #: :class:`str`
    key: str

    def __init__(self, *, action: str = None, key: str = None) -> None:
        self.key = key
        super().__init__(action="changeKey")

    def __repr__(self) -> str:
        return "ChannelChangeKeyAction(action=%r, key=%r)" % (self.action, self.key)


class ChannelChangeNameAction(ChannelUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ChannelChangeNameActionSchema`."
    #: :class:`commercetools.types.LocalizedString`
    name: "LocalizedString"

    def __init__(self, *, action: str = None, name: "LocalizedString" = None) -> None:
        self.name = name
        super().__init__(action="changeName")

    def __repr__(self) -> str:
        return "ChannelChangeNameAction(action=%r, name=%r)" % (self.action, self.name)


class ChannelRemoveRolesAction(ChannelUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ChannelRemoveRolesActionSchema`."
    #: List of :class:`commercetools.types.ChannelRoleEnum`
    roles: typing.List["ChannelRoleEnum"]

    def __init__(
        self, *, action: str = None, roles: typing.List["ChannelRoleEnum"] = None
    ) -> None:
        self.roles = roles
        super().__init__(action="removeRoles")

    def __repr__(self) -> str:
        return "ChannelRemoveRolesAction(action=%r, roles=%r)" % (
            self.action,
            self.roles,
        )


class ChannelSetAddressAction(ChannelUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ChannelSetAddressActionSchema`."
    #: Optional :class:`commercetools.types.Address`
    address: typing.Optional["Address"]

    def __init__(
        self, *, action: str = None, address: typing.Optional["Address"] = None
    ) -> None:
        self.address = address
        super().__init__(action="setAddress")

    def __repr__(self) -> str:
        return "ChannelSetAddressAction(action=%r, address=%r)" % (
            self.action,
            self.address,
        )


class ChannelSetCustomFieldAction(ChannelUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ChannelSetCustomFieldActionSchema`."
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
        return "ChannelSetCustomFieldAction(action=%r, name=%r, value=%r)" % (
            self.action,
            self.name,
            self.value,
        )


class ChannelSetCustomTypeAction(ChannelUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ChannelSetCustomTypeActionSchema`."
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
        return "ChannelSetCustomTypeAction(action=%r, type=%r, fields=%r)" % (
            self.action,
            self.type,
            self.fields,
        )


class ChannelSetGeoLocationAction(ChannelUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ChannelSetGeoLocationActionSchema`."
    #: Optional :class:`commercetools.types.GeoJson` `(Named` ``geoLocation`` `in Commercetools)`
    geo_location: typing.Optional["GeoJson"]

    def __init__(
        self, *, action: str = None, geo_location: typing.Optional["GeoJson"] = None
    ) -> None:
        self.geo_location = geo_location
        super().__init__(action="setGeoLocation")

    def __repr__(self) -> str:
        return "ChannelSetGeoLocationAction(action=%r, geo_location=%r)" % (
            self.action,
            self.geo_location,
        )


class ChannelSetRolesAction(ChannelUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ChannelSetRolesActionSchema`."
    #: List of :class:`commercetools.types.ChannelRoleEnum`
    roles: typing.List["ChannelRoleEnum"]

    def __init__(
        self, *, action: str = None, roles: typing.List["ChannelRoleEnum"] = None
    ) -> None:
        self.roles = roles
        super().__init__(action="setRoles")

    def __repr__(self) -> str:
        return "ChannelSetRolesAction(action=%r, roles=%r)" % (self.action, self.roles)
