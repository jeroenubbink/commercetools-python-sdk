# DO NOT EDIT! This file is automatically generated

import re

import marshmallow
import marshmallow_enum

from commercetools import helpers, types
from commercetools.schemas._base import (
    PagedQueryResponseSchema,
    UpdateActionSchema,
    UpdateSchema,
)
from commercetools.schemas._common import (
    LocalizedStringField,
    ReferenceSchema,
    ResourceSchema,
)

__all__ = [
    "CartDiscountChangeCartPredicateActionSchema",
    "CartDiscountChangeIsActiveActionSchema",
    "CartDiscountChangeNameActionSchema",
    "CartDiscountChangeRequiresDiscountCodeActionSchema",
    "CartDiscountChangeSortOrderActionSchema",
    "CartDiscountChangeStackingModeActionSchema",
    "CartDiscountChangeTargetActionSchema",
    "CartDiscountChangeValueActionSchema",
    "CartDiscountCustomLineItemsTargetSchema",
    "CartDiscountDraftSchema",
    "CartDiscountLineItemsTargetSchema",
    "CartDiscountPagedQueryResponseSchema",
    "CartDiscountReferenceSchema",
    "CartDiscountSchema",
    "CartDiscountSetCustomFieldActionSchema",
    "CartDiscountSetCustomTypeActionSchema",
    "CartDiscountSetDescriptionActionSchema",
    "CartDiscountSetValidFromActionSchema",
    "CartDiscountSetValidFromAndUntilActionSchema",
    "CartDiscountSetValidUntilActionSchema",
    "CartDiscountShippingCostTargetSchema",
    "CartDiscountTargetSchema",
    "CartDiscountUpdateActionSchema",
    "CartDiscountUpdateSchema",
    "CartDiscountValueAbsoluteSchema",
    "CartDiscountValueGiftLineItemSchema",
    "CartDiscountValueRelativeSchema",
    "CartDiscountValueSchema",
    "MultiBuyCustomLineItemsTargetSchema",
    "MultiBuyLineItemsTargetSchema",
]


class CartDiscountDraftSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountDraft`."
    name = LocalizedStringField(allow_none=True)
    description = LocalizedStringField(allow_none=True, missing=None)
    value = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "absolute": "commercetools.schemas._cart_discount.CartDiscountValueAbsoluteSchema",
            "giftLineItem": "commercetools.schemas._cart_discount.CartDiscountValueGiftLineItemSchema",
            "relative": "commercetools.schemas._cart_discount.CartDiscountValueRelativeSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    cart_predicate = marshmallow.fields.String(
        allow_none=True, data_key="cartPredicate"
    )
    target = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "customLineItems": "commercetools.schemas._cart_discount.CartDiscountCustomLineItemsTargetSchema",
            "lineItems": "commercetools.schemas._cart_discount.CartDiscountLineItemsTargetSchema",
            "shipping": "commercetools.schemas._cart_discount.CartDiscountShippingCostTargetSchema",
            "multiBuyCustomLineItems": "commercetools.schemas._cart_discount.MultiBuyCustomLineItemsTargetSchema",
            "multiBuyLineItems": "commercetools.schemas._cart_discount.MultiBuyLineItemsTargetSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    sort_order = marshmallow.fields.String(allow_none=True, data_key="sortOrder")
    is_active = marshmallow.fields.Bool(
        allow_none=True, missing=None, data_key="isActive"
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )
    requires_discount_code = marshmallow.fields.Bool(
        allow_none=True, data_key="requiresDiscountCode"
    )
    stacking_mode = marshmallow_enum.EnumField(
        types.StackingMode, by_value=True, missing=None, data_key="stackingMode"
    )
    custom = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.CartDiscountDraft(**data)


class CartDiscountPagedQueryResponseSchema(PagedQueryResponseSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountPagedQueryResponse`."
    results = marshmallow.fields.Nested(
        nested="commercetools.schemas._cart_discount.CartDiscountSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.CartDiscountPagedQueryResponse(**data)


class CartDiscountReferenceSchema(ReferenceSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountReference`."
    obj = marshmallow.fields.Nested(
        nested="commercetools.schemas._cart_discount.CartDiscountSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type_id"]
        return types.CartDiscountReference(**data)


class CartDiscountSchema(ResourceSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscount`."
    name = LocalizedStringField(allow_none=True)
    description = LocalizedStringField(allow_none=True, missing=None)
    value = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "absolute": "commercetools.schemas._cart_discount.CartDiscountValueAbsoluteSchema",
            "giftLineItem": "commercetools.schemas._cart_discount.CartDiscountValueGiftLineItemSchema",
            "relative": "commercetools.schemas._cart_discount.CartDiscountValueRelativeSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    cart_predicate = marshmallow.fields.String(
        allow_none=True, data_key="cartPredicate"
    )
    target = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "customLineItems": "commercetools.schemas._cart_discount.CartDiscountCustomLineItemsTargetSchema",
            "lineItems": "commercetools.schemas._cart_discount.CartDiscountLineItemsTargetSchema",
            "shipping": "commercetools.schemas._cart_discount.CartDiscountShippingCostTargetSchema",
            "multiBuyCustomLineItems": "commercetools.schemas._cart_discount.MultiBuyCustomLineItemsTargetSchema",
            "multiBuyLineItems": "commercetools.schemas._cart_discount.MultiBuyLineItemsTargetSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    sort_order = marshmallow.fields.String(allow_none=True, data_key="sortOrder")
    is_active = marshmallow.fields.Bool(allow_none=True, data_key="isActive")
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )
    requires_discount_code = marshmallow.fields.Bool(
        allow_none=True, data_key="requiresDiscountCode"
    )
    references = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("typeId", "type_id"),
            discriminator_schemas={
                "cart-discount": "commercetools.schemas._cart_discount.CartDiscountReferenceSchema",
                "cart": "commercetools.schemas._cart.CartReferenceSchema",
                "category": "commercetools.schemas._category.CategoryReferenceSchema",
                "channel": "commercetools.schemas._channel.ChannelReferenceSchema",
                "key-value-document": "commercetools.schemas._custom_object.CustomObjectReferenceSchema",
                "customer-group": "commercetools.schemas._customer_group.CustomerGroupReferenceSchema",
                "customer": "commercetools.schemas._customer.CustomerReferenceSchema",
                "discount-code": "commercetools.schemas._discount_code.DiscountCodeReferenceSchema",
                "inventory-entry": "commercetools.schemas._inventory.InventoryEntryReferenceSchema",
                "order-edit": "commercetools.schemas._order_edit.OrderEditReferenceSchema",
                "order": "commercetools.schemas._order.OrderReferenceSchema",
                "payment": "commercetools.schemas._payment.PaymentReferenceSchema",
                "product-discount": "commercetools.schemas._product_discount.ProductDiscountReferenceSchema",
                "product-type": "commercetools.schemas._product_type.ProductTypeReferenceSchema",
                "product": "commercetools.schemas._product.ProductReferenceSchema",
                "review": "commercetools.schemas._review.ReviewReferenceSchema",
                "shipping-method": "commercetools.schemas._shipping_method.ShippingMethodReferenceSchema",
                "shopping-list": "commercetools.schemas._shopping_list.ShoppingListReferenceSchema",
                "state": "commercetools.schemas._state.StateReferenceSchema",
                "tax-category": "commercetools.schemas._tax_category.TaxCategoryReferenceSchema",
                "type": "commercetools.schemas._type.TypeReferenceSchema",
                "zone": "commercetools.schemas._zone.ZoneReferenceSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        )
    )
    stacking_mode = marshmallow_enum.EnumField(
        types.StackingMode, by_value=True, data_key="stackingMode"
    )
    custom = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.CartDiscount(**data)


class CartDiscountTargetSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountTarget`."
    type = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type"]
        return types.CartDiscountTarget(**data)


class CartDiscountUpdateActionSchema(UpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountUpdateAction`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CartDiscountUpdateAction(**data)


