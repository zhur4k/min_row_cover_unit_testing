from graphviz import Digraph

def generate_graph():
    dot = Digraph()

    # Для test_generate_random_matrix_values
    dot.node('A', 'Start')
    dot.node('B', 'for row in matrix')
    dot.node('C', 'for value in row')
    dot.node('D', 'assertIn(value, [0, 1])')
    dot.node('E', 'End')

    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'C')
    dot.edge('C', 'E')

    dot.render('test_generate_random_matrix_values', format='png', cleanup=False)

generate_graph()
