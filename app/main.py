class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person in people:
        if person.get("wife"):
            wife = Person.people[person["wife"]]
            husband = Person.people[person["name"]]

        if person.get("husband"):
            husband = Person.people[person["husband"]]
            wife = Person.people[person["name"]]

    husband.wife = wife
    wife.husband = husband

    return list_of_people
