# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from improving_agent.models.base_model_ import Model
from improving_agent.models.attribute import Attribute
from improving_agent import util

from improving_agent.models.attribute import Attribute  # noqa: E501

class NodeBinding(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, query_id=None, attributes=None):  # noqa: E501
        """NodeBinding - a model defined in OpenAPI

        :param id: The id of this NodeBinding.  # noqa: E501
        :type id: str
        :param query_id: The query_id of this NodeBinding.  # noqa: E501
        :type query_id: str
        :param attributes: The attributes of this NodeBinding.  # noqa: E501
        :type attributes: List[Attribute]
        """
        self.openapi_types = {
            'id': str,
            'query_id': str,
            'attributes': List[Attribute]
        }

        self.attribute_map = {
            'id': 'id',
            'query_id': 'query_id',
            'attributes': 'attributes'
        }

        self._id = id
        self._query_id = query_id
        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'NodeBinding':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NodeBinding of this NodeBinding.  # noqa: E501
        :rtype: NodeBinding
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this NodeBinding.

        A Compact URI, consisting of a prefix and a reference separated by a colon, such as UniProtKB:P00738. Via an external context definition, the CURIE prefix and colon may be replaced by a URI prefix, such as http://identifiers.org/uniprot/, to form a full URI.  # noqa: E501

        :return: The id of this NodeBinding.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeBinding.

        A Compact URI, consisting of a prefix and a reference separated by a colon, such as UniProtKB:P00738. Via an external context definition, the CURIE prefix and colon may be replaced by a URI prefix, such as http://identifiers.org/uniprot/, to form a full URI.  # noqa: E501

        :param id: The id of this NodeBinding.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def query_id(self):
        """Gets the query_id of this NodeBinding.


        :return: The query_id of this NodeBinding.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this NodeBinding.


        :param query_id: The query_id of this NodeBinding.
        :type query_id: str
        """

        self._query_id = query_id

    @property
    def attributes(self):
        """Gets the attributes of this NodeBinding.

        A list of attributes providing further information about the node binding. This is not intended for capturing node attributes and should only be used for properties that vary from result to result.  # noqa: E501

        :return: The attributes of this NodeBinding.
        :rtype: List[Attribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this NodeBinding.

        A list of attributes providing further information about the node binding. This is not intended for capturing node attributes and should only be used for properties that vary from result to result.  # noqa: E501

        :param attributes: The attributes of this NodeBinding.
        :type attributes: List[Attribute]
        """

        self._attributes = attributes
