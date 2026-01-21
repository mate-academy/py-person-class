class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_objects = []
    for data in people_list:
        person = Person(name=data["name"], age=data["age"])
        person_objects.append(person)

    for data in people_list:
        person = Person.people[data["name"]]

        if "wife" in data and data["wife"] is not None:
            wife = Person.people[data["wife"]]
            person.wife = wife
            wife.husband = person

        if "husband" in data and data["husband"] is not None:
            husband = Person.people[data["husband"]]
            person.husband = husband
            husband.wife = person

    return person_objects
