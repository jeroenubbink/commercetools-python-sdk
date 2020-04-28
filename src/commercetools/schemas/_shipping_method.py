# DO NOT EDIT! This file is automatically generated

import marshmallow
import marshmallow_enum

from commercetools import helpers, types
from commercetools.schemas._common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)

__all__ = [
    "CartClassificationTierSchema",
    "CartScoreTierSchema",
    "CartValueTierSchema",
    "PriceFunctionSchema",
    "ShippingMethodAddShippingRateActionSchema",
    "ShippingMethodAddZoneActionSchema",
    "ShippingMethodChangeIsDefaultActionSchema",
    "ShippingMethodChangeNameActionSchema",
    "ShippingMethodChangeTaxCategoryActionSchema",
    "ShippingMethodDraftSchema",
    "ShippingMethodPagedQueryResponseSchema",
    "ShippingMethodReferenceSchema",
    "ShippingMethodRemoveShippingRateActionSchema",
    "ShippingMethodRemoveZoneActionSchema",
    "ShippingMethodResourceIdentifierSchema",
    "ShippingMethodSchema",
    "ShippingMethodSetDescriptionActionSchema",
    "ShippingMethodSetKeyActionSchema",
    "ShippingMethodSetLocalizedDescriptionActionSchema",
    "ShippingMethodSetPredicateActionSchema",
    "ShippingMethodUpdateActionSchema",
    "ShippingMethodUpdateSchema",
    "ShippingRateDraftSchema",
    "ShippingRatePriceTierSchema",
    "ShippingRateSchema",
    "ZoneRateDraftSchema",
    "ZoneRateSchema",
]


class PriceFunctionSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.PriceFunction`."
    currency_code = marshmallow.fields.String(data_key="currencyCode")
    function = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.PriceFunction(**data)


class ShippingMethodDraftSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodDraft`."
    key = marshmallow.fields.String(allow_none=True, missing=None)
    name = marshmallow.fields.String(allow_none=True)
    description = marshmallow.fields.String(allow_none=True, missing=None)
    localized_description = LocalizedStringField(
        allow_none=True, missing=None, data_key="localizedDescription"
    )
    tax_category = marshmallow.fields.Nested(
        nested="commercetools.schemas._tax_category.TaxCategoryResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="taxCategory",
    )
    zone_rates = marshmallow.fields.Nested(
        nested="commercetools.schemas._shipping_method.ZoneRateDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        data_key="zoneRates",
    )
    is_default = marshmallow.fields.Bool(allow_none=True, data_key="isDefault")
    predicate = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ShippingMethodDraft(**data)


class ShippingMethodPagedQueryResponseSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodPagedQueryResponse`."
    limit = marshmallow.fields.Integer(allow_none=True)
    count = marshmallow.fields.Integer(allow_none=True)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True)
    results = marshmallow.fields.Nested(
        nested="commercetools.schemas._shipping_method.ShippingMethodSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ShippingMethodPagedQueryResponse(**data)


class ShippingMethodReferenceSchema(ReferenceSchema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodReference`."
    obj = marshmallow.fields.Nested(
        nested="commercetools.schemas._shipping_method.ShippingMethodSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.ShippingMethodReference(**data)


class ShippingMethodResourceIdentifierSchema(ResourceIdentifierSchema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodResourceIdentifier`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.ShippingMethodResourceIdentifier(**data)


class ShippingMethodSchema(BaseResourceSchema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethod`."
    id = marshmallow.fields.String(allow_none=True)
    version = marshmallow.fields.Integer(allow_none=True)
    created_at = marshmallow.fields.DateTime(allow_none=True, data_key="createdAt")
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, data_key="lastModifiedAt"
    )
    last_modified_by = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.LastModifiedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.CreatedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="createdBy",
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)
    name = marshmallow.fields.String(allow_none=True)
    description = marshmallow.fields.String(allow_none=True, missing=None)
    localized_description = LocalizedStringField(
        allow_none=True, missing=None, data_key="localizedDescription"
    )
    tax_category = marshmallow.fields.Nested(
        nested="commercetools.schemas._tax_category.TaxCategoryReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="taxCategory",
    )
    zone_rates = marshmallow.fields.Nested(
        nested="commercetools.schemas._shipping_method.ZoneRateSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        data_key="zoneRates",
    )
    is_default = marshmallow.fields.Bool(allow_none=True, data_key="isDefault")
    predicate = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ShippingMethod(**data)


class ShippingMethodUpdateActionSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodUpdateAction`."
    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShippingMethodUpdateAction(**data)


class ShippingMethodUpdateSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodUpdate`."
    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addShippingRate": "commercetools.schemas._shipping_method.ShippingMethodAddShippingRateActionSchema",
                "addZone": "commercetools.schemas._shipping_method.ShippingMethodAddZoneActionSchema",
                "changeIsDefault": "commercetools.schemas._shipping_method.ShippingMethodChangeIsDefaultActionSchema",
                "changeName": "commercetools.schemas._shipping_method.ShippingMethodChangeNameActionSchema",
                "changeTaxCategory": "commercetools.schemas._shipping_method.ShippingMethodChangeTaxCategoryActionSchema",
                "removeShippingRate": "commercetools.schemas._shipping_method.ShippingMethodRemoveShippingRateActionSchema",
                "removeZone": "commercetools.schemas._shipping_method.ShippingMethodRemoveZoneActionSchema",
                "setDescription": "commercetools.schemas._shipping_method.ShippingMethodSetDescriptionActionSchema",
                "setKey": "commercetools.schemas._shipping_method.ShippingMethodSetKeyActionSchema",
                "setLocalizedDescription": "commercetools.schemas._shipping_method.ShippingMethodSetLocalizedDescriptionActionSchema",
                "setPredicate": "commercetools.schemas._shipping_method.ShippingMethodSetPredicateActionSchema",
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
        return types.ShippingMethodUpdate(**data)


class ShippingRateDraftSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ShippingRateDraft`."
    price = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    free_above = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="freeAbove",
    )
    tiers = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("type", "type"),
            discriminator_schemas={
                "CartClassification": "commercetools.schemas._shipping_method.CartClassificationTierSchema",
                "CartScore": "commercetools.schemas._shipping_method.CartScoreTierSchema",
                "CartValue": "commercetools.schemas._shipping_method.CartValueTierSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ShippingRateDraft(**data)


class ShippingRatePriceTierSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ShippingRatePriceTier`."
    type = marshmallow_enum.EnumField(types.ShippingRateTierType, by_value=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.ShippingRatePriceTier(**data)


class ShippingRateSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ShippingRate`."
    price = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": "commercetools.schemas._common.CentPrecisionMoneySchema",
            "highPrecision": "commercetools.schemas._common.HighPrecisionMoneySchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    free_above = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": "commercetools.schemas._common.CentPrecisionMoneySchema",
            "highPrecision": "commercetools.schemas._common.HighPrecisionMoneySchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="freeAbove",
    )
    is_matching = marshmallow.fields.Bool(
        allow_none=True, missing=None, data_key="isMatching"
    )
    tiers = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("type", "type"),
            discriminator_schemas={
                "CartClassification": "commercetools.schemas._shipping_method.CartClassificationTierSchema",
                "CartScore": "commercetools.schemas._shipping_method.CartScoreTierSchema",
                "CartValue": "commercetools.schemas._shipping_method.CartValueTierSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        )
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ShippingRate(**data)


class ZoneRateDraftSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ZoneRateDraft`."
    zone = marshmallow.fields.Nested(
        nested="commercetools.schemas._zone.ZoneResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    shipping_rates = marshmallow.fields.Nested(
        nested="commercetools.schemas._shipping_method.ShippingRateDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        data_key="shippingRates",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ZoneRateDraft(**data)


class ZoneRateSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ZoneRate`."
    zone = marshmallow.fields.Nested(
        nested="commercetools.schemas._zone.ZoneReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    shipping_rates = marshmallow.fields.Nested(
        nested="commercetools.schemas._shipping_method.ShippingRateSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        data_key="shippingRates",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ZoneRate(**data)


class CartClassificationTierSchema(ShippingRatePriceTierSchema):
    "Marshmallow schema for :class:`commercetools.types.CartClassificationTier`."
    value = marshmallow.fields.String(allow_none=True)
    price = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    is_matching = marshmallow.fields.Bool(
        allow_none=True, missing=None, data_key="isMatching"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.CartClassificationTier(**data)


class CartScoreTierSchema(ShippingRatePriceTierSchema):
    "Marshmallow schema for :class:`commercetools.types.CartScoreTier`."
    score = marshmallow.fields.Integer(allow_none=True)
    price = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    price_function = marshmallow.fields.Nested(
        nested="commercetools.schemas._shipping_method.PriceFunctionSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="priceFunction",
    )
    is_matching = marshmallow.fields.Bool(
        allow_none=True, missing=None, data_key="isMatching"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.CartScoreTier(**data)


class CartValueTierSchema(ShippingRatePriceTierSchema):
    "Marshmallow schema for :class:`commercetools.types.CartValueTier`."
    minimum_cent_amount = marshmallow.fields.Integer(
        allow_none=True, data_key="minimumCentAmount"
    )
    price = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    is_matching = marshmallow.fields.Bool(
        allow_none=True, missing=None, data_key="isMatching"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.CartValueTier(**data)


class ShippingMethodAddShippingRateActionSchema(ShippingMethodUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodAddShippingRateAction`."
    zone = marshmallow.fields.Nested(
        nested="commercetools.schemas._zone.ZoneResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    shipping_rate = marshmallow.fields.Nested(
        nested="commercetools.schemas._shipping_method.ShippingRateDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="shippingRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShippingMethodAddShippingRateAction(**data)


class ShippingMethodAddZoneActionSchema(ShippingMethodUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodAddZoneAction`."
    zone = marshmallow.fields.Nested(
        nested="commercetools.schemas._zone.ZoneResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShippingMethodAddZoneAction(**data)


class ShippingMethodChangeIsDefaultActionSchema(ShippingMethodUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodChangeIsDefaultAction`."
    is_default = marshmallow.fields.Bool(allow_none=True, data_key="isDefault")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShippingMethodChangeIsDefaultAction(**data)


class ShippingMethodChangeNameActionSchema(ShippingMethodUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodChangeNameAction`."
    name = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShippingMethodChangeNameAction(**data)


class ShippingMethodChangeTaxCategoryActionSchema(ShippingMethodUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodChangeTaxCategoryAction`."
    tax_category = marshmallow.fields.Nested(
        nested="commercetools.schemas._tax_category.TaxCategoryResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="taxCategory",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShippingMethodChangeTaxCategoryAction(**data)


class ShippingMethodRemoveShippingRateActionSchema(ShippingMethodUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodRemoveShippingRateAction`."
    zone = marshmallow.fields.Nested(
        nested="commercetools.schemas._zone.ZoneResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    shipping_rate = marshmallow.fields.Nested(
        nested="commercetools.schemas._shipping_method.ShippingRateDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="shippingRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShippingMethodRemoveShippingRateAction(**data)


class ShippingMethodRemoveZoneActionSchema(ShippingMethodUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodRemoveZoneAction`."
    zone = marshmallow.fields.Nested(
        nested="commercetools.schemas._zone.ZoneResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShippingMethodRemoveZoneAction(**data)


class ShippingMethodSetDescriptionActionSchema(ShippingMethodUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodSetDescriptionAction`."
    description = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShippingMethodSetDescriptionAction(**data)


class ShippingMethodSetKeyActionSchema(ShippingMethodUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodSetKeyAction`."
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShippingMethodSetKeyAction(**data)


class ShippingMethodSetLocalizedDescriptionActionSchema(
    ShippingMethodUpdateActionSchema
):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodSetLocalizedDescriptionAction`."
    localized_description = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="localizedDescription"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShippingMethodSetLocalizedDescriptionAction(**data)


class ShippingMethodSetPredicateActionSchema(ShippingMethodUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ShippingMethodSetPredicateAction`."
    predicate = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShippingMethodSetPredicateAction(**data)
