from server import util
from server.models.base_model_ import Model


class TemplateToFile(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        id: str = None,
        name: str = None,
        workspace_id: str = None,
        doc_location: str = None,
        mime_type: str = None,
    ):  # noqa: E501
        """TemplateToFile - a model defined in Swagger

        :param extraction_template_id: The extraction_template_id of this TemplateToFile.  # noqa: E501
        :type extraction_template_id: str
        :param document_id: The document_id of this TemplateToFile.  # noqa: E501
        :type document_id: str
        """
        self.swagger_types = {
            "id": str,
            "name": str,
            "doc_location": str,
            "workspace_id": str,
            "mime_type": str,
        }

        self.attribute_map = {
            "id": "id",
            "name": "name",
            "doc_location": "docLocation",
            "workspace_id": "workspaceId",
            "mime_type": "mimeType",
        }
        self.id = id
        self.name = name
        self.doc_location = doc_location
        self.workspace_id = workspace_id
        self.mime_type = mime_type

    @classmethod
    def from_dict(cls, dikt) -> "TemplateToFile":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TemplateToFile of this TemplateToFile.  # noqa: E501
        :rtype: TemplateToFile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def extraction_template_id(self) -> str:
        """Gets the extraction_template_id of this TemplateToFile.


        :return: The extraction_template_id of this TemplateToFile.
        :rtype: str
        """
        return self._extraction_template_id

    @extraction_template_id.setter
    def extraction_template_id(self, extraction_template_id: str):
        """Sets the extraction_template_id of this TemplateToFile.


        :param extraction_template_id: The extraction_template_id of this TemplateToFile.
        :type extraction_template_id: str
        """

        self._extraction_template_id = extraction_template_id

    @property
    def id(self) -> str:
        """Gets the document_id of this TemplateToFile.


        :return: The document_id of this TemplateToFile.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the document_id of this TemplateToFile.


        :param document_id: The document_id of this TemplateToFile.
        :type document_id: str
        """

        self._id = id
