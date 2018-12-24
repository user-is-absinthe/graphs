import func_true_chromatic
import func_read_from_csv as csv
import time
import numpy


TEMP_MATRIX = 'temp_matrix.txt'

ALL_START_TIME = time.time()


def to_csv(info):
    with open('otchet.csv', 'a') as file:
        file.write(str(info) + '\n')


for i in range(1, 100):
    avg_list = list()
    for test in range(10):
        once_start_time = time.time()
        func_true_chromatic.generate_matrix_in(i, TEMP_MATRIX)

        matrix_str = csv.open_matrix('../data/true_chromatic/temp_matrix.txt')

        graph = func_true_chromatic.create_graph(matrix_str)

        chromatic_number, colors = func_true_chromatic.find_colors(graph)

        once_end_time = time.time() - once_start_time

        # to_csv(once_end_time)
        avg_list.append(once_end_time)

    avg_print = numpy.mean(avg_list)
    print(i, avg_print)
    to_csv(str(avg_print) + ',avg time')

all_end_time = time.time() - ALL_START_TIME
to_csv(str(all_end_time) + ',all time')


