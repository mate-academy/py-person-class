class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    return_list = []
    for person in people:
        # creating extra variable to make the code easier
        human = Person(person["name"], person["age"])
        return_list.append(human)

    for person in people:
        if "wife" in person.keys() and person["wife"] is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif "husband" in person.keys() and person["husband"] is not None:
            Person.people[person["name"]].husband \
                = Person.people[person["husband"]]

    return return_list
