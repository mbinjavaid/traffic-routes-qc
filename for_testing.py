# import networkx as nx
# import matplotlib.pyplot as plt
# import numpy as np
#
# starting_node = ['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F']
# ending_node = ['B', 'D', 'A', 'C', 'E', 'B', 'D', 'F', 'A', 'C', 'B', 'F', 'C', 'E']
# weights = [100, 15, 10, 5, 5, 5, 5, 10, 15, 5, 5, 5, 10, 5]
#
# G = nx.DiGraph()
#
# # adding nodes
# G.add_nodes_from(starting_node)
# print(G.nodes)
#
#
# for i in range(len(starting_node)):
#     print("start: ", starting_node[i], " end: ", ending_node[i], " weight: ", weights[i])
#     G.add_edge(starting_node[i], ending_node[i], weight=weights[i])
#
# print(G.edges)
#
#
# pos = nx.spring_layout(G)
# # nodes
# nx.draw_networkx_nodes(G, pos, node_size=700)
#
# # edges
# nx.draw_networkx_edges(G, pos,
#                        width=6)
# nx.draw_networkx_edges(G, pos,
#                        width=6, alpha=0.5, edge_color='b', style='dashed')
#
# # labels
# nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
#
# plt.axis('off')
# # plt.show()
#
#
# # nx.draw(G, with_labels=True)
# # plt.show()
#
#
# print(nx.dijkstra_path(G, 'A', 'F', weight='weight'))
