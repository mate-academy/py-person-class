class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = [Person(friend["name"], friend["age"]) for friend in people]
    for person in people:
        person_name = Person.people[person["name"]]
        if person.get("wife"):
            person_name.wife = Person.people[person["wife"]]
        if person.get("husband"):
            person_name.husband = Person.people[person["husband"]]
    return persons_list
