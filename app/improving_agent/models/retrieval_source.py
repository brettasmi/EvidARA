# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from improving_agent.models.base_model_ import Model
from improving_agent.models.resource_role_enum import ResourceRoleEnum
from improving_agent import util

from improving_agent.models.resource_role_enum import ResourceRoleEnum  # noqa: E501

class RetrievalSource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, resource_id=None, resource_role=None, upstream_resource_ids=None, source_record_urls=None):  # noqa: E501
        """RetrievalSource - a model defined in OpenAPI

        :param resource_id: The resource_id of this RetrievalSource.  # noqa: E501
        :type resource_id: str
        :param resource_role: The resource_role of this RetrievalSource.  # noqa: E501
        :type resource_role: ResourceRoleEnum
        :param upstream_resource_ids: The upstream_resource_ids of this RetrievalSource.  # noqa: E501
        :type upstream_resource_ids: List[str]
        :param source_record_urls: The source_record_urls of this RetrievalSource.  # noqa: E501
        :type source_record_urls: List[str]
        """
        self.openapi_types = {
            'resource_id': str,
            'resource_role': ResourceRoleEnum,
            'upstream_resource_ids': List[str],
            'source_record_urls': List[str]
        }

        self.attribute_map = {
            'resource_id': 'resource_id',
            'resource_role': 'resource_role',
            'upstream_resource_ids': 'upstream_resource_ids',
            'source_record_urls': 'source_record_urls'
        }

        self._resource_id = resource_id
        self._resource_role = resource_role
        self._upstream_resource_ids = upstream_resource_ids
        self._source_record_urls = source_record_urls

    @classmethod
    def from_dict(cls, dikt) -> 'RetrievalSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RetrievalSource of this RetrievalSource.  # noqa: E501
        :rtype: RetrievalSource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resource_id(self):
        """Gets the resource_id of this RetrievalSource.

        A Compact URI, consisting of a prefix and a reference separated by a colon, such as UniProtKB:P00738. Via an external context definition, the CURIE prefix and colon may be replaced by a URI prefix, such as http://identifiers.org/uniprot/, to form a full URI.  # noqa: E501

        :return: The resource_id of this RetrievalSource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this RetrievalSource.

        A Compact URI, consisting of a prefix and a reference separated by a colon, such as UniProtKB:P00738. Via an external context definition, the CURIE prefix and colon may be replaced by a URI prefix, such as http://identifiers.org/uniprot/, to form a full URI.  # noqa: E501

        :param resource_id: The resource_id of this RetrievalSource.
        :type resource_id: str
        """

        self._resource_id = resource_id

    @property
    def resource_role(self):
        """Gets the resource_role of this RetrievalSource.


        :return: The resource_role of this RetrievalSource.
        :rtype: ResourceRoleEnum
        """
        return self._resource_role

    @resource_role.setter
    def resource_role(self, resource_role):
        """Sets the resource_role of this RetrievalSource.


        :param resource_role: The resource_role of this RetrievalSource.
        :type resource_role: ResourceRoleEnum
        """
        if resource_role is None:
            raise ValueError("Invalid value for `resource_role`, must not be `None`")  # noqa: E501

        self._resource_role = resource_role

    @property
    def upstream_resource_ids(self):
        """Gets the upstream_resource_ids of this RetrievalSource.

        An upstream InformationResource from which the resource being described directly retrieved a record of the knowledge expressed in the Edge, or data used to generate this knowledge. This is an array because there are cases where a merged Edge holds knowledge that was retrieved from multiple sources. e.g. an Edge provided by the ARAGORN ARA can expressing knowledge it retrieved from both the automat-mychem-info and molepro KPs, which both provided it with records of this single fact.  # noqa: E501

        :return: The upstream_resource_ids of this RetrievalSource.
        :rtype: List[str]
        """
        return self._upstream_resource_ids

    @upstream_resource_ids.setter
    def upstream_resource_ids(self, upstream_resource_ids):
        """Sets the upstream_resource_ids of this RetrievalSource.

        An upstream InformationResource from which the resource being described directly retrieved a record of the knowledge expressed in the Edge, or data used to generate this knowledge. This is an array because there are cases where a merged Edge holds knowledge that was retrieved from multiple sources. e.g. an Edge provided by the ARAGORN ARA can expressing knowledge it retrieved from both the automat-mychem-info and molepro KPs, which both provided it with records of this single fact.  # noqa: E501

        :param upstream_resource_ids: The upstream_resource_ids of this RetrievalSource.
        :type upstream_resource_ids: List[str]
        """

        self._upstream_resource_ids = upstream_resource_ids

    @property
    def source_record_urls(self):
        """Gets the source_record_urls of this RetrievalSource.

        A URL linking to a specific web page or document provided by the  source, that contains a record of the knowledge expressed in the  Edge. If the knowledge is contained in more than one web page on  an Information Resource's site, urls MAY be provided for each.  For example, Therapeutic Targets Database (TTD) has separate web  pages for 'Imatinib' and its protein target KIT, both of which hold  the claim that 'the KIT protein is a therapeutic target for Imatinib'.           # noqa: E501

        :return: The source_record_urls of this RetrievalSource.
        :rtype: List[str]
        """
        return self._source_record_urls

    @source_record_urls.setter
    def source_record_urls(self, source_record_urls):
        """Sets the source_record_urls of this RetrievalSource.

        A URL linking to a specific web page or document provided by the  source, that contains a record of the knowledge expressed in the  Edge. If the knowledge is contained in more than one web page on  an Information Resource's site, urls MAY be provided for each.  For example, Therapeutic Targets Database (TTD) has separate web  pages for 'Imatinib' and its protein target KIT, both of which hold  the claim that 'the KIT protein is a therapeutic target for Imatinib'.           # noqa: E501

        :param source_record_urls: The source_record_urls of this RetrievalSource.
        :type source_record_urls: List[str]
        """

        self._source_record_urls = source_record_urls
