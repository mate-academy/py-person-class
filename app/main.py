class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for data in people:
        Person(data["name"], data["age"])

    for data in people:
        person = Person.people[data["name"]]
        if "wife" in data and data["wife"]:
            wife_name = data["wife"]
            if wife_name in Person.people:
                person.wife = Person.people[wife_name]
        if "husband" in data and data["husband"]:
            husband_name = data["husband"]
            if husband_name in Person.people:
                person.husband = Person.people[husband_name]

    return list(Person.people.values())
