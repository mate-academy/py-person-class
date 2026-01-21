class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    new_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        new_list.append(new_person)

    for other_person in people:
        instance = Person.people[other_person["name"]]
        if "wife" in other_person and other_person["wife"]:
            instance.wife = Person.people[other_person["wife"]]
        elif "husband" in other_person and other_person["husband"]:
            instance.husband = Person.people[other_person["husband"]]

    return list(Person.people.values())
