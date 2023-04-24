# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from improving_agent.models.base_model_ import Model
from improving_agent.models.attribute import Attribute
from improving_agent.models.qualifier import Qualifier
from improving_agent.models.retrieval_source import RetrievalSource
from improving_agent import util

from improving_agent.models.attribute import Attribute  # noqa: E501
from improving_agent.models.qualifier import Qualifier  # noqa: E501
from improving_agent.models.retrieval_source import RetrievalSource  # noqa: E501

class Edge(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, predicate=None, subject=None, object=None, attributes=None, qualifiers=None, sources=None):  # noqa: E501
        """Edge - a model defined in OpenAPI

        :param predicate: The predicate of this Edge.  # noqa: E501
        :type predicate: EdgePredicate
        :param subject: The subject of this Edge.  # noqa: E501
        :type subject: EdgeSubject
        :param object: The object of this Edge.  # noqa: E501
        :type object: EdgeObject
        :param attributes: The attributes of this Edge.  # noqa: E501
        :type attributes: List[Attribute]
        :param qualifiers: The qualifiers of this Edge.  # noqa: E501
        :type qualifiers: List[Qualifier]
        :param sources: The sources of this Edge.  # noqa: E501
        :type sources: List[RetrievalSource]
        """
        self.openapi_types = {
            'predicate': str,
            'subject': str,
            'object': str,
            'attributes': List[Attribute],
            'qualifiers': List[Qualifier],
            'sources': List[RetrievalSource],
        }

        self.attribute_map = {
            'predicate': 'predicate',
            'subject': 'subject',
            'object': 'object',
            'attributes': 'attributes',
            'qualifiers': 'qualifiers',
            'sources': 'sources'
        }

        self._predicate = predicate
        self._subject = subject
        self._object = object
        self._attributes = attributes
        self._qualifiers = qualifiers
        self._sources = sources

    @classmethod
    def from_dict(cls, dikt) -> 'Edge':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Edge of this Edge.  # noqa: E501
        :rtype: Edge
        """
        return util.deserialize_model(dikt, cls)

    @property
    def predicate(self):
        """Gets the predicate of this Edge.


        :return: The predicate of this Edge.
        :rtype: EdgePredicate
        """
        return self._predicate

    @predicate.setter
    def predicate(self, predicate):
        """Sets the predicate of this Edge.


        :param predicate: The predicate of this Edge.
        :type predicate: EdgePredicate
        """
        if predicate is None:
            raise ValueError("Invalid value for `predicate`, must not be `None`")  # noqa: E501

        self._predicate = predicate

    @property
    def subject(self):
        """Gets the subject of this Edge.


        :return: The subject of this Edge.
        :rtype: EdgeSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Edge.


        :param subject: The subject of this Edge.
        :type subject: EdgeSubject
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def object(self):
        """Gets the object of this Edge.


        :return: The object of this Edge.
        :rtype: EdgeObject
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this Edge.


        :param object: The object of this Edge.
        :type object: EdgeObject
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")  # noqa: E501

        self._object = object

    @property
    def attributes(self):
        """Gets the attributes of this Edge.

        A list of additional attributes for this edge  # noqa: E501

        :return: The attributes of this Edge.
        :rtype: List[Attribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Edge.

        A list of additional attributes for this edge  # noqa: E501

        :param attributes: The attributes of this Edge.
        :type attributes: List[Attribute]
        """

        self._attributes = attributes

    @property
    def qualifiers(self):
        """Gets the qualifiers of this Edge.

        A set of Qualifiers that act together to add nuance or detail to the statement expressed in an Edge.  # noqa: E501

        :return: The qualifiers of this Edge.
        :rtype: List[Qualifier]
        """
        return self._qualifiers

    @qualifiers.setter
    def qualifiers(self, qualifiers):
        """Sets the qualifiers of this Edge.

        A set of Qualifiers that act together to add nuance or detail to the statement expressed in an Edge.  # noqa: E501

        :param qualifiers: The qualifiers of this Edge.
        :type qualifiers: List[Qualifier]
        """

        self._qualifiers = qualifiers

    @property
    def sources(self):
        """Gets the sources of this Edge.

        A list of RetrievalSource objects that provide information about how a particular Information Resource served as a source from which the knowledge expressed in an Edge, or data used to generate this knowledge, was retrieved.  # noqa: E501

        :return: The sources of this Edge.
        :rtype: List[RetrievalSource]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this Edge.

        A list of RetrievalSource objects that provide information about how a particular Information Resource served as a source from which the knowledge expressed in an Edge, or data used to generate this knowledge, was retrieved.  # noqa: E501

        :param sources: The sources of this Edge.
        :type sources: List[RetrievalSource]
        """
        if sources is None:
            raise ValueError("Invalid value for `sources`, must not be `None`")  # noqa: E501
        if sources is not None and len(sources) < 1:
            raise ValueError("Invalid value for `sources`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._sources = sources
