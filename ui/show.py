from model.logic import Logic
import tkinter as tk
from tkinter import messagebox

logic = Logic()

class Tkinter():
    def __init__(self):
        self.logic = Logic()
        self.array = []
        self.init_ui()

    def init_ui(self):
        self.root = tk.Tk()
        self.root.title("Minimum Row Cover Problem")

        self.label = tk.Label(self.root, text="Enter matrix size:")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.generate_button = tk.Button(self.root, text="Generate Matrix", command=self.on_generate)
        self.generate_button.pack()

        self.run_button = tk.Button(self.root, text="Run Algorithm", command=self.run_algorithm)
        self.run_button.pack()

        self.matrix_display = tk.Text(self.root, height=15, width=50, state="disabled")
        self.matrix_display.pack()

        self.root.mainloop()

    def on_generate(self):
        try:
            size = int(self.entry.get())
            if not (1 <= size <= 12):
                raise ValueError("Size must be an integer between 1 and 12.")
            self.array = self.logic.generate_random_matrix(size)
            self.display_matrix(self.array)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def display_matrix(self, matrix):
        self.matrix_display.config(state="normal")
        self.matrix_display.delete('1.0', tk.END)
        for row in matrix:
            self.matrix_display.insert(tk.END, ' '.join(map(str, row)) + '\n')
        self.matrix_display.config(state="disabled")

    def run_algorithm(self):
        if not self.array:
            messagebox.showerror("Error", "Matrix is not generated yet.")
            return

        solution = self.logic.min_row_cover(self.array)
        self.display_result(solution)

    def display_result(self, solution):
        # Создаем строку для отображения матрицы
        result = "Minimal Row Cover Solution:\n\n"

        for i, row in enumerate(self.array):
            if i in solution:  # Если строка входит в минимальное покрытие
                result += ">>   " + "  ".join(map(str, row)) + "   <<\n"
            else:
                result += "     " + "  ".join(map(str, row)) + "\n"

        # Добавляем список строк, которые входят в покрытие
        result += "\nSelected rows (indices): " + ", ".join(map(str, solution))

        # Отображаем результат в messagebox
        messagebox.showinfo("Solution", result)
