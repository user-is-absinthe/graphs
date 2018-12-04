import sys
import random

import read_from_csv as csv

import networkx
import matplotlib.pyplot


def main():
    matrix_str = csv.open_matrix('data.txt')

    if not csv.good_matrix(matrix_str):
        print('Bad matrix.')
        sys.exit(1)

    print(matrix_str)

    graph = create_graph(matrix_str)
    # print(graph.edges)
    draw_graph(graph)

    # new_graph = networkx.algorithms.coloring.greedy_color(graph)
    # print(new_graph)

    chromatic_number, colors = find_colors(graph)

    draw_graph(graph, colors=colors)

    pass


def find_colors(graph):
    colors_dict = networkx.algorithms.coloring.greedy_color(graph)
    # keys = colors_dict.keys()
    color_scheme = colors_dict.values()
    color_scheme = list(set(color_scheme))
    for index in range(len(color_scheme)):
        color_scheme[index] = (random.random(), random.random(), random.random())
    colors = list()
    for node in graph.node:
        colors.append(color_scheme[colors_dict[node]])

    return len(color_scheme), colors


def create_graph(matrix_str):
    graph = networkx.Graph()
    graph.add_nodes_from([i for i in range(len(matrix_str))])
    for index_line in range(len(matrix_str)):
        for index_number in range(len(matrix_str[index_line])):
            if matrix_str[index_line][index_number] == '1':
                graph.add_edge(index_line, index_number)
    return graph


def draw_graph(graph, path_to_save=None, colors=None):
    if colors is None:
        networkx.draw(graph)
    else:
        networkx.draw(graph, node_color=colors)
    if path_to_save is not None:
        matplotlib.pyplot.savefig(path_to_save)
    matplotlib.pyplot.show()
    pass


if __name__ == '__main__':
    main()
