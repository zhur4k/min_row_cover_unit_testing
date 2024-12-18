import random

class Logic():

    def generate_random_matrix(self, size):
        # Генерация случайной матрицы размера size x size
        matrix = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(random.randint(0, 1))  # Генерация случайных значений 0 или 1
            matrix.append(row)
        return matrix

    def min_row_cover(self, matrix):
        def helper(matrix, covered_cols):
            # Проверка на пустую матрицу
            if not matrix:  
                return []

            # Если все столбцы покрыты, возвращаем пустой список
            if all(c in covered_cols for c in range(len(matrix[0]))):
                return []

            # Поиск строки, которая покрывает наибольшее количество еще не покрытых столбцов
            best_row = None
            best_cover_count = -1
            for i, row in enumerate(matrix):
                cover_count = sum(1 for j in range(len(row)) if row[j] == 1 and j not in covered_cols)
                if cover_count > best_cover_count:
                    best_row = i
                    best_cover_count = cover_count

            # Если ни одна строка не покрывает новые столбцы, завершаем
            if best_row is None or best_cover_count == 0:
                return []

            # Добавляем эту строку в список покрытия
            new_covered_cols = covered_cols.copy()
            for j in range(len(matrix[best_row])):
                if matrix[best_row][j] == 1:
                    new_covered_cols.add(j)

            # Рекурсивно находим минимальное покрытие для оставшихся столбцов
            rest_solution = helper(matrix, new_covered_cols)
            return [best_row] + rest_solution

        return helper(matrix, set())
    