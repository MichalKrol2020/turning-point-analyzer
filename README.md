1\. Wstęp teoretyczny
=====================

Analiza matematyczna odgrywa kluczową rolę w przetwarzaniu danych i rozumieniu ich właściwości. W ramach tej dziedziny matematyki wiele technik jest używanych do analizy szeregów czasowych, w tym szeregów finansowych, danych naukowych czy sygnałów. Jednym z ważnych aspektów analizy jest identyfikacja punktów przegięcia w danych, co może wskazywać na istotne zmiany w ich przebiegu.

W tym projekcie zostanie przedstawione narzędzie do analizy punktów przegięcia na wykresie kurtozy lub odchylenia standardowego. Kurtoza mierzy "grupowanie" danych wokół średniej, co pozwala na ocenę "ostrości" rozkładu. Z kolei odchylenie standardowe mierzy, jak bardzo wartości są rozproszone wokół średniej. Oba te parametry są użyteczne w analizie danych, a ich zmiany mogą wskazywać na istotne punkty przegięcia.

1.1. Wykorzystanie Języka Python w Analizie Matematycznej
---------------------------------------------------------

Python jest jednym z najczęściej używanych języków programowania w dziedzinie analizy danych i matematyki. Istnieje wiele bibliotek i narzędzi, które ułatwiają pracę z danymi numerycznymi oraz tworzenie zaawansowanych wykresów. W tym projekcie wykorzystano kilka kluczowych bibliotek:

### NumPy

NumPy to biblioteka do obliczeń numerycznych w Pythonie. Posiada efektywne struktury danych do przechowywania danych numerycznych oraz funkcje umożliwiające efektywne operacje na tych danych.

### SciPy

SciPy to biblioteka rozwinięta na bazie NumPy, oferująca dodatkowe funkcje do naukowych obliczeń, w tym statystyki, optymalizację, przetwarzanie sygnałów czy algorytmy numeryczne.

### Matplotlib

Matplotlib to narzędzie do tworzenia wykresów w języku Python. Jest szeroko używane w analizie danych i naukowych projektach do wizualizacji wyników.

### Tkinter

Tkinter to biblioteka standardowa do tworzenia interfejsu graficznego w Pythonie. W tym projekcie została użyta do stworzenia prostego interfejsu użytkownika.

### Inne Biblioteki

Dodatkowo, w projekcie wykorzystano funkcje związane z analizą matematyczną, takie jak filtrowanie Savitzky-Golay czy znajdowanie ekstremów lokalnych, dostępne w bibliotece SciPy.

Wszystkie te narzędzia w połączeniu umożliwiają efektywną analizę matematyczną, w tym identyfikację punktów przegięcia na wykresach, co jest istotne w kontekście analizy danych numerycznych.

1.2. Filtr Savitzky-Golay
-------------------------

Filtr Savitzky-Golay to technika wygładzania sygnałów numerycznych, używana do redukcji szumów i wyrównywania krzywych. Jest szczególnie przydatna w przypadku danych eksperymentalnych, gdzie występuje szum i nieregularności.

### Jak Działa Filtr Savitzky-Golay?

Filtr Savitzky-Golay opiera się na lokalnym dopasowaniu wielomianu do punktów danych w oknie czasowym. Następnie, dla każdego punktu, wartość wielomianu jest używana jako nowa wartość wygładzona. W rezultacie, punkty odstające lub szumy są łatwiej wyłapywane i eliminowane, a krzywe stają się bardziej gładkie.

### Parametry Filtra

1.  **Okno Czasowe (Window Size):** Określa ilość punktów danych branych pod uwagę przy dopasowywaniu wielomianu. Większe okno czasowe oznacza bardziej wygładzoną krzywą, ale może prowadzić do utraty szczegółów.

2.  **Stopień Wielomianu (Polynomial Order):** Określa stopień wielomianu używanego do dopasowania. Większy stopień wielomianu może lepiej dopasować bardziej skomplikowane krzywe, ale może też prowadzić do nadmiernego dopasowania (overfitting).

### Implementacja w Projekcie

W projekcie wykorzystano funkcję `savgol_filter` z biblioteki SciPy, która implementuje filtr Savitzky-Golay. Parametry takie jak okno czasowe i stopień wielomianu są ustalane przez użytkownika w interfejsie aplikacji.

2\. Tworzenie Aplikacji Desktopowej w Pythonie z Użyciem Tkinter
================================================================

### Tkinter - Podstawowe Informacje

