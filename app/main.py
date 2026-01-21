class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        human = Person.people[person["name"]]
        person_wife = person.get("wife")
        person_husband = person.get("husband")

        if person_wife:
            human.wife = Person.people[person_wife]
        if person_husband:
            human.husband = Person.people[person_husband]

    return people_list
