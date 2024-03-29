import pprint
import re  # noqa: F401
from typing import List

from server import util
from server.models.base_model_ import Model


class FilterSearchCriteria(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "criterias": List[object],
    }

    attribute_map = {
        "criterias": "criterias",
    }

    def __init__(self, criterias=None):  # noqa: E501
        """FilterSearchCriteria - a model defined in Swagger"""  # noqa: E501
        self._criterias = None
        self.discriminator = None
        if criterias is not None:
            self.criterias = criterias

    @classmethod
    def from_dict(cls, dikt) -> "FilterSearchCriteria":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FilterSearchCriteria of this FilterSearchCriteria.  # noqa: E501
        :rtype: FilterSearchCriteria
        """
        return util.deserialize_model(dikt, cls)

    @property
    def criterias(self):
        """Gets the criterias of this FilterSearchCriteria.  # noqa: E501


        :return: The criterias of this FilterSearchCriteria.  # noqa: E501
        :rtype: list[FilterSearchCriteriaCriterias]
        """
        return self._criterias

    @criterias.setter
    def criterias(self, criterias):
        """Sets the criterias of this FilterSearchCriteria.


        :param criterias: The criterias of this FilterSearchCriteria.  # noqa: E501
        :type: list[FilterSearchCriteriaCriterias]
        """

        self._criterias = criterias

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value,
                    ),
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    ),
                )
            else:
                result[attr] = value
        if issubclass(FilterSearchCriteria, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FilterSearchCriteria):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other