Tkinter to biblioteka do tworzenia interfejsów graficznych (GUI) w języku Python. Jest częścią standardowej biblioteki Pythona, co oznacza, że nie wymaga dodatkowej instalacji. Tkinter umożliwia tworzenie okien, przycisków, etykiet, pól tekstowych i innych elementów interfejsu graficznego.

### Krok 1: Importowanie Tkinter

W pierwszym kroku importujemy moduł Tkinter oraz niektóre z jego submodułów, które będziemy używać do tworzenia interfejsu graficznego.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_14128c7f4e2495a1.gif)

### Krok 2: Inicjalizacja Okna Aplikacji

Następnie inicjalizujemy główne okno aplikacji. Nadajemy mu tytuł za pomocą metody `title`.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_42ffa8bf39b5fa40.gif)

### Krok 3: Dodanie Elementów Interfejsu Graficznego

W tym kroku dodajemy elementy interfejsu graficznego, takie jak przyciski, etykiety, pola tekstowe itp. Możemy używać modułu `ttk`, który dostarcza zaawansowane kontrolki.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_a10eb5950a7c651e.gif)

### Krok 4: Zdefiniowanie Funkcji Obsługującej Zdarzenia

Definiujemy funkcje, które zostaną wywołane po wystąpieniu określonych zdarzeń, takich jak kliknięcie przycisku. Te funkcje będą zawierać kod obsługujący te zdarzenia.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_9d4c8934a5ae1677.gif)

### Krok 5: Uruchomienie Pętli Głównej

Uruchamiamy pętlę główną aplikacji. Ta pętla sprawia, że aplikacja pozostaje otwarta i reaguje na interakcje użytkownika.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_a000a3133ff1a7f0.gif)

### Krok 6: Komunikacja z Kodem Analizy

Aby zintegrować aplikację z kodem analizy punktów przegięcia, musimy skorzystać z odpowiednich funkcji w odpowiednich miejscach. Możemy użyć funkcji obsługujących zdarzenia, takich jak kliknięcie przycisku, wczytywanie danych z pliku itp.

3\. Analiza Punktów Przegięcia w Pythonie z Użyciem SciPy
---------------------------------------------------------

### Krok 1: Importowanie Niezbędnych Bibliotek

W pierwszym kroku importujemy niezbędne biblioteki, takie jak NumPy do manipulacji danymi numerycznymi oraz funkcje z biblioteki SciPy do analizy matematycznej.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_fa72830c9c5396b3.gif)

### Krok 2: Pobranie Parametrów z Pól Wprowadzania Tekstu

W pierwszym kroku funkcja pobiera parametry analizy z pól wprowadzania tekstu. Korzysta z zmiennych przechowujących wartości z pól wprowadzania tekstu, takich jak `window_size_var`, `poly_order_var` i `plot_type_var`. Wartości te reprezentują okno czasowe, stopień wielomianu i typ analizy.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_1575ae36df0b1a9a.gif)

### Krok 3: Sprawdzenie Poprawności Danych

Funkcja sprawdza, czy wczytano dane z pliku przed rozpoczęciem analizy. Jeśli dane nie są wczytane, wyrzuca błąd.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_36546dec8e4f983.gif)

### Krok 4: Obliczanie Kurtozy lub Odchylenia Standardowego dla Kolejnych Fragmentów Danych

Na podstawie wczytanych danych i parametrów analizy obliczane są wartości kurtozy lub odchylenia standardowego dla kolejnych fragmentów danych.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_9f42ef624edf7636.gif)

### Krok 5: Wygładzanie Krzywej Filtrem Savitzky-Golay

Krzywa danych jest następnie wygładzana filtrem Savitzky-Golay za pomocą funkcji `savgol_filter`.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_ee0a42731a07437c.gif)

### Krok 6: Znajdowanie Punktów Przegięcia na Wygładzonej Krzywej

Funkcja używa funkcji `argrelextrema` z biblioteki SciPy do znalezienia punktów przegięcia (maksimów i minimów lokalnych) na wygładzonej krzywej.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_a8874e72f6c2b68b.gif)

### Krok 7: Znajdowanie Globalnych Punktów Przegięcia

Na podstawie lokalnych punktów przegięcia funkcja znajduje globalny punkt przegięcia, który odpowiada maksymalnej wartości na wygładzonej krzywej.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_60c951e14e6c3634.gif)

### Krok 8: Wyświetlenie Wyników w Oknie Komunikatu

