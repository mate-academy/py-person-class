class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person in people:
        current = Person.people[person["name"]]
        if "wife" in person:
            wife_name = person["wife"]
            if wife_name:
                current.wife = Person.people[wife_name]
        elif "husband" in person:
            husband_name = person["husband"]
            if husband_name:
                current.husband = Person.people[husband_name]

    return result
