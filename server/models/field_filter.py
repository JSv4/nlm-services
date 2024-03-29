from server import util
from server.models.base_model_ import Model


class FieldFilter(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        field_bundle_id: str = "",
        filter_model: object = None,
        **kwargs,
    ):  # noqa: E501
        """Criteria - a model defined in Swagger

        :param field_bundle_id: The question of this Field Filter.  # noqa: E501
        :type field_bundle_id: str
        :param filter_model: The templates of this Criteria.  # noqa: E501
        :type filter_model: object
        """
        self.swagger_types = {
            "field_bundle_id": str,
            "filter_model": object,
        }

        self.attribute_map = {
            "field_bundle_id": "fieldBundleId",
            "filter_model": "filterModel",
        }

        self._field_bundle_id = field_bundle_id
        self._filter_model = filter_model

    @classmethod
    def from_dict(cls, dikt) -> "FieldFilter":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FieldFilter of this FieldFilter.  # noqa: E501
        :rtype: FieldFilter
        """
        return util.deserialize_model(dikt, cls)

    @property
    def field_bundle_id(self) -> str:
        """Gets the field_bundle_id of this FieldFilter.


        :return: The field_bundle_id of this FieldFilter.
        :rtype: str
        """
        return self._field_bundle_id

    @field_bundle_id.setter
    def field_bundle_id(self, field_bundle_id: str):
        """Sets the field_bundle_id of this FieldFilter.


        :param field_bundle_id: The field_bundle_id of this FieldFilter.
        :type field_bundle_id: str
        """

        self._field_bundle_id = field_bundle_id

    @property
    def filter_model(self) -> object:
        """Gets the filter_model of this FieldFilter.


        :return: The filter_model of this FieldFilter.
        :rtype: str
        """
        return self._filter_model

    @filter_model.setter
    def filter_model(self, filter_model: object):
        """Sets the filter_model of this FieldFilter.


        :param filter_model: The templates of this FieldFilter.
        :type filter_model: List[str]
        """

        self._filter_model = filter_model
