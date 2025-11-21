class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []

    for person in people:
        person_obj = Person(person["name"], person["age"])
        result.append(person_obj)

    for person in people:
        name = person["name"]
        instance = Person.people[name]

        if "wife" in person and person["wife"] is not None:
            wife_name = person["wife"]
            instance.wife = Person.people[wife_name]

        if "husband" in person and person["husband"] is not None:
            husband_name = person["husband"]
            instance.husband = Person.people[husband_name]

    return result
