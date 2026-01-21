class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for current_person in people:
        name = current_person["name"]
        age = current_person["age"]
        people_list.append(Person(name, age))

    for current_person in people:
        if "wife" in current_person:
            if current_person["wife"] is not None:
                Person.people[current_person["name"]].wife \
                    = Person.people.get(current_person["wife"])
        if "husband" in current_person:
            if current_person["husband"] is not None:
                Person.people[current_person["name"]].husband \
                    = Person.people.get(current_person["husband"])

    return people_list
