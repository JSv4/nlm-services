# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server.models.base_model_ import Model
from server.models.block import Block  # noqa: F401,E501
from server import util


class KeyValuePair(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, block: Block=None, all_quoted_words: List[str]=None, key: str=None, value: str=None):  # noqa: E501
        """KeyValuePair - a model defined in Swagger

        :param block: The block of this KeyValuePair.  # noqa: E501
        :type block: Block
        :param all_quoted_words: The all_quoted_words of this KeyValuePair.  # noqa: E501
        :type all_quoted_words: List[str]
        :param key: The key of this KeyValuePair.  # noqa: E501
        :type key: str
        :param value: The value of this KeyValuePair.  # noqa: E501
        :type value: str
        """
        self.swagger_types = {
            'block': Block,
            'all_quoted_words': List[str],
            'key': str,
            'value': str
        }

        self.attribute_map = {
            'block': 'block',
            'all_quoted_words': 'all_quoted_words',
            'key': 'key',
            'value': 'value'
        }
        self._block = block
        self._all_quoted_words = all_quoted_words
        self._key = key
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'KeyValuePair':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The KeyValuePair of this KeyValuePair.  # noqa: E501
        :rtype: KeyValuePair
        """
        return util.deserialize_model(dikt, cls)

    @property
    def block(self) -> Block:
        """Gets the block of this KeyValuePair.


        :return: The block of this KeyValuePair.
        :rtype: Block
        """
        return self._block

    @block.setter
    def block(self, block: Block):
        """Sets the block of this KeyValuePair.


        :param block: The block of this KeyValuePair.
        :type block: Block
        """

        self._block = block

    @property
    def all_quoted_words(self) -> List[str]:
        """Gets the all_quoted_words of this KeyValuePair.


        :return: The all_quoted_words of this KeyValuePair.
        :rtype: List[str]
        """
        return self._all_quoted_words

    @all_quoted_words.setter
    def all_quoted_words(self, all_quoted_words: List[str]):
        """Sets the all_quoted_words of this KeyValuePair.


        :param all_quoted_words: The all_quoted_words of this KeyValuePair.
        :type all_quoted_words: List[str]
        """

        self._all_quoted_words = all_quoted_words

    @property
    def key(self) -> str:
        """Gets the key of this KeyValuePair.


        :return: The key of this KeyValuePair.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key: str):
        """Sets the key of this KeyValuePair.


        :param key: The key of this KeyValuePair.
        :type key: str
        """

        self._key = key

    @property
    def value(self) -> str:
        """Gets the value of this KeyValuePair.


        :return: The value of this KeyValuePair.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this KeyValuePair.


        :param value: The value of this KeyValuePair.
        :type value: str
        """

        self._value = value
