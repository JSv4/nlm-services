from datetime import datetime

from server import util
from server.models.base_model_ import Model
from server.models.search_criteria import SearchCriteria


class SearchHistory(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        id: str = None,
        user_id: str = None,
        doc_id: str = None,
        workspace_id: str = None,
        timestamp: datetime = None,
        search_criteria: SearchCriteria = None,
    ):  # noqa: E501
        """SearchHistory - a model defined in Swagger

        :param user_id: The user_id of this SearchHistory.  # noqa: E501
        :type user_id: str
        :param doc_id: The doc_id of this SearchHistory.  # noqa: E501
        :type doc_id: str
        :param workspace_id: The workspace_id of this SearchHistory.  # noqa: E501
        :type workspace_id: str
        :param question: The question of this SearchHistory.  # noqa: E501
        :type question: List[str]
        :param pattern: The pattern of this SearchHistory.  # noqa: E501
        :type pattern: List[str]
        :param id: The id of this SearchHistory.  # noqa: E501
        :type id: str
        :param timestamp: The timestamp of this SearchHistory.  # noqa: E501
        :type timestamp: datetime
        """
        self.swagger_types = {
            "id": str,
            "user_id": str,
            "doc_id": str,
            "workspace_id": str,
            "timestamp": datetime,
            "search_criteria": SearchCriteria,
        }

        self.attribute_map = {
            "id": "id",
            "user_id": "user_id",
            "doc_id": "doc_id",
            "workspace_id": "workspace_id",
            "timestamp": "timestamp",
            "search_criteria": "searchCriteria",
        }
        self._id = id
        self._user_id = user_id
        self._doc_id = doc_id
        self._workspace_id = workspace_id
        self._timestamp = timestamp
        self._search_criteria = search_criteria

    @classmethod
    def from_dict(cls, dikt) -> "SearchHistory":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SearchHistory of this SearchHistory.  # noqa: E501
        :rtype: SearchHistory
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this SearchHistory.


        :return: The id of this SearchHistory.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this SearchHistory.


        :param id: The id of this SearchHistory.
        :type id: str
        """

        self._id = id

    @property
    def user_id(self) -> str:
        """Gets the user_id of this SearchHistory.


        :return: The user_id of this SearchHistory.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this SearchHistory.


        :param user_id: The user_id of this SearchHistory.
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def doc_id(self) -> str:
        """Gets the doc_id of this SearchHistory.


        :return: The doc_id of this SearchHistory.
        :rtype: str
        """
        return self._doc_id

    @doc_id.setter
    def doc_id(self, doc_id: str):
        """Sets the doc_id of this SearchHistory.


        :param doc_id: The doc_id of this SearchHistory.
        :type doc_id: str
        """

        self._doc_id = doc_id

    @property
    def workspace_id(self) -> str:
        """Gets the workspace_id of this SearchHistory.


        :return: The workspace_id of this SearchHistory.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id: str):
        """Sets the workspace_id of this SearchHistory.


        :param workspace_id: The workspace_id of this SearchHistory.
        :type workspace_id: str
        """

        self._workspace_id = workspace_id

    @property
    def timestamp(self) -> datetime:
        """Gets the timestamp of this SearchHistory.


        :return: The timestamp of this SearchHistory.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        """Sets the timestamp of this SearchHistory.


        :param timestamp: The timestamp of this SearchHistory.
        :type timestamp: datetime
        """

        self._timestamp = timestamp

    @property
    def search_criteria(self) -> SearchCriteria:
        """Gets the search_criteria of this SearchCriteria.


        :return: The search_criteria of this SearchCriteria.
        :rtype: SearchCriteria
        """
        if isinstance(self._search_criteria, dict):
            self._search_criteria = SearchCriteria(**self._search_criteria)
        return self._search_criteria

    @search_criteria.setter
    def search_criteria(self, search_criteria: SearchCriteria):
        """Sets the search_criteria of this SearchCriteria.


        :param search_criteria: The search_criteria of this SearchCriteria.
        :type search_criteria: SearchCriteria
        """

        self._search_criteria = search_criteria
