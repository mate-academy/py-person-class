class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for person in people:
        result_list.append(Person(person["name"], person["age"]))
    for person in people:
        if "wife" in person.keys() and person["wife"]:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif "husband" in person.keys() and person["husband"]:
            Person.people[
                person["name"]
            ].husband = Person.people[
                person["husband"]
            ]

    return result_list