Funkcja wyświetla wyniki analizy, w tym globalny punkt przegięcia, w oknie komunikatu za pomocą funkcji `messagebox.showinfo`.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_4b49274757055ae0.gif)

### Krok 8: Aktualizacja Wykresu

Ostatnim krokiem funkcji jest aktualizacja wykresu. W tym celu funkcja czyści obszar wykresu, dodaje nowe serie danych i aktualizuje widoczny zakres osi x.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_7ac10da0b086b8e.gif)

### Krok 9: Obsługa Błędów

Funkcja obsługuje błędy, takie jak błędy wartości czy nieznane błędy, i wyświetla komunikaty o błędach za pomocą funkcji `messagebox.showerror`.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_b818ae97e3a1d7a6.gif)

4\. Poruszanie się po wykresie
==============================

**Przesuwanie Wykresu w Lewo (**`move_left`**):**

-   Funkcja przesuwa wykres w lewo o 10% aktualnego zakresu osi x.

-   Wartość przesunięcia obliczana jest jako 10% różnicy między górnym a dolnym zakresem osi x.

-   Zakres osi x jest aktualizowany, a wykres jest przerysowywany.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_4faf9655e3e114d6.gif)

**Przesuwanie Wykresu w Prawo (**`move_right`**):**

-   Funkcja przesuwa wykres w prawo o 10% aktualnego zakresu osi x.

-   Wartość przesunięcia obliczana jest jako 10% różnicy między górnym a dolnym zakresem osi x.

-   Zakres osi x jest aktualizowany, a wykres jest przerysowywany.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_5b176d76dc774fdb.gif)

**Powiększanie Wykresu (**`zoom_plot`**):**

-   Funkcja powiększa wykres, przybliżając go do obszaru wokół globalnego punktu przegięcia.

-   Zakres osi x jest ustawiany na obszar 100 jednostek przed i po globalnym punkcie przegięcia.

-   Wykres jest przerysowywany.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_d97f06d2f4929979.gif)

**Zmniejszanie Wykresu do Pierwotnego Zakresu (**`reset_plot`**):**

-   Funkcja przywraca wykres do pierwotnego zakresu, obejmującego cały zbiór danych.

-   Zakres osi x jest ustawiany na zakres od 0 do długości załadowanych danych.

-   Wykres jest przerysowywany.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_e30c9b691af6b98a.gif)

**Wyśrodkowanie Wykresu na Globalnym Punkcie Przegięcia (**`center_plot`**):**

-   Funkcja wyśrodkowuje wykres na globalnym punkcie przegięcia.

-   Nowy zakres osi x jest ustawiany tak, aby globalny punkt przegięcia znajdował się w środku, z szerokością równą aktualnemu zakresowi.

-   Wykres jest przerysowywany.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_cddcd22f875f68c2.gif)

**Obsługa Zmiany Rozmiaru Okna (**`on_window_resize`**):**

-   Funkcja obsługuje zdarzenie zmiany rozmiaru okna aplikacji.

-   Wykres jest przerysowywany, aby dostosować się do nowego rozmiaru okna.

![](file:///C:/Users/desktop/AppData/Local/Temp/lu14348l956.tmp/lu14348l96y_tmp_b469f655af969176.gif)

Podsumowanie Projektu
---------------------

Projekt stanowi narzędzie do analizy danych numerycznych w poszukiwaniu punktów przegięcia na wykresie. Zastosowanie filtrowania Savitzky-Golay, analiza lokalnych ekstremów i interaktywne narzędzia do poruszania się po wykresie umożliwiają użytkownikowi dogłębną analizę zmian w danych.

Wnioski z projektu:

1.  **Skalowalność Analizy:** Dzięki parametrom, takim jak rozmiar okna czy stopień wielomianu, projekt umożliwia skalowanie analizy do różnych rodzajów danych.

2.  **Interaktywność:** Dodane funkcje interaktywne pozwalają użytkownikowi dostosowywać widok wykresu, co ułatwia identyfikację kluczowych punktów przegięcia.

3.  **Zastosowanie Wersji Desktopowej:** Przeniesienie funkcji analizy do aplikacji desktopowej przy użyciu Tkinter umożliwia wygodne korzystanie z narzędzia przez użytkowników.

4.  **Zastosowanie Filtracji Savitzky-Golay:** Filtr Savitzky-Golay skutecznie wygładza krzywe, ułatwiając identyfikację punktów przegięcia.

</br>

![image](https://github.com/MichalKrol2020/turning-point-analyzer/assets/106864921/7a4c2bca-d918-4480-8ba4-1d2a4848d2b8)
