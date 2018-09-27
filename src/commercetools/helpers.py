from marshmallow import class_registry
from marshmallow.fields import Field
from marshmallow.utils import RAISE, is_collection
from marshmallow.utils import missing as missing_
from marshmallow.exceptions import ValidationError, StringNotCollectionError


class Discriminator(Field):
    default_error_messages = {"type": "Invalid type."}

    def __init__(
        self,
        default=missing_,
        exclude=tuple(),
        only=None,
        discriminator_field=None,
        discriminator_schemas=None,
        **kwargs
    ):
        # Raise error if only or exclude is passed as string, not list of strings
        if only is not None and not is_collection(only):
            raise StringNotCollectionError('"only" should be a list of strings')
        if exclude is not None and not is_collection(exclude):
            raise StringNotCollectionError('"exclude" should be a list of strings')
        self.only = only
        self.exclude = exclude
        self.many = kwargs.get("many", False)
        self.unknown = kwargs.get("unknown", RAISE)
        self.discriminator_field = discriminator_field
        self.discriminator_schemas = discriminator_schemas
        self.__updated_fields = False
        super().__init__(default=default, **kwargs)

    def get_schema(self, name):
        context = getattr(self.parent, "context", {})
        schema_class = class_registry.get_class(name)
        schema = schema_class(
            many=self.many,
            only=self.only,
            exclude=self.exclude,
            context=context,
            load_only=self._nested_normalized_option("load_only"),
            dump_only=self._nested_normalized_option("dump_only"),
        )
        schema.ordered = getattr(self.parent, "ordered", False)
        return schema

    def _nested_normalized_option(self, option_name):
        nested_field = "%s." % self.name
        return [
            field.split(nested_field, 1)[1]
            for field in getattr(self.root, option_name, set())
            if field.startswith(nested_field)
        ]

    def _serialize(self, nested_obj, attr, obj):
        discriminator_value = getattr(nested_obj, self.discriminator_field)
        schema_name = self.discriminator_schemas[discriminator_value]
        schema = self.get_schema(schema_name)

        if nested_obj is None:
            return None
        if not self.__updated_fields:
            schema._update_fields(obj=nested_obj, many=self.many)
            self.__updated_fields = True
        try:
            return schema.dump(
                nested_obj, many=self.many, update_fields=not self.__updated_fields
            )
        except ValidationError as exc:
            raise ValidationError(exc.messages, data=obj, valid_data=exc.valid_data)

    def _test_collection(self, value):
        if self.many and not utils.is_collection(value):
            self.fail("type", input=value, type=value.__class__.__name__)

    def _load(self, value, data):
        discriminator_value = value[self.discriminator_field]
        schema_name = self.discriminator_schemas[discriminator_value]
        schema = self.get_schema(schema_name)

        try:
            valid_data = schema.load(value, unknown=self.unknown)
        except ValidationError as exc:
            raise ValidationError(exc.messages, data=data, valid_data=exc.valid_data)
        return valid_data

    def _deserialize(self, value, attr, data):
        self._test_collection(value)
        return self._load(value, data)