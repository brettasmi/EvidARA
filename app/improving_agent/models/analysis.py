from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from improving_agent.models.base_model import Model
from improving_agent.models.attribute import Attribute
from improving_agent.models.edge_binding import EdgeBinding
from improving_agent import util

from improving_agent.models.attribute import Attribute  # noqa: E501
from improving_agent.models.edge_binding import EdgeBinding  # noqa: E501

class Analysis(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, resource_id=None, score=None, edge_bindings=None, support_graphs=None, scoring_method=None, attributes=None):  # noqa: E501
        """Analysis - a model defined in OpenAPI

        :param resource_id: The resource_id of this Analysis.  # noqa: E501
        :type resource_id: str
        :param score: The score of this Analysis.  # noqa: E501
        :type score: float
        :param edge_bindings: The edge_bindings of this Analysis.  # noqa: E501
        :type edge_bindings: Dict[str, List[EdgeBinding]]
        :param support_graphs: The support_graphs of this Analysis.  # noqa: E501
        :type support_graphs: List[str]
        :param scoring_method: The scoring_method of this Analysis.  # noqa: E501
        :type scoring_method: str
        :param attributes: The attributes of this Analysis.  # noqa: E501
        :type attributes: List[Attribute]
        """
        self.openapi_types = {
            'resource_id': str,
            'score': float,
            'edge_bindings': Dict[str, List[EdgeBinding]],
            'support_graphs': List[str],
            'scoring_method': str,
            'attributes': List[Attribute]
        }

        self.attribute_map = {
            'resource_id': 'resource_id',
            'score': 'score',
            'edge_bindings': 'edge_bindings',
            'support_graphs': 'support_graphs',
            'scoring_method': 'scoring_method',
            'attributes': 'attributes'
        }

        self._resource_id = resource_id
        self._score = score
        self._edge_bindings = edge_bindings
        self._support_graphs = support_graphs
        self._scoring_method = scoring_method
        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'Analysis':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Analysis of this Analysis.  # noqa: E501
        :rtype: Analysis
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resource_id(self) -> str:
        """Gets the resource_id of this Analysis.

        A Compact URI, consisting of a prefix and a reference separated by a colon, such as UniProtKB:P00738. Via an external context definition, the CURIE prefix and colon may be replaced by a URI prefix, such as http://identifiers.org/uniprot/, to form a full URI.  # noqa: E501

        :return: The resource_id of this Analysis.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id: str):
        """Sets the resource_id of this Analysis.

        A Compact URI, consisting of a prefix and a reference separated by a colon, such as UniProtKB:P00738. Via an external context definition, the CURIE prefix and colon may be replaced by a URI prefix, such as http://identifiers.org/uniprot/, to form a full URI.  # noqa: E501

        :param resource_id: The resource_id of this Analysis.
        :type resource_id: str
        """
        if resource_id is None:
            raise ValueError("Invalid value for `resource_id`, must not be `None`")  # noqa: E501

        self._resource_id = resource_id

    @property
    def score(self) -> float:
        """Gets the score of this Analysis.

        A numerical score associated with this result indicating the relevance or confidence of this result relative to others in the returned set. Higher MUST be better.  # noqa: E501

        :return: The score of this Analysis.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score: float):
        """Sets the score of this Analysis.

        A numerical score associated with this result indicating the relevance or confidence of this result relative to others in the returned set. Higher MUST be better.  # noqa: E501

        :param score: The score of this Analysis.
        :type score: float
        """

        self._score = score

    @property
    def edge_bindings(self) -> Dict[str, List[EdgeBinding]]:
        """Gets the edge_bindings of this Analysis.

        The dictionary of input Query Graph to Knowledge Graph edge bindings where the dictionary keys are the key identifiers of the Query Graph edges and the associated values of those keys are instances of EdgeBinding schema type (see below). This value is an array of EdgeBindings since a given query edge may resolve to multiple Knowledge Graph Edges.  # noqa: E501

        :return: The edge_bindings of this Analysis.
        :rtype: Dict[str, List[EdgeBinding]]
        """
        return self._edge_bindings

    @edge_bindings.setter
    def edge_bindings(self, edge_bindings: Dict[str, List[EdgeBinding]]):
        """Sets the edge_bindings of this Analysis.

        The dictionary of input Query Graph to Knowledge Graph edge bindings where the dictionary keys are the key identifiers of the Query Graph edges and the associated values of those keys are instances of EdgeBinding schema type (see below). This value is an array of EdgeBindings since a given query edge may resolve to multiple Knowledge Graph Edges.  # noqa: E501

        :param edge_bindings: The edge_bindings of this Analysis.
        :type edge_bindings: Dict[str, List[EdgeBinding]]
        """
        if edge_bindings is None:
            raise ValueError("Invalid value for `edge_bindings`, must not be `None`")  # noqa: E501

        self._edge_bindings = edge_bindings

    @property
    def support_graphs(self) -> List[str]:
        """Gets the support_graphs of this Analysis.

        This is a list of references to Auxiliary Graph instances that supported the analysis of a Result as performed by the reasoning service. Each item in the list is the key of a single Auxiliary Graph.  # noqa: E501

        :return: The support_graphs of this Analysis.
        :rtype: List[str]
        """
        return self._support_graphs

    @support_graphs.setter
    def support_graphs(self, support_graphs: List[str]):
        """Sets the support_graphs of this Analysis.

        This is a list of references to Auxiliary Graph instances that supported the analysis of a Result as performed by the reasoning service. Each item in the list is the key of a single Auxiliary Graph.  # noqa: E501

        :param support_graphs: The support_graphs of this Analysis.
        :type support_graphs: List[str]
        """

        self._support_graphs = support_graphs

    @property
    def scoring_method(self) -> str:
        """Gets the scoring_method of this Analysis.

        An identifier and link to an explanation for the method used to generate the score  # noqa: E501

        :return: The scoring_method of this Analysis.
        :rtype: str
        """
        return self._scoring_method

    @scoring_method.setter
    def scoring_method(self, scoring_method: str):
        """Sets the scoring_method of this Analysis.

        An identifier and link to an explanation for the method used to generate the score  # noqa: E501

        :param scoring_method: The scoring_method of this Analysis.
        :type scoring_method: str
        """

        self._scoring_method = scoring_method

    @property
    def attributes(self) -> List[Attribute]:
        """Gets the attributes of this Analysis.

        The attributes of this particular Analysis.  # noqa: E501

        :return: The attributes of this Analysis.
        :rtype: List[Attribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: List[Attribute]):
        """Sets the attributes of this Analysis.

        The attributes of this particular Analysis.  # noqa: E501

        :param attributes: The attributes of this Analysis.
        :type attributes: List[Attribute]
        """

        self._attributes = attributes
