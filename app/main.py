class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []
    result_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        name_person = Person.people[person["name"]]
        if person.get("wife"):
            name_wife = Person.people[person["wife"]]
            name_person.wife = name_wife
            name_wife.husband = name_person
        if person.get("husband"):
            name_husband = Person.people[person["husband"]]
            name_person.husband = name_husband
            name_husband.wife = name_person
    return result_list
