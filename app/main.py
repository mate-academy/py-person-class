class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_person = [
        Person(person["name"], person["age"]) for person in people
    ]

    for person in people:
        current_person = Person.people[person["name"]]
        person_wife = person.get("wife")
        person_husband = person.get("husband")

        if person_wife:
            current_person.wife = Person.people[person_wife]
        if person_husband:
            current_person.husband = Person.people[person_husband]

    return list_of_person
