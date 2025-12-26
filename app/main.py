class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    lista_people = []

    for person_ in people:
        Person(person_["name"], person_["age"])

    for person in people:
        if "wife" in person and person["wife"]:
            Person.people[person["name"]].wife = Person.people[person["wife"]]

        if "husband" in person and person["husband"]:
            person_ = Person.people[person["name"]]
            person_.husband = Person.people[person["husband"]]

        lista_people.append(Person.people[person["name"]])

    return lista_people