class CartDiscountUpdateSchema(UpdateSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountUpdate`."
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "changeCartPredicate": "commercetools.schemas._cart_discount.CartDiscountChangeCartPredicateActionSchema",
                "changeIsActive": "commercetools.schemas._cart_discount.CartDiscountChangeIsActiveActionSchema",
                "changeName": "commercetools.schemas._cart_discount.CartDiscountChangeNameActionSchema",
                "changeRequiresDiscountCode": "commercetools.schemas._cart_discount.CartDiscountChangeRequiresDiscountCodeActionSchema",
                "changeSortOrder": "commercetools.schemas._cart_discount.CartDiscountChangeSortOrderActionSchema",
                "changeStackingMode": "commercetools.schemas._cart_discount.CartDiscountChangeStackingModeActionSchema",
                "changeTarget": "commercetools.schemas._cart_discount.CartDiscountChangeTargetActionSchema",
                "changeValue": "commercetools.schemas._cart_discount.CartDiscountChangeValueActionSchema",
                "setCustomField": "commercetools.schemas._cart_discount.CartDiscountSetCustomFieldActionSchema",
                "setCustomType": "commercetools.schemas._cart_discount.CartDiscountSetCustomTypeActionSchema",
                "setDescription": "commercetools.schemas._cart_discount.CartDiscountSetDescriptionActionSchema",
                "setValidFrom": "commercetools.schemas._cart_discount.CartDiscountSetValidFromActionSchema",
                "setValidFromAndUntil": "commercetools.schemas._cart_discount.CartDiscountSetValidFromAndUntilActionSchema",
                "setValidUntil": "commercetools.schemas._cart_discount.CartDiscountSetValidUntilActionSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.CartDiscountUpdate(**data)


class CartDiscountValueSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountValue`."
    type = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type"]
        return types.CartDiscountValue(**data)


class CartDiscountChangeCartPredicateActionSchema(CartDiscountUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountChangeCartPredicateAction`."
    cart_predicate = marshmallow.fields.String(
        allow_none=True, data_key="cartPredicate"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CartDiscountChangeCartPredicateAction(**data)


class CartDiscountChangeIsActiveActionSchema(CartDiscountUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountChangeIsActiveAction`."
    is_active = marshmallow.fields.Bool(allow_none=True, data_key="isActive")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CartDiscountChangeIsActiveAction(**data)


class CartDiscountChangeNameActionSchema(CartDiscountUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountChangeNameAction`."
    name = LocalizedStringField(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CartDiscountChangeNameAction(**data)


class CartDiscountChangeRequiresDiscountCodeActionSchema(
    CartDiscountUpdateActionSchema
):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountChangeRequiresDiscountCodeAction`."
    requires_discount_code = marshmallow.fields.Bool(
        allow_none=True, data_key="requiresDiscountCode"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CartDiscountChangeRequiresDiscountCodeAction(**data)


class CartDiscountChangeSortOrderActionSchema(CartDiscountUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountChangeSortOrderAction`."
    sort_order = marshmallow.fields.String(allow_none=True, data_key="sortOrder")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CartDiscountChangeSortOrderAction(**data)


class CartDiscountChangeStackingModeActionSchema(CartDiscountUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountChangeStackingModeAction`."
    stacking_mode = marshmallow_enum.EnumField(
        types.StackingMode, by_value=True, data_key="stackingMode"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CartDiscountChangeStackingModeAction(**data)


class CartDiscountChangeTargetActionSchema(CartDiscountUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountChangeTargetAction`."
    target = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "customLineItems": "commercetools.schemas._cart_discount.CartDiscountCustomLineItemsTargetSchema",
            "lineItems": "commercetools.schemas._cart_discount.CartDiscountLineItemsTargetSchema",
            "shipping": "commercetools.schemas._cart_discount.CartDiscountShippingCostTargetSchema",
            "multiBuyCustomLineItems": "commercetools.schemas._cart_discount.MultiBuyCustomLineItemsTargetSchema",
            "multiBuyLineItems": "commercetools.schemas._cart_discount.MultiBuyLineItemsTargetSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CartDiscountChangeTargetAction(**data)


class CartDiscountChangeValueActionSchema(CartDiscountUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountChangeValueAction`."
    value = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "absolute": "commercetools.schemas._cart_discount.CartDiscountValueAbsoluteSchema",
            "giftLineItem": "commercetools.schemas._cart_discount.CartDiscountValueGiftLineItemSchema",
            "relative": "commercetools.schemas._cart_discount.CartDiscountValueRelativeSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CartDiscountChangeValueAction(**data)


class CartDiscountCustomLineItemsTargetSchema(CartDiscountTargetSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountCustomLineItemsTarget`."
    predicate = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type"]
        return types.CartDiscountCustomLineItemsTarget(**data)


class CartDiscountLineItemsTargetSchema(CartDiscountTargetSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountLineItemsTarget`."
    predicate = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type"]
        return types.CartDiscountLineItemsTarget(**data)


class CartDiscountSetCustomFieldActionSchema(CartDiscountUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountSetCustomFieldAction`."
    name = marshmallow.fields.String(allow_none=True)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CartDiscountSetCustomFieldAction(**data)


class CartDiscountSetCustomTypeActionSchema(CartDiscountUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountSetCustomTypeAction`."
    type = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.TypeReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    fields = marshmallow.fields.Dict(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CartDiscountSetCustomTypeAction(**data)


class CartDiscountSetDescriptionActionSchema(CartDiscountUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountSetDescriptionAction`."
    description = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CartDiscountSetDescriptionAction(**data)


class CartDiscountSetValidFromActionSchema(CartDiscountUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountSetValidFromAction`."
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CartDiscountSetValidFromAction(**data)


class CartDiscountSetValidFromAndUntilActionSchema(CartDiscountUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountSetValidFromAndUntilAction`."
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CartDiscountSetValidFromAndUntilAction(**data)


class CartDiscountSetValidUntilActionSchema(CartDiscountUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountSetValidUntilAction`."
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.CartDiscountSetValidUntilAction(**data)


class CartDiscountShippingCostTargetSchema(CartDiscountTargetSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountShippingCostTarget`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type"]
        return types.CartDiscountShippingCostTarget(**data)


class CartDiscountValueAbsoluteSchema(CartDiscountValueSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountValueAbsolute`."
    money = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type"]
        return types.CartDiscountValueAbsolute(**data)


class CartDiscountValueGiftLineItemSchema(CartDiscountValueSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountValueGiftLineItem`."
    product = marshmallow.fields.Nested(
        nested="commercetools.schemas._product.ProductReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    variant_id = marshmallow.fields.Integer(allow_none=True, data_key="variantId")
    supply_channel = marshmallow.fields.Nested(
        nested="commercetools.schemas._channel.ChannelReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="supplyChannel",
    )
    distribution_channel = marshmallow.fields.Nested(
        nested="commercetools.schemas._channel.ChannelReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="distributionChannel",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type"]
        return types.CartDiscountValueGiftLineItem(**data)


class CartDiscountValueRelativeSchema(CartDiscountValueSchema):
    "Marshmallow schema for :class:`commercetools.types.CartDiscountValueRelative`."
    permyriad = marshmallow.fields.Integer(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type"]
        return types.CartDiscountValueRelative(**data)


class MultiBuyCustomLineItemsTargetSchema(CartDiscountTargetSchema):
    "Marshmallow schema for :class:`commercetools.types.MultiBuyCustomLineItemsTarget`."
    predicate = marshmallow.fields.String(allow_none=True)
    trigger_quantity = marshmallow.fields.Integer(
        allow_none=True, data_key="triggerQuantity"
    )
    discounted_quantity = marshmallow.fields.Integer(
        allow_none=True, data_key="discountedQuantity"
    )
    max_occurrence = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="maxOccurrence"
    )
    selection_mode = marshmallow_enum.EnumField(
        types.SelectionMode, by_value=True, data_key="selectionMode"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type"]
        return types.MultiBuyCustomLineItemsTarget(**data)


class MultiBuyLineItemsTargetSchema(CartDiscountTargetSchema):
    "Marshmallow schema for :class:`commercetools.types.MultiBuyLineItemsTarget`."
    predicate = marshmallow.fields.String(allow_none=True)
    trigger_quantity = marshmallow.fields.Integer(
        allow_none=True, data_key="triggerQuantity"
    )
    discounted_quantity = marshmallow.fields.Integer(
        allow_none=True, data_key="discountedQuantity"
    )
    max_occurrence = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="maxOccurrence"
    )
    selection_mode = marshmallow_enum.EnumField(
        types.SelectionMode, by_value=True, data_key="selectionMode"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type"]
        return types.MultiBuyLineItemsTarget(**data)