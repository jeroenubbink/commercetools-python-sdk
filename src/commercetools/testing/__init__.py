from contextlib import contextmanager
import typing

import requests_mock
import wrapt

from commercetools import types
from commercetools.testing.abstract import BaseBackend
from commercetools.testing.auth import AuthBackend
from commercetools.testing.categories import CategoriesBackend
from commercetools.testing.channels import ChannelsBackend
from commercetools.testing.custom_objects import CustomObjectsBackend
from commercetools.testing.extensions import ExtensionsBackend
from commercetools.testing.inventory import InventoryEntryBackend
from commercetools.testing.payments import PaymentsBackend
from commercetools.testing.product_projections import ProductProjectionsBackend
from commercetools.testing.product_types import ProductTypesBackend
from commercetools.testing.products import ProductsBackend
from commercetools.testing.project import ProjectBackend
from commercetools.testing.shipping_methods import ShippingMethodsBackend
from commercetools.testing.subscriptions import SubscriptionsBackend
from commercetools.testing.tax_categories import TaxCategoryBackend
from commercetools.testing.types import TypesBackend


class Storage:
    def __init__(self):
        self._stores = {}

    def init_store(self, name: str) -> typing.Dict[str, typing.Any]:
        return self._stores.setdefault(name, {})
class BackendRepository:
    def __init__(self):
        requests_mock.mock.case_sensitive = True

        self._storage = Storage()

        self.auth = AuthBackend()
        self.categories = CategoriesBackend(self._storage)
        self.channels = ChannelsBackend(self._storage)
        self.custom_objects = CustomObjectsBackend(self._storage)
        self.extensions = ExtensionsBackend(self._storage)
        self.inventory = InventoryEntryBackend(self._storage)
        self.payments = PaymentsBackend(self._storage)
        self.project = ProjectBackend()
        self.products = ProductsBackend(self._storage)
        self.product_projections = ProductProjectionsBackend(
            self._storage, model=self.products.model
        )
        self.product_types = ProductTypesBackend(self._storage)
        self.shipping_methods = ShippingMethodsBackend(self._storage)
        self.tax_categories = TaxCategoryBackend(self._storage)
        self.types = TypesBackend(self._storage)
        self.subscriptions = SubscriptionsBackend(self._storage)

    def register(self, adapter):
        # Bit of a hack, but it works and makes life easier so hey :-)
        for name, value in self.__dict__.items():
            if isinstance(value, BaseBackend):
                value.register(adapter)

        if isinstance(adapter, requests_mock.mocker.Mocker):
            self.requests_mock = adapter


@contextmanager
def backend_mocker(*args, **kwargs):
    with requests_mock.Mocker(real_http=True) as m:
        repo = BackendRepository()
        repo.register(m)
        yield repo


@wrapt.decorator
def mock_commercetools(wrapped, instance, args, kwargs):
    with backend_mocker():
        return wrapped(*args, **kwargs)
