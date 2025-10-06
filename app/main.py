class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Primeiro, criar todas as instâncias de Person
    for person_dict in people:
        Person(person_dict["name"], person_dict["age"])

    # Depois, estabelecer as relações wife/husband
    for person_dict in people:
        person_instance = Person.people[person_dict["name"]]

        if "wife" in person_dict and person_dict["wife"] is not None:
            person_instance.wife = Person.people[person_dict["wife"]]

        if "husband" in person_dict and person_dict["husband"] is not None:
            person_instance.husband = Person.people[person_dict["husband"]]

    # Retornar lista de instâncias na mesma ordem
    return [Person.people[person_dict["name"]] for person_dict in people]
