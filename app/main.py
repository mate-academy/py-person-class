class Person:
    people = {}  # Dicionário de classe para add as instancias

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # insere a pessoa no dicionário de classe
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Cria as instancias sem relacionar ainda
    person_list = []
    for human in people:
        person = Person(human["name"], human["age"])
        person_list.append(person)

    # Depois adiciona os relacionamentos (wife / husband)
    for human in people:
        current_person = Person.people[human["name"]]

        if "wife" in human and human["wife"] is not None:
            current_person.wife = Person.people[human["wife"]]
        elif "husband" in human and human["husband"] is not None:
            current_person.husband = Person.people[human["husband"]]

    return person_list
