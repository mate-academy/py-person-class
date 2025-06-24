class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # wife/husband attributes will be added dynamically later
        Person.people[name] = self


def create_person_list(people_data: list[dict]) -> list[Person]:
    # Limpa o dicionário para evitar dados persistentes entre chamadas
    Person.people.clear()

    # Fase 1: Criação das instâncias
    person_list = []
    for person_dict in people_data:
        person = Person(person_dict["name"], person_dict["age"])
        person_list.append(person)

    # Fase 2: Atribuição de relacionamentos
    for person_dict in people_data:
        current = Person.people[person_dict["name"]]

        if "wife" in person_dict and person_dict["wife"] is not None:
            current.wife = Person.people[person_dict["wife"]]

        if "husband" in person_dict and person_dict["husband"] is not None:
            current.husband = Person.people[person_dict["husband"]]

    return person_list
