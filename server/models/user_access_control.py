from typing import List

from server import util
from server.models.base_model_ import Model


class UserAccessControl(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        user_id: str = None,
        email_id: str = None,
        access_control_list: List[str] = None,
        **kwargs,
    ):  # noqa: E501
        """UserAccessControl - a model defined in Swagger

        :param user_id: The user_id of this UserAccessControl.  # noqa: E501
        :type user_id: str
        :param email_id: The email_id of this UserAccessControl.  # noqa: E501
        :type email_id: str
        :param access_control_list: The access_control_list of this UserAccessControl.  # noqa: E501
        :type access_control_list: List[str]
        """
        self.swagger_types = {
            "user_id": str,
            "email_id": str,
            "access_control_list": List[str],
        }

        self.attribute_map = {
            "user_id": "userId",
            "email_id": "emailId",
            "access_control_list": "accessControlList",
        }

        self._user_id = user_id
        self._email_id = email_id
        self._access_control_list = access_control_list

    @classmethod
    def from_dict(cls, dikt) -> "UserAccessControl":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserAccessControl of this UserAccessControl.  # noqa: E501
        :rtype: UserAccessControl
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_id(self) -> str:
        """Gets the user_id of this UserAccessControl.


        :return: The user_id of this UserAccessControl.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this UserAccessControl.


        :param user_id: The user_id of this UserAccessControl.
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def email_id(self) -> str:
        """Gets the email_id of this UserAccessControl.


        :return: The email_id of this UserAccessControl.
        :rtype: str
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id: str):
        """Sets the email_id of this UserAccessControl.


        :param email_id: The email_id of this UserAccessControl.
        :type email_id: str
        """

        self._email_id = email_id

    @property
    def access_control_list(self) -> List[str]:
        """Gets the access_control_list of this User.


        :return: The access_control_list of this User.
        :rtype: List[str]
        """
        return self._access_control_list

    @access_control_list.setter
    def access_control_list(self, access_control_list: List[str]):
        """Sets the access_control_list of this User.


        :param access_control_list: The access_control_list of this User.
        :type access_control_list: List[str]
        """

        self._access_control_list = access_control_list
