import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.stats import kurtosis
import numpy as np
from scipy.signal import savgol_filter, argrelextrema

class TurningPointAnalyzerApp:
    def __init__(self, root):
        self.root = root
        root.title("Turning Point Analyzer")

        # Utworzenie zmiennych kontrolnych
        self.data_size_var = tk.StringVar(value="1000")
        self.window_size_var = tk.StringVar(value="50")
        self.poly_order_var = tk.StringVar(value="3")
        self.plot_type_var = tk.StringVar(value="Kurtoza")

        # Utworzenie atrybutu przechowującego globalny punkt przegięcia
        self.global_turning_point = None

        # Atrybut do przechowywania aktualnego zakresu osi x
        self.current_xlim = None

        # Atrybut przechowujący wczytane dane z pliku
        self.loaded_data = None

        # Utworzenie etykiet
        ttk.Label(root, text="Ilość danych:").grid(column=0, row=0, padx=10, pady=10)
        ttk.Label(root, text="Rozmiar okna:").grid(column=0, row=1, padx=10, pady=10)
        ttk.Label(root, text="Stopień wielomianu:").grid(column=0, row=2, padx=10, pady=10)
        ttk.Label(root, text="Rodzaj wykresu:").grid(column=0, row=3, padx=10, pady=10)

        # Utworzenie pól wprowadzania tekstu
        ttk.Entry(root, textvariable=self.data_size_var).grid(column=1, row=0, padx=10, pady=10)
        ttk.Entry(root, textvariable=self.window_size_var).grid(column=1, row=1, padx=10, pady=10)
        ttk.Entry(root, textvariable=self.poly_order_var).grid(column=1, row=2, padx=10, pady=10)

        # Utworzenie rozwijanej listy wyboru rodzaju wykresu
        ttk.Combobox(root, textvariable=self.plot_type_var, values=["Kurtoza", "Odcylenie Standardowe"]).grid(column=1, row=3, padx=10, pady=10)

        # Utworzenie przycisku do uruchamiania analizy
        ttk.Button(root, text="Uruchom Analizę", command=self.run_analysis).grid(column=0, row=4, columnspan=2, pady=10)

        # Utworzenie przycisku do wczytywania danych z pliku
        ttk.Button(root, text="Wczytaj dane z pliku", command=self.load_data_from_file).grid(column=0, row=5, columnspan=2, pady=10)

        # Utworzenie obszaru rysowania wykresu
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.plot_area = self.figure.add_subplot(1, 1, 1)
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().grid(column=0, row=6, columnspan=2, pady=10)

        # Utworzenie przycisków do nawigacji po wykresie
        ttk.Button(root, text="Lewo", command=self.move_left).grid(column=0, row=7, pady=10)
        ttk.Button(root, text="Prawo", command=self.move_right).grid(column=1, row=7, pady=10)

        # Utworzenie przycisku do powiększania wykresu
        ttk.Button(root, text="Powiększ Wykres", command=self.zoom_plot).grid(column=0, row=8, pady=10)

        # Utworzenie przycisku do zmniejszania wykresu
        ttk.Button(root, text="Zmniejsz Wykres", command=self.reset_plot).grid(column=1, row=8, pady=10)

        # Utworzenie przycisku do wyśrodkowania wykresu na globalnym punkcie przegięcia
        ttk.Button(root, text="Wyśrodkuj", command=self.center_plot).grid(column=0, row=9, columnspan=2, pady=10)

        # Przypisanie funkcji do aktualizacji wykresu po zmianie rozmiaru okna
        self.root.bind("<Configure>", self.on_window_resize)

    def run_analysis(self):
        try:
            # Pobranie parametrów z pól wprowadzania tekstu
            window_size = int(self.window_size_var.get())
            poly_order = int(self.poly_order_var.get())
            plot_type = self.plot_type_var.get()

            # Sprawdzenie, czy wczytano dane z pliku
            if self.loaded_data is None:
                raise ValueError("Wczytaj dane z pliku przed uruchomieniem analizy.")

            # Jeśli wczytano mniej danych niż określono w polu "Ilość danych", dostosuj ilość danych wejściowych
            data_size = min(int(self.data_size_var.get()), len(self.loaded_data))

            # Obliczanie kurtozy lub odchylenia standardowego dla kolejnych fragmentów danych
            if plot_type == "Kurtoza":
                plot_data = [kurtosis(self.loaded_data[i:i+window_size]) for i in range(data_size-window_size+1)]
            elif plot_type == "Odcylenie Standardowe":
                plot_data = [np.std(self.loaded_data[i:i+window_size]) for i in range(data_size-window_size+1)]

            # Wygładzanie krzywej filtrem Savitzky-Golay
            smoothed_data = savgol_filter(plot_data, window_size, poly_order)

            # Znajdowanie punktów przegięcia (maksimów i minimów lokalnych) na wygładzonej krzywej
            extrema_min_indices = argrelextrema(smoothed_data, np.less)[0]
            extrema_max_indices = argrelextrema(smoothed_data, np.greater)[0]

            # Znajdowanie globalnych punktów przegięcia
            all_extrema_indices = np.concatenate([extrema_min_indices, extrema_max_indices])
            self.global_turning_point = max(all_extrema_indices, key=lambda idx: smoothed_data[idx])

            # Wyświetlenie wyników w oknie komunikatu
            result_message = f'Globalny punkt przegięcia {plot_type.lower()}: {self.global_turning_point}'
            messagebox.showinfo("Wyniki Analizy", result_message)

            # Ustawienie aktualnego zakresu osi x na cały zakres
            self.current_xlim = (0, len(plot_data))

            # Rysowanie wykresu
            self.plot_area.clear()
            self.plot_area.plot(range(len(plot_data)), plot_data, label=plot_type)
            self.plot_area.plot(range(len(smoothed_data)), smoothed_data, label=f'Wygładzona {plot_type.lower()}', linestyle='--')
            self.plot_area.scatter(extrema_min_indices, np.array(smoothed_data)[extrema_min_indices], c='blue', marker='o', label='Minima lokalne')
            self.plot_area.scatter(extrema_max_indices, np.array(smoothed_data)[extrema_max_indices], c='red', marker='o', label='Maksima lokalne')
            self.plot_area.scatter([self.global_turning_point], [smoothed_data[self.global_turning_point]], c='green', marker='o', label=f'Globalny punkt przegięcia {plot_type.lower()}')
            self.plot_area.legend()
            self.plot_area.set_xlim(self.current_xlim)
            self.canvas.draw()

        except ValueError as ve:
            messagebox.showerror("Błąd", str(ve))
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił nieznany błąd: {str(e)}")

    def load_data_from_file(self):
        # Funkcja do wczytywania danych z pliku
        file_path = filedialog.askopenfilename(title="Wybierz plik z danymi", filetypes=[("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")])
        if file_path:
            try:
                # Wczytywanie danych z pliku
                self.loaded_data = np.loadtxt(file_path)

                # Aktualizacja danych na wykresie
                self.plot_area.clear()
                self.plot_area.plot(self.loaded_data, label="Dane z pliku")
                self.plot_area.legend()
                self.current_xlim = (0, len(self.loaded_data))
                self.plot_area.set_xlim(self.current_xlim)
                self.canvas.draw()

                # Zresetowanie globalnego punktu przegięcia
                self.global_turning_point = None

                # Automatyczne uruchamianie analizy po wczytaniu danych z pliku
                self.run_analysis()

                messagebox.showinfo("Sukces", "Dane zostały wczytane z pliku.")

            except Exception as e:
                messagebox.showerror("Błąd", f"Wystąpił błąd podczas wczytywania danych z pliku: {str(e)}")

    def move_left(self):
        # Przesuwanie wykresu w lewo
        if self.current_xlim is not None:
            step = int((self.current_xlim[1] - self.current_xlim[0]) * 0.1)
            new_xlim = (max(0, self.current_xlim[0] - step), max(step, self.current_xlim[1] - step))
            self.current_xlim = new_xlim
            self.plot_area.set_xlim(new_xlim)
            self.canvas.draw()

    def move_right(self):
        # Przesuwanie wykresu w prawo
        if self.current_xlim is not None:
            step = int((self.current_xlim[1] - self.current_xlim[0]) * 0.1)
            new_xlim = (self.current_xlim[0] + step, self.current_xlim[1] + step)
            self.current_xlim = new_xlim
            self.plot_area.set_xlim(new_xlim)
            self.canvas.draw()

    def zoom_plot(self):
        # Powiększanie wykresu
        if self.global_turning_point is not None:
            self.current_xlim = (self.global_turning_point - 50, self.global_turning_point + 50)
            self.plot_area.set_xlim(self.current_xlim)
            self.canvas.draw()

    def reset_plot(self):
        # Funkcja do zmniejszania wykresu do pierwotnego zakresu
        if self.current_xlim is not None:
            step = int(self.data_size_var.get())
            new_xlim = (0, len(self.loaded_data))
            self.current_xlim = new_xlim
            self.plot_area.set_xlim(new_xlim)
            self.canvas.draw()

    def center_plot(self):
        # Wyśrodkowanie wykresu na globalnym punkcie przegięcia
        if self.global_turning_point is not None:
            half_width = int((self.current_xlim[1] - self.current_xlim[0]) / 2)
            new_xlim = (self.global_turning_point - half_width, self.global_turning_point + half_width)
            self.current_xlim = new_xlim
            self.plot_area.set_xlim(new_xlim)
            self.canvas.draw()

    def on_window_resize(self, event):
        # Funkcja do obsługi zmiany rozmiaru okna
        self.canvas.draw()

# Uruchomienie aplikacji
root = tk.Tk()
app = TurningPointAnalyzerApp(root)
root.mainloop()
