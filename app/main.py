class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    for i in people:
        person_obj = Person.people[i["name"]]

        if "wife" in i and i["wife"] is not None:
            person_obj.wife = Person.people[i["wife"]]

        if "husband" in i and i["husband"] is not None:
            person_obj.husband = Person.people[i["husband"]]

    return list(Person.people.values())
