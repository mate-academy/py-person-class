class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    result = list()

    [Person(person["name"], person["age"]) for person in people]

    for person in people:
        instance_person = Person.people[person["name"]]
        if "wife" in person:
            if person["wife"]:
                instance_person.wife = Person.people[person["wife"]]
        elif "husband" in person:
            if person["husband"]:
                instance_person.husband = Person.people[person["husband"]]
        result.append(instance_person)

    return result
