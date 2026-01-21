class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Limpa o dicionário para evitar acúmulo entre execuções
    Person.people.clear()

    for peo in people:
        Person(peo["name"], peo["age"])

    for peo in people:
        person = Person.people[peo["name"]]
        if "wife" in peo and peo["wife"] is not None:
            person.wife = Person.people[peo["wife"]]
        if "husband" in peo and peo["husband"] is not None:
            person.husband = Person.people[peo["husband"]]

    return list(Person.people.values())
