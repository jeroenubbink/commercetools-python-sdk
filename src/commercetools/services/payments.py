# DO NOT EDIT! This file is automatically generated
import typing

from commercetools import schemas, types
from commercetools.helpers import RemoveEmptyValuesMixin
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _PaymentQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _PaymentUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _PaymentDeleteSchema(
    traits.VersionedSchema, traits.ExpandableSchema, traits.DataErasureSchema
):
    pass


class PaymentService(abstract.AbstractService):
    """Payments hold information about the current state of receiving and/or
    refunding money"""

    def get_by_id(self, id: str, *, expand: OptionalListStr = None) -> types.Payment:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"payments/{id}", params=params, schema_cls=schemas.PaymentSchema
        )

    def get_by_key(self, key: str, *, expand: OptionalListStr = None) -> types.Payment:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"payments/key={key}",
            params=params,
            schema_cls=schemas.PaymentSchema,
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
    ) -> types.PaymentPagedQueryResponse:
        """Payments hold information about the current state of receiving and/or
        refunding money
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
            _PaymentQuerySchema,
        )
        return self._client._get(
            endpoint="payments",
            params=params,
            schema_cls=schemas.PaymentPagedQueryResponseSchema,
        )

    def create(
        self, draft: types.PaymentDraft, *, expand: OptionalListStr = None
    ) -> types.Payment:
        """To create a payment object a payment draft object has to be given with
        the request.

        Payments hold information about the current state of receiving and/or
        refunding money
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="payments",
            params=params,
            data_object=draft,
            request_schema_cls=schemas.PaymentDraftSchema,
            response_schema_cls=schemas.PaymentSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[types.PaymentUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> types.Payment:
        params = self._serialize_params({"expand": expand}, _PaymentUpdateSchema)
        update_action = types.PaymentUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"payments/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.PaymentUpdateSchema,
            response_schema_cls=schemas.PaymentSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[types.PaymentUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> types.Payment:
        params = self._serialize_params({"expand": expand}, _PaymentUpdateSchema)
        update_action = types.PaymentUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"payments/key={key}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.PaymentUpdateSchema,
            response_schema_cls=schemas.PaymentSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        data_erasure: bool = None,
        force_delete: bool = False,
    ) -> types.Payment:
        params = self._serialize_params(
            {"version": version, "expand": expand, "dataErasure": data_erasure},
            _PaymentDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"payments/{id}",
            params=params,
            response_schema_cls=schemas.PaymentSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        data_erasure: bool = None,
        force_delete: bool = False,
    ) -> types.Payment:
        params = self._serialize_params(
            {"version": version, "expand": expand, "dataErasure": data_erasure},
            _PaymentDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"payments/key={key}",
            params=params,
            response_schema_cls=schemas.PaymentSchema,
            force_delete=force_delete,
        )
