# DO NOT EDIT! This file is automatically generated
import marshmallow

from commercetools import helpers, types
from commercetools._schemas._common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from commercetools._schemas._type import FieldContainerField

__all__ = [
    "CategoryAddAssetActionSchema",
    "CategoryChangeAssetNameActionSchema",
    "CategoryChangeAssetOrderActionSchema",
    "CategoryChangeNameActionSchema",
    "CategoryChangeOrderHintActionSchema",
    "CategoryChangeParentActionSchema",
    "CategoryChangeSlugActionSchema",
    "CategoryDraftSchema",
    "CategoryPagedQueryResponseSchema",
    "CategoryReferenceSchema",
    "CategoryRemoveAssetActionSchema",
    "CategoryResourceIdentifierSchema",
    "CategorySchema",
    "CategorySetAssetCustomFieldActionSchema",
    "CategorySetAssetCustomTypeActionSchema",
    "CategorySetAssetDescriptionActionSchema",
    "CategorySetAssetKeyActionSchema",
    "CategorySetAssetSourcesActionSchema",
    "CategorySetAssetTagsActionSchema",
    "CategorySetCustomFieldActionSchema",
    "CategorySetCustomTypeActionSchema",
    "CategorySetDescriptionActionSchema",
    "CategorySetExternalIdActionSchema",
    "CategorySetKeyActionSchema",
    "CategorySetMetaDescriptionActionSchema",
    "CategorySetMetaKeywordsActionSchema",
    "CategorySetMetaTitleActionSchema",
    "CategoryUpdateActionSchema",
    "CategoryUpdateSchema",
]


class CategoryDraftSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CategoryDraft`."""

    name = LocalizedStringField(allow_none=True)
    slug = LocalizedStringField(allow_none=True)
    description = LocalizedStringField(allow_none=True, missing=None)
    parent = helpers.LazyNestedField(
        nested="commercetools._schemas._category.CategoryResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    order_hint = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="orderHint"
    )
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )
    meta_title = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaTitle"
    )
    meta_description = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaDescription"
    )
    meta_keywords = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaKeywords"
    )
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    assets = helpers.LazyNestedField(
        nested="commercetools._schemas._common.AssetDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CategoryDraft(**data)


class CategoryPagedQueryResponseSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CategoryPagedQueryResponse`."""

    limit = marshmallow.fields.Integer(allow_none=True)
    count = marshmallow.fields.Integer(allow_none=True)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True)
    results = helpers.LazyNestedField(
        nested="commercetools._schemas._category.CategorySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CategoryPagedQueryResponse(**data)


class CategoryReferenceSchema(ReferenceSchema):
    """Marshmallow schema for :class:`commercetools.types.CategoryReference`."""

    obj = helpers.LazyNestedField(
        nested="commercetools._schemas._category.CategorySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.CategoryReference(**data)


class CategoryResourceIdentifierSchema(ResourceIdentifierSchema):
    """Marshmallow schema for :class:`commercetools.types.CategoryResourceIdentifier`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.CategoryResourceIdentifier(**data)


