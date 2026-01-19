class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    people_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person1 = Person.people[person["name"]]
        if person.get("wife"):
            person1.wife = Person.people[person["wife"]]
            person1.wife.husband = person1
        if person.get("husband"):
            person1.husband = Person.people[person["husband"]]
            person1.husband.wife = person1

    return people_list
