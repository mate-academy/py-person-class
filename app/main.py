class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    people_objs = [
        Person(person["name"], person["age"])
        for person in people
    ]
    for person in people:
        if person.get("wife") is not None:
            wife = Person.people.get(person["wife"])
            husband = Person.people.get(person["name"])
            husband.wife = wife
        if person.get("husband") is not None:
            husband = Person.people.get(person["husband"])
            wife = Person.people.get(person["name"])
            wife.husband = husband
    return people_objs
