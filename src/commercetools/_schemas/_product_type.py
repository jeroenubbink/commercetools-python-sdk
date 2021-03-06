# DO NOT EDIT! This file is automatically generated
import marshmallow
import marshmallow_enum

from commercetools import helpers, types
from commercetools._schemas._common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)

__all__ = [
    "AttributeBooleanTypeSchema",
    "AttributeDateTimeTypeSchema",
    "AttributeDateTypeSchema",
    "AttributeDefinitionDraftSchema",
    "AttributeDefinitionSchema",
    "AttributeEnumTypeSchema",
    "AttributeLocalizableTextTypeSchema",
    "AttributeLocalizedEnumTypeSchema",
    "AttributeLocalizedEnumValueSchema",
    "AttributeMoneyTypeSchema",
    "AttributeNestedTypeSchema",
    "AttributeNumberTypeSchema",
    "AttributePlainEnumValueSchema",
    "AttributeReferenceTypeSchema",
    "AttributeSetTypeSchema",
    "AttributeTextTypeSchema",
    "AttributeTimeTypeSchema",
    "AttributeTypeSchema",
    "ProductTypeAddAttributeDefinitionActionSchema",
    "ProductTypeAddLocalizedEnumValueActionSchema",
    "ProductTypeAddPlainEnumValueActionSchema",
    "ProductTypeChangeAttributeConstraintActionSchema",
    "ProductTypeChangeAttributeNameActionSchema",
    "ProductTypeChangeAttributeOrderActionSchema",
    "ProductTypeChangeAttributeOrderByNameActionSchema",
    "ProductTypeChangeDescriptionActionSchema",
    "ProductTypeChangeEnumKeyActionSchema",
    "ProductTypeChangeInputHintActionSchema",
    "ProductTypeChangeIsSearchableActionSchema",
    "ProductTypeChangeLabelActionSchema",
    "ProductTypeChangeLocalizedEnumValueLabelActionSchema",
    "ProductTypeChangeLocalizedEnumValueOrderActionSchema",
    "ProductTypeChangeNameActionSchema",
    "ProductTypeChangePlainEnumValueLabelActionSchema",
    "ProductTypeChangePlainEnumValueOrderActionSchema",
    "ProductTypeDraftSchema",
    "ProductTypePagedQueryResponseSchema",
    "ProductTypeReferenceSchema",
    "ProductTypeRemoveAttributeDefinitionActionSchema",
    "ProductTypeRemoveEnumValuesActionSchema",
    "ProductTypeResourceIdentifierSchema",
    "ProductTypeSchema",
    "ProductTypeSetInputTipActionSchema",
    "ProductTypeSetKeyActionSchema",
    "ProductTypeUpdateActionSchema",
    "ProductTypeUpdateSchema",
]


class AttributeDefinitionDraftSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.AttributeDefinitionDraft`."""

    type = helpers.Discriminator(
        discriminator_field=("name", "name"),
        discriminator_schemas={
            "boolean": "commercetools._schemas._product_type.AttributeBooleanTypeSchema",
            "datetime": "commercetools._schemas._product_type.AttributeDateTimeTypeSchema",
            "date": "commercetools._schemas._product_type.AttributeDateTypeSchema",
            "enum": "commercetools._schemas._product_type.AttributeEnumTypeSchema",
            "ltext": "commercetools._schemas._product_type.AttributeLocalizableTextTypeSchema",
            "lenum": "commercetools._schemas._product_type.AttributeLocalizedEnumTypeSchema",
            "money": "commercetools._schemas._product_type.AttributeMoneyTypeSchema",
            "nested": "commercetools._schemas._product_type.AttributeNestedTypeSchema",
            "number": "commercetools._schemas._product_type.AttributeNumberTypeSchema",
            "reference": "commercetools._schemas._product_type.AttributeReferenceTypeSchema",
            "set": "commercetools._schemas._product_type.AttributeSetTypeSchema",
            "text": "commercetools._schemas._product_type.AttributeTextTypeSchema",
            "time": "commercetools._schemas._product_type.AttributeTimeTypeSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    name = marshmallow.fields.String(allow_none=True)
    label = LocalizedStringField(allow_none=True)
    is_required = marshmallow.fields.Bool(allow_none=True, data_key="isRequired")
    attribute_constraint = marshmallow_enum.EnumField(
        types.AttributeConstraintEnum,
        by_value=True,
        missing=None,
        data_key="attributeConstraint",
    )
    input_tip = LocalizedStringField(allow_none=True, missing=None, data_key="inputTip")
    input_hint = marshmallow_enum.EnumField(
        types.TextInputHint, by_value=True, missing=None, data_key="inputHint"
    )
    is_searchable = marshmallow.fields.Bool(
        allow_none=True, missing=None, data_key="isSearchable"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.AttributeDefinitionDraft(**data)


class AttributeDefinitionSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.AttributeDefinition`."""

    type = helpers.Discriminator(
        discriminator_field=("name", "name"),
        discriminator_schemas={
            "boolean": "commercetools._schemas._product_type.AttributeBooleanTypeSchema",
            "datetime": "commercetools._schemas._product_type.AttributeDateTimeTypeSchema",
            "date": "commercetools._schemas._product_type.AttributeDateTypeSchema",
            "enum": "commercetools._schemas._product_type.AttributeEnumTypeSchema",
            "ltext": "commercetools._schemas._product_type.AttributeLocalizableTextTypeSchema",
            "lenum": "commercetools._schemas._product_type.AttributeLocalizedEnumTypeSchema",
            "money": "commercetools._schemas._product_type.AttributeMoneyTypeSchema",
            "nested": "commercetools._schemas._product_type.AttributeNestedTypeSchema",
            "number": "commercetools._schemas._product_type.AttributeNumberTypeSchema",
            "reference": "commercetools._schemas._product_type.AttributeReferenceTypeSchema",
            "set": "commercetools._schemas._product_type.AttributeSetTypeSchema",
            "text": "commercetools._schemas._product_type.AttributeTextTypeSchema",
            "time": "commercetools._schemas._product_type.AttributeTimeTypeSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    name = marshmallow.fields.String(allow_none=True)
    label = LocalizedStringField(allow_none=True)
    is_required = marshmallow.fields.Bool(allow_none=True, data_key="isRequired")
    attribute_constraint = marshmallow_enum.EnumField(
        types.AttributeConstraintEnum, by_value=True, data_key="attributeConstraint"
    )
    input_tip = LocalizedStringField(allow_none=True, missing=None, data_key="inputTip")
    input_hint = marshmallow_enum.EnumField(
        types.TextInputHint, by_value=True, data_key="inputHint"
    )
    is_searchable = marshmallow.fields.Bool(allow_none=True, data_key="isSearchable")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.AttributeDefinition(**data)


class AttributeLocalizedEnumValueSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.AttributeLocalizedEnumValue`."""

    key = marshmallow.fields.String(allow_none=True)
    label = LocalizedStringField(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.AttributeLocalizedEnumValue(**data)


class AttributePlainEnumValueSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.AttributePlainEnumValue`."""

    key = marshmallow.fields.String(allow_none=True)
    label = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.AttributePlainEnumValue(**data)


class AttributeTypeSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.AttributeType`."""

    name = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return types.AttributeType(**data)


class ProductTypeDraftSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeDraft`."""

    key = marshmallow.fields.String(allow_none=True, missing=None)
    name = marshmallow.fields.String(allow_none=True)
    description = marshmallow.fields.String(allow_none=True)
    attributes = helpers.LazyNestedField(
        nested="commercetools._schemas._product_type.AttributeDefinitionDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ProductTypeDraft(**data)


class ProductTypePagedQueryResponseSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypePagedQueryResponse`."""

    limit = marshmallow.fields.Integer(allow_none=True)
    count = marshmallow.fields.Integer(allow_none=True)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True)
    results = helpers.LazyNestedField(
        nested="commercetools._schemas._product_type.ProductTypeSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ProductTypePagedQueryResponse(**data)


class ProductTypeReferenceSchema(ReferenceSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeReference`."""

    obj = helpers.LazyNestedField(
        nested="commercetools._schemas._product_type.ProductTypeSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.ProductTypeReference(**data)


class ProductTypeResourceIdentifierSchema(ResourceIdentifierSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeResourceIdentifier`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.ProductTypeResourceIdentifier(**data)


class ProductTypeSchema(BaseResourceSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductType`."""

    id = marshmallow.fields.String(allow_none=True)
    version = marshmallow.fields.Integer(allow_none=True)
    created_at = marshmallow.fields.DateTime(allow_none=True, data_key="createdAt")
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, data_key="lastModifiedAt"
    )
    last_modified_by = helpers.LazyNestedField(
        nested="commercetools._schemas._common.LastModifiedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested="commercetools._schemas._common.CreatedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="createdBy",
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)
    name = marshmallow.fields.String(allow_none=True)
    description = marshmallow.fields.String(allow_none=True)
    attributes = helpers.LazyNestedField(
        nested="commercetools._schemas._product_type.AttributeDefinitionSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ProductType(**data)


class ProductTypeUpdateActionSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeUpdateAction`."""

    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeUpdateAction(**data)


class ProductTypeUpdateSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeUpdate`."""

    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addAttributeDefinition": "commercetools._schemas._product_type.ProductTypeAddAttributeDefinitionActionSchema",
                "addLocalizedEnumValue": "commercetools._schemas._product_type.ProductTypeAddLocalizedEnumValueActionSchema",
                "addPlainEnumValue": "commercetools._schemas._product_type.ProductTypeAddPlainEnumValueActionSchema",
                "changeAttributeConstraint": "commercetools._schemas._product_type.ProductTypeChangeAttributeConstraintActionSchema",
                "changeAttributeName": "commercetools._schemas._product_type.ProductTypeChangeAttributeNameActionSchema",
                "changeAttributeOrder": "commercetools._schemas._product_type.ProductTypeChangeAttributeOrderActionSchema",
                "changeAttributeOrderByName": "commercetools._schemas._product_type.ProductTypeChangeAttributeOrderByNameActionSchema",
                "changeDescription": "commercetools._schemas._product_type.ProductTypeChangeDescriptionActionSchema",
                "changeEnumKey": "commercetools._schemas._product_type.ProductTypeChangeEnumKeyActionSchema",
                "changeInputHint": "commercetools._schemas._product_type.ProductTypeChangeInputHintActionSchema",
                "changeIsSearchable": "commercetools._schemas._product_type.ProductTypeChangeIsSearchableActionSchema",
                "changeLabel": "commercetools._schemas._product_type.ProductTypeChangeLabelActionSchema",
                "changeLocalizedEnumValueLabel": "commercetools._schemas._product_type.ProductTypeChangeLocalizedEnumValueLabelActionSchema",
                "changeLocalizedEnumValueOrder": "commercetools._schemas._product_type.ProductTypeChangeLocalizedEnumValueOrderActionSchema",
                "changeName": "commercetools._schemas._product_type.ProductTypeChangeNameActionSchema",
                "changePlainEnumValueLabel": "commercetools._schemas._product_type.ProductTypeChangePlainEnumValueLabelActionSchema",
                "changePlainEnumValueOrder": "commercetools._schemas._product_type.ProductTypeChangePlainEnumValueOrderActionSchema",
                "removeAttributeDefinition": "commercetools._schemas._product_type.ProductTypeRemoveAttributeDefinitionActionSchema",
                "removeEnumValues": "commercetools._schemas._product_type.ProductTypeRemoveEnumValuesActionSchema",
                "setInputTip": "commercetools._schemas._product_type.ProductTypeSetInputTipActionSchema",
                "setKey": "commercetools._schemas._product_type.ProductTypeSetKeyActionSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ProductTypeUpdate(**data)


class AttributeBooleanTypeSchema(AttributeTypeSchema):
    """Marshmallow schema for :class:`commercetools.types.AttributeBooleanType`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return types.AttributeBooleanType(**data)


class AttributeDateTimeTypeSchema(AttributeTypeSchema):
    """Marshmallow schema for :class:`commercetools.types.AttributeDateTimeType`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return types.AttributeDateTimeType(**data)


class AttributeDateTypeSchema(AttributeTypeSchema):
    """Marshmallow schema for :class:`commercetools.types.AttributeDateType`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return types.AttributeDateType(**data)


class AttributeEnumTypeSchema(AttributeTypeSchema):
    """Marshmallow schema for :class:`commercetools.types.AttributeEnumType`."""

    values = helpers.LazyNestedField(
        nested="commercetools._schemas._product_type.AttributePlainEnumValueSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return types.AttributeEnumType(**data)


class AttributeLocalizableTextTypeSchema(AttributeTypeSchema):
    """Marshmallow schema for :class:`commercetools.types.AttributeLocalizableTextType`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return types.AttributeLocalizableTextType(**data)


class AttributeLocalizedEnumTypeSchema(AttributeTypeSchema):
    """Marshmallow schema for :class:`commercetools.types.AttributeLocalizedEnumType`."""

    values = helpers.LazyNestedField(
        nested="commercetools._schemas._product_type.AttributeLocalizedEnumValueSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return types.AttributeLocalizedEnumType(**data)


class AttributeMoneyTypeSchema(AttributeTypeSchema):
    """Marshmallow schema for :class:`commercetools.types.AttributeMoneyType`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return types.AttributeMoneyType(**data)


class AttributeNestedTypeSchema(AttributeTypeSchema):
    """Marshmallow schema for :class:`commercetools.types.AttributeNestedType`."""

    type_reference = helpers.LazyNestedField(
        nested="commercetools._schemas._product_type.ProductTypeReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="typeReference",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return types.AttributeNestedType(**data)


class AttributeNumberTypeSchema(AttributeTypeSchema):
    """Marshmallow schema for :class:`commercetools.types.AttributeNumberType`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return types.AttributeNumberType(**data)


class AttributeReferenceTypeSchema(AttributeTypeSchema):
    """Marshmallow schema for :class:`commercetools.types.AttributeReferenceType`."""

    reference_type_id = marshmallow_enum.EnumField(
        types.ReferenceTypeId, by_value=True, data_key="referenceTypeId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return types.AttributeReferenceType(**data)


class AttributeSetTypeSchema(AttributeTypeSchema):
    """Marshmallow schema for :class:`commercetools.types.AttributeSetType`."""

    element_type = helpers.Discriminator(
        discriminator_field=("name", "name"),
        discriminator_schemas={
            "boolean": "commercetools._schemas._product_type.AttributeBooleanTypeSchema",
            "datetime": "commercetools._schemas._product_type.AttributeDateTimeTypeSchema",
            "date": "commercetools._schemas._product_type.AttributeDateTypeSchema",
            "enum": "commercetools._schemas._product_type.AttributeEnumTypeSchema",
            "ltext": "commercetools._schemas._product_type.AttributeLocalizableTextTypeSchema",
            "lenum": "commercetools._schemas._product_type.AttributeLocalizedEnumTypeSchema",
            "money": "commercetools._schemas._product_type.AttributeMoneyTypeSchema",
            "nested": "commercetools._schemas._product_type.AttributeNestedTypeSchema",
            "number": "commercetools._schemas._product_type.AttributeNumberTypeSchema",
            "reference": "commercetools._schemas._product_type.AttributeReferenceTypeSchema",
            "set": "commercetools._schemas._product_type.AttributeSetTypeSchema",
            "text": "commercetools._schemas._product_type.AttributeTextTypeSchema",
            "time": "commercetools._schemas._product_type.AttributeTimeTypeSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="elementType",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return types.AttributeSetType(**data)


class AttributeTextTypeSchema(AttributeTypeSchema):
    """Marshmallow schema for :class:`commercetools.types.AttributeTextType`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return types.AttributeTextType(**data)


class AttributeTimeTypeSchema(AttributeTypeSchema):
    """Marshmallow schema for :class:`commercetools.types.AttributeTimeType`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["name"]
        return types.AttributeTimeType(**data)


class ProductTypeAddAttributeDefinitionActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeAddAttributeDefinitionAction`."""

    attribute = helpers.LazyNestedField(
        nested="commercetools._schemas._product_type.AttributeDefinitionDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeAddAttributeDefinitionAction(**data)


class ProductTypeAddLocalizedEnumValueActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeAddLocalizedEnumValueAction`."""

    attribute_name = marshmallow.fields.String(
        allow_none=True, data_key="attributeName"
    )
    value = helpers.LazyNestedField(
        nested="commercetools._schemas._product_type.AttributeLocalizedEnumValueSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeAddLocalizedEnumValueAction(**data)


class ProductTypeAddPlainEnumValueActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeAddPlainEnumValueAction`."""

    attribute_name = marshmallow.fields.String(
        allow_none=True, data_key="attributeName"
    )
    value = helpers.LazyNestedField(
        nested="commercetools._schemas._product_type.AttributePlainEnumValueSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeAddPlainEnumValueAction(**data)


class ProductTypeChangeAttributeConstraintActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeChangeAttributeConstraintAction`."""

    attribute_name = marshmallow.fields.String(
        allow_none=True, data_key="attributeName"
    )
    new_value = marshmallow_enum.EnumField(
        types.AttributeConstraintEnumDraft, by_value=True, data_key="newValue"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeChangeAttributeConstraintAction(**data)


class ProductTypeChangeAttributeNameActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeChangeAttributeNameAction`."""

    attribute_name = marshmallow.fields.String(
        allow_none=True, data_key="attributeName"
    )
    new_attribute_name = marshmallow.fields.String(
        allow_none=True, data_key="newAttributeName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeChangeAttributeNameAction(**data)


class ProductTypeChangeAttributeOrderActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeChangeAttributeOrderAction`."""

    attributes = helpers.LazyNestedField(
        nested="commercetools._schemas._product_type.AttributeDefinitionSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeChangeAttributeOrderAction(**data)


class ProductTypeChangeAttributeOrderByNameActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeChangeAttributeOrderByNameAction`."""

    attribute_names = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), data_key="attributeNames"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeChangeAttributeOrderByNameAction(**data)


class ProductTypeChangeDescriptionActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeChangeDescriptionAction`."""

    description = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeChangeDescriptionAction(**data)


class ProductTypeChangeEnumKeyActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeChangeEnumKeyAction`."""

    attribute_name = marshmallow.fields.String(
        allow_none=True, data_key="attributeName"
    )
    key = marshmallow.fields.String(allow_none=True)
    new_key = marshmallow.fields.String(allow_none=True, data_key="newKey")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeChangeEnumKeyAction(**data)


class ProductTypeChangeInputHintActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeChangeInputHintAction`."""

    attribute_name = marshmallow.fields.String(
        allow_none=True, data_key="attributeName"
    )
    new_value = marshmallow_enum.EnumField(
        types.TextInputHint, by_value=True, data_key="newValue"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeChangeInputHintAction(**data)


class ProductTypeChangeIsSearchableActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeChangeIsSearchableAction`."""

    attribute_name = marshmallow.fields.String(
        allow_none=True, data_key="attributeName"
    )
    is_searchable = marshmallow.fields.Bool(allow_none=True, data_key="isSearchable")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeChangeIsSearchableAction(**data)


class ProductTypeChangeLabelActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeChangeLabelAction`."""

    attribute_name = marshmallow.fields.String(
        allow_none=True, data_key="attributeName"
    )
    label = LocalizedStringField(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeChangeLabelAction(**data)


class ProductTypeChangeLocalizedEnumValueLabelActionSchema(
    ProductTypeUpdateActionSchema
):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeChangeLocalizedEnumValueLabelAction`."""

    attribute_name = marshmallow.fields.String(
        allow_none=True, data_key="attributeName"
    )
    new_value = helpers.LazyNestedField(
        nested="commercetools._schemas._product_type.AttributeLocalizedEnumValueSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="newValue",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeChangeLocalizedEnumValueLabelAction(**data)


class ProductTypeChangeLocalizedEnumValueOrderActionSchema(
    ProductTypeUpdateActionSchema
):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeChangeLocalizedEnumValueOrderAction`."""

    attribute_name = marshmallow.fields.String(
        allow_none=True, data_key="attributeName"
    )
    values = helpers.LazyNestedField(
        nested="commercetools._schemas._product_type.AttributeLocalizedEnumValueSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeChangeLocalizedEnumValueOrderAction(**data)


class ProductTypeChangeNameActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeChangeNameAction`."""

    name = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeChangeNameAction(**data)


class ProductTypeChangePlainEnumValueLabelActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeChangePlainEnumValueLabelAction`."""

    attribute_name = marshmallow.fields.String(
        allow_none=True, data_key="attributeName"
    )
    new_value = helpers.LazyNestedField(
        nested="commercetools._schemas._product_type.AttributePlainEnumValueSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="newValue",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeChangePlainEnumValueLabelAction(**data)


class ProductTypeChangePlainEnumValueOrderActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeChangePlainEnumValueOrderAction`."""

    attribute_name = marshmallow.fields.String(
        allow_none=True, data_key="attributeName"
    )
    values = helpers.LazyNestedField(
        nested="commercetools._schemas._product_type.AttributePlainEnumValueSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeChangePlainEnumValueOrderAction(**data)


class ProductTypeRemoveAttributeDefinitionActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeRemoveAttributeDefinitionAction`."""

    name = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeRemoveAttributeDefinitionAction(**data)


class ProductTypeRemoveEnumValuesActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeRemoveEnumValuesAction`."""

    attribute_name = marshmallow.fields.String(
        allow_none=True, data_key="attributeName"
    )
    keys = marshmallow.fields.List(marshmallow.fields.String(allow_none=True))

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeRemoveEnumValuesAction(**data)


class ProductTypeSetInputTipActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeSetInputTipAction`."""

    attribute_name = marshmallow.fields.String(
        allow_none=True, data_key="attributeName"
    )
    input_tip = LocalizedStringField(allow_none=True, missing=None, data_key="inputTip")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeSetInputTipAction(**data)


class ProductTypeSetKeyActionSchema(ProductTypeUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProductTypeSetKeyAction`."""

    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProductTypeSetKeyAction(**data)
