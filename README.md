# Utrzymanie dokumentacji kodu źródłowego
Prezentowany projekt jest częścią mojej pracy magisterskiej: "Utrzymanie dokumentacji kodu źródłowego"

## 1. Opis projektu
Celem pracy magisterskiej było znalezienie narzędzia, które pozwala na automatyczne generowanie dokumentacji kodu źródłowego,
bez potrzeby angażowania w tym procesie programistów. W tym celu zostały dokonane badania mające za zadanie
zbadanie możliwości wykorzystania ChatGPT w tym procesie.

Z przeprowadzonych prac można stwierdzić, że ChatGPT dobrze radzi sobie z generowaniem dokumentacji kodu źródłowego
dla prostych programów napisanych w języku Python, jednak najważniejszy pozostaje dobór odpowiedniego zapytania.
Z przeprowadzonych badań wynika, że najlepsza jakościowo dokumentacji została stworzona dla zapytanie o treści: 
"Create a documentation commentary that is accurate, complete, understandable, and includes an example for the class on file: " oraz "Create documentation that is accurate, complete, understandable and includes an example for the class on file: ". Ponadto zmiany wartości parametru "temperature", nie mają znaczącego wpływu na polepszenie jakości uzyskanych odpowiedzi wygenerowanych przez ChatGPT.

## 2. Struktura projektu
* Projekt zawiera dziesięć prostych programów napisanych w języku Python, które zostały przebadane pod kontem
udokumentowania ich automatycznie przy pomocy ChatGPT. Przez to stanowią one zbiór danych testowych wraz ze sformułowanymi dziesięcioma pytaniami do ChatGPT.
Przykładowe programy zawierają się w folderze o nazwie [baza](https://github.com/leszniewskamonika/dokumentacjaKodu/tree/main/baza).

* Główny kod źródłowy programu zawiera się w pliku [turbo_prompy.py](https://github.com/leszniewskamonika/dokumentacjaKodu/blob/main/turbo_prompt.py), który zawiera 10 przykładowych pytań do ChatGPT. Odpowiedzi dla czterech ostatnich zapytań dla wszystkich przykładowych programów zostają zapisane w pliku [prompt_2.txt](https://github.com/leszniewskamonika/dokumentacjaKodu/blob/main/prompt_2.txt) podczas uruchomienia programu. Natomiast odpowiedzi do wcześniejszych zapytań zostają zapisane w pliku [prompt_1.txt](https://github.com/leszniewskamonika/dokumentacjaKodu/blob/main/prompt_1.txt) po zmianie zapisu do tego pliku w pliku głównym.
  
* Pomocniczy kod źródłowy badający możliwości wpływu doboru pamaremtru "temperature" na jakość wygenerowanej dokumentacji znajduje się w pliku [turbo_temperature.py](https://github.com/leszniewskamonika/dokumentacjaKodu/blob/main/turbo_temperature.py), gdzie odpowiedzi wygenerowane przez ChatGPT dla dwóch badanych zapytań zostają zapisane w pliku [raport.txt](https://github.com/leszniewskamonika/dokumentacjaKodu/blob/main/raport.txt).


> **ℹ️ Informacja**
> Do poprawnego działania programu potrzebne jest podanie indywidualnego klucza open api oraz instalacja openai (więcej infromacji można zaleźć w dokumentacji [API reference](https://platform.openai.com/docs/api-reference/introduction))
