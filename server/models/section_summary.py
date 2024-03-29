# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server.models.base_model_ import Model
from server.models.block import Block  # noqa: F401,E501
from server import util


class SectionSummary(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, title: str=None, block: Block=None, n_quoted_words: float=None, noun_chunks: List[str]=None):  # noqa: E501
        """SectionSummary - a model defined in Swagger

        :param title: The title of this SectionSummary.  # noqa: E501
        :type title: str
        :param block: The block of this SectionSummary.  # noqa: E501
        :type block: Block
        :param n_quoted_words: The n_quoted_words of this SectionSummary.  # noqa: E501
        :type n_quoted_words: float
        :param noun_chunks: The noun_chunks of this SectionSummary.  # noqa: E501
        :type noun_chunks: List[str]
        """
        self.swagger_types = {
            'title': str,
            'block': Block,
            'n_quoted_words': float,
            'noun_chunks': List[str]
        }

        self.attribute_map = {
            'title': 'title',
            'block': 'block',
            'n_quoted_words': 'n_quoted_words',
            'noun_chunks': 'noun_chunks'
        }
        self._title = title
        self._block = block
        self._n_quoted_words = n_quoted_words
        self._noun_chunks = noun_chunks

    @classmethod
    def from_dict(cls, dikt) -> 'SectionSummary':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SectionSummary of this SectionSummary.  # noqa: E501
        :rtype: SectionSummary
        """
        return util.deserialize_model(dikt, cls)

    @property
    def title(self) -> str:
        """Gets the title of this SectionSummary.


        :return: The title of this SectionSummary.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this SectionSummary.


        :param title: The title of this SectionSummary.
        :type title: str
        """

        self._title = title

    @property
    def block(self) -> Block:
        """Gets the block of this SectionSummary.


        :return: The block of this SectionSummary.
        :rtype: Block
        """
        return self._block

    @block.setter
    def block(self, block: Block):
        """Sets the block of this SectionSummary.


        :param block: The block of this SectionSummary.
        :type block: Block
        """

        self._block = block

    @property
    def n_quoted_words(self) -> float:
        """Gets the n_quoted_words of this SectionSummary.


        :return: The n_quoted_words of this SectionSummary.
        :rtype: float
        """
        return self._n_quoted_words

    @n_quoted_words.setter
    def n_quoted_words(self, n_quoted_words: float):
        """Sets the n_quoted_words of this SectionSummary.


        :param n_quoted_words: The n_quoted_words of this SectionSummary.
        :type n_quoted_words: float
        """

        self._n_quoted_words = n_quoted_words

    @property
    def noun_chunks(self) -> List[str]:
        """Gets the noun_chunks of this SectionSummary.


        :return: The noun_chunks of this SectionSummary.
        :rtype: List[str]
        """
        return self._noun_chunks

    @noun_chunks.setter
    def noun_chunks(self, noun_chunks: List[str]):
        """Sets the noun_chunks of this SectionSummary.


        :param noun_chunks: The noun_chunks of this SectionSummary.
        :type noun_chunks: List[str]
        """

        self._noun_chunks = noun_chunks
