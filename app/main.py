class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for individ in people:
        person_list.append(Person(individ["name"], individ["age"]))

        if individ.get("wife") in Person.people:
            wife = individ["wife"]
            Person.people[individ["name"]].wife = Person.people[wife]
            Person.people[wife].husband = Person.people[individ["name"]]

    return person_list
