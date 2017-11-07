# -*- coding: utf-8 -*-
__author__ = 'huash06'


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pydot
# import pygraphviz
import os
import networkx as nx
import matplotlib.image as mpimg

try:
    from networkx import graphviz_layout
except ImportError:
    raise ImportError("This example needs Graphviz and either PyGraphviz or Pydot")


def draw_tree(root, file_path):
    # 无向图用 graph_type='graph'
    graph = pydot.Dot(graph_type='digraph')
    # G = nx.Graph()

    file_path = os.path.abspath('output/' + file_path)
    # print('Write to ', file_path)
    node = root
    nodes = []
    graphNode = []
    nodes.append(root)
    pNode = pydot.Node(str(node), style="filled", fillcolor="green")
    graph.add_node(pNode)
    graphNode.append(pNode)
    nodeIndex = 1
    while len(nodes) > 0:
        node = nodes.pop()
        pNode = graphNode.pop()

        for child in node.children:
            if child is None:
                continue
            text = "{0}\n{1}".format(nodeIndex, str(child))
            nodeIndex += 1
            cNode = pydot.Node(text, label=str(child), style="filled", fillcolor="green")
            graphNode.append(cNode)
            graph.add_node(cNode)
            graph.add_edge(pydot.Edge(pNode, cNode))
            nodes.append(child)
    graph.write_png(file_path)

    img = mpimg.imread(file_path)

    # plot the image
    plt.figure(file_path)
    plt.imshow(img, aspect='equal')
    plt.show(block=True)

