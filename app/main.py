class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        name = person["name"]
        age = person["age"]
        person_list.append(Person(name, age))
        if person.get("husband"):
            wife = Person.people[name]
            husband = Person.people[person["husband"]]
            wife.husband = husband
            husband.wife = wife
    return person_list