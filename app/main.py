class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife"):
            current_person = Person.people[person["name"]]
            person_wife = Person.people[person["wife"]]
            current_person.wife = person_wife

        elif person.get("husband"):
            current_person = Person.people[person["name"]]
            person_husband = Person.people[person["husband"]]
            current_person.husband = person_husband

    return result
