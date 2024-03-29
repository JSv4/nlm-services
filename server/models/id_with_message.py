# coding: utf-8

from __future__ import absolute_import

from server import util
from server.models.base_model_ import Model


class IdWithMessage(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, message: str=None):  # noqa: E501
        """IdWithMessage - a model defined in Swagger

        :param id: The id of this IdWithMessage.  # noqa: E501
        :type id: str
        :param message: The message of this IdWithMessage.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'id': str,
            'message': str
        }

        self.attribute_map = {
            'id': 'id',
            'message': 'message'
        }
        self._id = id
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'IdWithMessage':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IdWithMessage of this IdWithMessage.  # noqa: E501
        :rtype: IdWithMessage
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this IdWithMessage.


        :return: The id of this IdWithMessage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this IdWithMessage.


        :param id: The id of this IdWithMessage.
        :type id: str
        """

        self._id = id

    @property
    def message(self) -> str:
        """Gets the message of this IdWithMessage.


        :return: The message of this IdWithMessage.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this IdWithMessage.


        :param message: The message of this IdWithMessage.
        :type message: str
        """

        self._message = message
