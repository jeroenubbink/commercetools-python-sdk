# DO NOT EDIT! This file is automatically generated
import typing

from commercetools import schemas, types
from commercetools.helpers import RemoveEmptyValuesMixin
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _CustomerGroupQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _CustomerGroupUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _CustomerGroupDeleteSchema(traits.VersionedSchema, traits.ExpandableSchema):
    pass


class CustomerGroupService(abstract.AbstractService):
    """customer-groups are used to evaluate products and channels."""

    def get_by_id(
        self, id: str, *, expand: OptionalListStr = None
    ) -> types.CustomerGroup:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"customer-groups/{id}",
            params=params,
            schema_cls=schemas.CustomerGroupSchema,
        )

    def get_by_key(
        self, key: str, *, expand: OptionalListStr = None
    ) -> types.CustomerGroup:
        """Gets a customer group by Key."""
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"customer-groups/key={key}",
            params=params,
            schema_cls=schemas.CustomerGroupSchema,
        )

    def query(
        self,
        *,
        expand: OptionalListStr = None,
        sort: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: OptionalListStr = None,
        predicate_var: typing.Dict[str, str] = None,
    ) -> types.CustomerGroupPagedQueryResponse:
        """customer-groups are used to evaluate products and channels.
        """
        params = self._serialize_params(
            {
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
                "predicate_var": predicate_var,
            },
            _CustomerGroupQuerySchema,
        )
        return self._client._get(
            endpoint="customer-groups",
            params=params,
            schema_cls=schemas.CustomerGroupPagedQueryResponseSchema,
        )

    def create(
        self, draft: types.CustomerGroupDraft, *, expand: OptionalListStr = None
    ) -> types.CustomerGroup:
        """customer-groups are used to evaluate products and channels.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="customer-groups",
            params=params,
            data_object=draft,
            request_schema_cls=schemas.CustomerGroupDraftSchema,
            response_schema_cls=schemas.CustomerGroupSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[types.CustomerGroupUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> types.CustomerGroup:
        params = self._serialize_params({"expand": expand}, _CustomerGroupUpdateSchema)
        update_action = types.CustomerGroupUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"customer-groups/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.CustomerGroupUpdateSchema,
            response_schema_cls=schemas.CustomerGroupSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[types.CustomerGroupUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> types.CustomerGroup:
        """Updates a customer group by Key."""
        params = self._serialize_params({"expand": expand}, _CustomerGroupUpdateSchema)
        update_action = types.CustomerGroupUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"customer-groups/key={key}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.CustomerGroupUpdateSchema,
            response_schema_cls=schemas.CustomerGroupSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> types.CustomerGroup:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _CustomerGroupDeleteSchema
        )
        return self._client._delete(
            endpoint=f"customer-groups/{id}",
            params=params,
            response_schema_cls=schemas.CustomerGroupSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> types.CustomerGroup:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _CustomerGroupDeleteSchema
        )
        return self._client._delete(
            endpoint=f"customer-groups/key={key}",
            params=params,
            response_schema_cls=schemas.CustomerGroupSchema,
            force_delete=force_delete,
        )
