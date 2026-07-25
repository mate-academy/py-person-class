class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    instances = []
    for person in people:
        instances.append(Person(person["name"], person["age"]))

    for person in people:
        # Verifica se a chave existe.
        # Se não existir, a segunda parte nem é executada.
        if "wife" in person and person["wife"] is not None:
            name = person["name"]
            wife = person["wife"]
            Person.people[name].wife = Person.people[wife]
        # Verifica se a chave existe.
        # Se não existir, a segunda parte nem é executada.
        elif "husband" in person and person["husband"] is not None:
            name = person["name"]
            husband = person["husband"]
            Person.people[name].husband = Person.people[husband]
    return instances
