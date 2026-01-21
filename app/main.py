class Person:
    people = {}
    # Klasa Person:
    # Ma przechowywać informacje o osobie (imię i wiek)
    # Powinna mieć atrybut klasowy people, który jest
    # słownikiem mapującym imiona na odpowiadające im instancje klasy
    # Atrybuty instancji:
    # Podstawowe: name i age (ustawiane w __init__)
    # Opcjonalne: wife lub husband (w zależności
    # od płci - to wynika z danych wejściowych)
    # Te opcjonalne atrybuty powinny być
    # referencjami do innych obiektów Person

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    Person.people = {}

    for person in people:
        Person(name=person["name"], age=person["age"])

    for person_data in people:
        person = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"] in Person.people:
            person.wife = Person.people[person_data["wife"]]

        elif ("husband" in person_data
              and person_data["husband"] in Person.people):
            person.husband = Person.people[person_data["husband"]]

    # for person in people:
    #     current_person = Person.people[person["name"]]
    #
    #     if "wife" in person and person["wife"] in Person.people:
    #         wife = Person.people[person["wife"]]
    #         current_person.wife = wife
    #         wife.husband = current_person
    #
    #     elif "husband" in person and person["husband"] in Person.people:
    #         husband = Person.people[person["husband"]]
    #         current_person.husband = husband
    #         husband.wife = current_person

    return list(Person.people.values())

# To zadanie polega na stworzeniu klasy
# Person i funkcji create_person_list,
# która przekształca listę słowników opisujących
# osoby w listę instancji tej klasy. Oto kluczowe elementy zadania:

# Funkcja create_person_list:
# Przetwarza listę słowników na listę obiektów Person
# Musi prawidłowo ustawiać relacje małżeńskie
# (wife/husband) między obiektami
# Relacje powinny być ustawiane jako bezpośrednie
# referencje do obiektów, nie jako stringi
# Ważne szczegóły:
# Każda osoba ma unikalne imię
# Relacje są dwustronne (jeśli Ross ma żonę Rachel,
# to Rachel powinna mieć męża Rossa)
# Atrybut wife/husband powinien istnieć tylko
# jeśli dana osoba jest w związku
# Słownik Person.people ma pozwalać na szybkie
# wyszukiwanie osób po imieniu
# Przykład pokazuje:
# Jak powinny wyglądać poprawne referencje między obiektami
# Jak sprawdzać poprawność implementacji
# Że relacje powinny być obustronne i spójne
# Zadanie testuje:
#
# Umiejętność pracy z klasami w Pythonie
# Zarządzanie referencjami między obiektami
# Prawidłowe użycie atrybutów klasowych i instancyjnych
# Logikę przetwarzania danych wejściowych
# Kluczowa trudność polega na prawidłowym ustawieniu
# wzajemnych referencji między obiektami, tak
# aby relacje małżeńskie były spójne i obustronne.
