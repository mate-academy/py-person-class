class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_persons = [
        Person(person["name"], person["age"]) for person in people
    ]
    for every_people in people:
        name = every_people["name"]
        persons_name = Person.people[name]

        if every_people.get("wife"):
            persons_name.wife = Person.people[every_people["wife"]]
        if every_people.get("husband"):
            persons_name.husband = Person.people[every_people["husband"]]
    return list_of_persons
