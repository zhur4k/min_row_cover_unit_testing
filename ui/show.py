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
    # Инициализация переменной result как строки
        result = "Minimal Row Cover Solution (row indices):\n"
        
        # Преобразуем элементы solution в строки и объединяем их через запятую
        result += ", ".join([str(sol) for sol in solution])  # Преобразуем индексы в строку с разделением запятыми
        
        # Выводим сообщение в окно с помощью messagebox
        messagebox.showinfo("Solution", result)
