class Person:

    people = {}

    def __init__(
            self,
            name: str,
            age: int,
    ):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []

    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        our_object = Person.people[person["name"]]

        if "wife" in person and person["wife"] is not None:
            our_object.wife = Person.people[person["wife"]]
            result.append(our_object)

        elif "husband" in person and person["husband"] is not None:
            our_object.husband = Person.people[person["husband"]]
            result.append(our_object)

        else:
            result.append(our_object)

    return result
