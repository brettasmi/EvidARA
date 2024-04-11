from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from improving_agent.models.base_model import Model
from improving_agent.models.edge import Edge
from improving_agent.models.node import Node
from improving_agent import util

from improving_agent.models.edge import Edge  # noqa: E501
from improving_agent.models.node import Node  # noqa: E501

class KnowledgeGraph(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, nodes=None, edges=None):  # noqa: E501
        """KnowledgeGraph - a model defined in OpenAPI

        :param nodes: The nodes of this KnowledgeGraph.  # noqa: E501
        :type nodes: Dict[str, Node]
        :param edges: The edges of this KnowledgeGraph.  # noqa: E501
        :type edges: Dict[str, Edge]
        """
        self.openapi_types = {
            'nodes': Dict[str, Node],
            'edges': Dict[str, Edge]
        }

        self.attribute_map = {
            'nodes': 'nodes',
            'edges': 'edges'
        }

        self._nodes = nodes
        self._edges = edges

    @classmethod
    def from_dict(cls, dikt) -> 'KnowledgeGraph':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The KnowledgeGraph of this KnowledgeGraph.  # noqa: E501
        :rtype: KnowledgeGraph
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nodes(self) -> Dict[str, Node]:
        """Gets the nodes of this KnowledgeGraph.

        Dictionary of Node instances used in the KnowledgeGraph, referenced elsewhere in the TRAPI output by the dictionary key.  # noqa: E501

        :return: The nodes of this KnowledgeGraph.
        :rtype: Dict[str, Node]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes: Dict[str, Node]):
        """Sets the nodes of this KnowledgeGraph.

        Dictionary of Node instances used in the KnowledgeGraph, referenced elsewhere in the TRAPI output by the dictionary key.  # noqa: E501

        :param nodes: The nodes of this KnowledgeGraph.
        :type nodes: Dict[str, Node]
        """
        if nodes is None:
            raise ValueError("Invalid value for `nodes`, must not be `None`")  # noqa: E501

        self._nodes = nodes

    @property
    def edges(self) -> Dict[str, Edge]:
        """Gets the edges of this KnowledgeGraph.

        Dictionary of Edge instances used in the KnowledgeGraph, referenced elsewhere in the TRAPI output by the dictionary key.  # noqa: E501

        :return: The edges of this KnowledgeGraph.
        :rtype: Dict[str, Edge]
        """
        return self._edges

    @edges.setter
    def edges(self, edges: Dict[str, Edge]):
        """Sets the edges of this KnowledgeGraph.

        Dictionary of Edge instances used in the KnowledgeGraph, referenced elsewhere in the TRAPI output by the dictionary key.  # noqa: E501

        :param edges: The edges of this KnowledgeGraph.
        :type edges: Dict[str, Edge]
        """
        if edges is None:
            raise ValueError("Invalid value for `edges`, must not be `None`")  # noqa: E501

        self._edges = edges
