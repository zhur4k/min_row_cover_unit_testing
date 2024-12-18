import unittest
from model.logic import Logic  # Импортируем ваш класс Logic


class TestLogic(unittest.TestCase):

    def setUp(self):
        self.logic = Logic()

    def test_generate_random_matrix_values(self):
        # Проверка, что элементы матрицы принимают только значения 0 или 1
        size = 3
        matrix = self.logic.generate_random_matrix(size)
        for row in matrix:
            for value in row:
                self.assertIn(value, [0, 1])  # Элементы должны быть 0 или 1

    

    def test_min_row_cover_complex_case(self):
        # Более сложный случай
        matrix = [[1, 0, 1, 0],
                  [0, 1, 0, 1],
                  [1, 1, 0, 0],
                  [0, 0, 1, 1]]
        result = self.logic.min_row_cover(matrix)
        self.assertTrue(is_valid_cover(matrix, result))


# Вспомогательная функция для проверки валидности покрытия
def is_valid_cover(matrix, rows):
    covered_columns = set()
    for row in rows:
        for j, val in enumerate(matrix[row]):
            if val == 1:
                covered_columns.add(j)
    return len(covered_columns) == len(matrix[0]) if matrix else True


if __name__ == "__main__":
    unittest.main()
    