class CategorySchema(BaseResourceSchema):
    """Marshmallow schema for :class:`commercetools.types.Category`."""

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
    name = LocalizedStringField(allow_none=True)
    slug = LocalizedStringField(allow_none=True)
    description = LocalizedStringField(allow_none=True, missing=None)
    ancestors = helpers.LazyNestedField(
        nested="commercetools._schemas._category.CategoryReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )
    parent = helpers.LazyNestedField(
        nested="commercetools._schemas._category.CategoryReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    order_hint = marshmallow.fields.String(allow_none=True, data_key="orderHint")
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )
    meta_title = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaTitle"
    )
    meta_description = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaDescription"
    )
    meta_keywords = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaKeywords"
    )
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    assets = helpers.LazyNestedField(
        nested="commercetools._schemas._common.AssetSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.Category(**data)


class CategoryUpdateActionSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CategoryUpdateAction`."""

    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategoryUpdateAction(**data)


class CategoryUpdateSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CategoryUpdate`."""

    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addAsset": "commercetools._schemas._category.CategoryAddAssetActionSchema",
                "changeAssetName": "commercetools._schemas._category.CategoryChangeAssetNameActionSchema",
                "changeAssetOrder": "commercetools._schemas._category.CategoryChangeAssetOrderActionSchema",
                "changeName": "commercetools._schemas._category.CategoryChangeNameActionSchema",
                "changeOrderHint": "commercetools._schemas._category.CategoryChangeOrderHintActionSchema",
                "changeParent": "commercetools._schemas._category.CategoryChangeParentActionSchema",
                "changeSlug": "commercetools._schemas._category.CategoryChangeSlugActionSchema",
                "removeAsset": "commercetools._schemas._category.CategoryRemoveAssetActionSchema",
                "setAssetCustomField": "commercetools._schemas._category.CategorySetAssetCustomFieldActionSchema",
                "setAssetCustomType": "commercetools._schemas._category.CategorySetAssetCustomTypeActionSchema",
                "setAssetDescription": "commercetools._schemas._category.CategorySetAssetDescriptionActionSchema",
                "setAssetKey": "commercetools._schemas._category.CategorySetAssetKeyActionSchema",
                "setAssetSources": "commercetools._schemas._category.CategorySetAssetSourcesActionSchema",
                "setAssetTags": "commercetools._schemas._category.CategorySetAssetTagsActionSchema",
                "setCustomField": "commercetools._schemas._category.CategorySetCustomFieldActionSchema",
                "setCustomType": "commercetools._schemas._category.CategorySetCustomTypeActionSchema",
                "setDescription": "commercetools._schemas._category.CategorySetDescriptionActionSchema",
                "setExternalId": "commercetools._schemas._category.CategorySetExternalIdActionSchema",
                "setKey": "commercetools._schemas._category.CategorySetKeyActionSchema",
                "setMetaDescription": "commercetools._schemas._category.CategorySetMetaDescriptionActionSchema",
                "setMetaKeywords": "commercetools._schemas._category.CategorySetMetaKeywordsActionSchema",
                "setMetaTitle": "commercetools._schemas._category.CategorySetMetaTitleActionSchema",
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
        return types.CategoryUpdate(**data)


class CategoryAddAssetActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategoryAddAssetAction`."""

    asset = helpers.LazyNestedField(
        nested="commercetools._schemas._common.AssetDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    position = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategoryAddAssetAction(**data)


class CategoryChangeAssetNameActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategoryChangeAssetNameAction`."""

    asset_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetKey"
    )
    name = LocalizedStringField(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategoryChangeAssetNameAction(**data)


class CategoryChangeAssetOrderActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategoryChangeAssetOrderAction`."""

    asset_order = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), data_key="assetOrder"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategoryChangeAssetOrderAction(**data)


class CategoryChangeNameActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategoryChangeNameAction`."""

    name = LocalizedStringField(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategoryChangeNameAction(**data)


class CategoryChangeOrderHintActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategoryChangeOrderHintAction`."""

    order_hint = marshmallow.fields.String(allow_none=True, data_key="orderHint")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategoryChangeOrderHintAction(**data)


class CategoryChangeParentActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategoryChangeParentAction`."""

    parent = helpers.LazyNestedField(
        nested="commercetools._schemas._category.CategoryResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategoryChangeParentAction(**data)


class CategoryChangeSlugActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategoryChangeSlugAction`."""

    slug = LocalizedStringField(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategoryChangeSlugAction(**data)


class CategoryRemoveAssetActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategoryRemoveAssetAction`."""

    asset_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategoryRemoveAssetAction(**data)


class CategorySetAssetCustomFieldActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategorySetAssetCustomFieldAction`."""

    asset_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetKey"
    )
    name = marshmallow.fields.String(allow_none=True)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategorySetAssetCustomFieldAction(**data)


class CategorySetAssetCustomTypeActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategorySetAssetCustomTypeAction`."""

    asset_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetKey"
    )
    type = helpers.LazyNestedField(
        nested="commercetools._schemas._type.TypeResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    fields = marshmallow.fields.Dict(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategorySetAssetCustomTypeAction(**data)


class CategorySetAssetDescriptionActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategorySetAssetDescriptionAction`."""

    asset_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetKey"
    )
    description = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategorySetAssetDescriptionAction(**data)


class CategorySetAssetKeyActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategorySetAssetKeyAction`."""

    asset_id = marshmallow.fields.String(allow_none=True, data_key="assetId")
    asset_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategorySetAssetKeyAction(**data)


class CategorySetAssetSourcesActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategorySetAssetSourcesAction`."""

    asset_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetKey"
    )
    sources = helpers.LazyNestedField(
        nested="commercetools._schemas._common.AssetSourceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategorySetAssetSourcesAction(**data)


class CategorySetAssetTagsActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategorySetAssetTagsAction`."""

    asset_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetId"
    )
    asset_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="assetKey"
    )
    tags = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategorySetAssetTagsAction(**data)


class CategorySetCustomFieldActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategorySetCustomFieldAction`."""

    name = marshmallow.fields.String(allow_none=True)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategorySetCustomFieldAction(**data)


class CategorySetCustomTypeActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategorySetCustomTypeAction`."""

    type = helpers.LazyNestedField(
        nested="commercetools._schemas._type.TypeResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategorySetCustomTypeAction(**data)


class CategorySetDescriptionActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategorySetDescriptionAction`."""

    description = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategorySetDescriptionAction(**data)


class CategorySetExternalIdActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategorySetExternalIdAction`."""

    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategorySetExternalIdAction(**data)


class CategorySetKeyActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategorySetKeyAction`."""

    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategorySetKeyAction(**data)


class CategorySetMetaDescriptionActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategorySetMetaDescriptionAction`."""

    meta_description = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaDescription"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategorySetMetaDescriptionAction(**data)


class CategorySetMetaKeywordsActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategorySetMetaKeywordsAction`."""

    meta_keywords = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaKeywords"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategorySetMetaKeywordsAction(**data)


class CategorySetMetaTitleActionSchema(CategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.CategorySetMetaTitleAction`."""

    meta_title = LocalizedStringField(
        allow_none=True, missing=None, data_key="metaTitle"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.CategorySetMetaTitleAction(**data)
