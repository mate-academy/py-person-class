class Person:
    # atributo de classe para armazenar todas as instâncias
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # adiciona a instância ao dicionário de pessoas
        Person.people[name] = self


def create_person_list(people_dicts: list[dict]) -> list[Person]:
    # cria todas as instâncias com list comprehension
    person_list = [Person(person_dict["name"], person_dict["age"])
                   for person_dict in people_dicts]

    # conecta marido/esposa usando .get()
    for person_dict in people_dicts:
        person = Person.people[person_dict["name"]]
        if person_dict.get("wife"):
            person.wife = Person.people[person_dict["wife"]]
        if person_dict.get("husband"):
            person.husband = Person.people[person_dict["husband"]]

    return person_list
