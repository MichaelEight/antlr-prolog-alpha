# Mini Interpreter Prologu

## Instalacja

1. Upewnij się, że masz zainstalowanego Pythona w wersji 3.10 lub nowszej.
2. Zainstaluj wymagane zależności, uruchamiając:
   ```bash
   pip install antlr4-python3-runtime
   ```

## Jak uruchomić

1. Sklonuj lub pobierz to repozytorium.
2. Przejdź do katalogu projektu.
3. Uruchom interpreter za pomocą:
   ```bash
   python prolog_runner.py
   ```

## Skróty klawiszowe

- **F**: Wybierz panel Faktów  
- **R**: Wybierz panel Reguł  
- **Q**: Wybierz panel Zapytania  
- **A**: Dodaj nowy fakt/regułę lub zadaj zapytanie (ustawia fokus na polu wejściowym)  
- **E**: Edytuj wybrany fakt/regułę  
- **D**: Usuń wybrany fakt/regułę  
- **ESC**: Wyjdź z trybu edycji lub odznacz wszystkie panele  
- **Ctrl+S**: Zapisz fakty i reguły do pliku `.xd`  
- **Ctrl+L**: Wczytaj fakty i reguły z pliku `.xd`  
- **Strzałka w górę/dół**: Nawiguj po historii zapytań w panelu Zapytania  

## Poprawna składnia danych wejściowych

### Fakty
- Format: `predykat(arg1, arg2, ...)`
- Przykład: `parent(john, mary)`

### Reguły
- Format: `nagłówek(arg1, arg2, ...) :- nazwa1(arg1, arg2, ...), nazwa2(arg1, arg2, ...)`
- Przykład: `grandparent(X, Y) :- parent(X, Z), parent(Z, Y)`

### Zapytania
- Format: `predykat(arg1, arg2, ...)`
- Przykład: `parent(X, mary)`

### Uwagi
- Nie dodawaj kropki (`.`) na końcu — interfejs graficzny zrobi to automatycznie.
- Używaj zmiennych (np. `X`, `Y`) w zapytaniach i regułach oraz stałych (np. `john`, `mary`) w faktach.

## Funkcje

- Dodawanie, edycja i usuwanie faktów oraz reguł.
- Interaktywny system zapytań do bazy wiedzy.
- Możliwość zapisu i wczytywania faktów oraz reguł z/do plików `.xd`.
- Skróty klawiszowe dla sprawnej nawigacji i działania.
- Nawigacja po historii zapytań za pomocą klawiszy strzałek.