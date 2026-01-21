class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])
    for human in people:
        person_instance = Person.people[human["name"]]
        if human.get("wife"):
            person_instance.wife = Person.people[human["wife"]]
        if human.get("husband"):
            person_instance.husband = Person.people[human["husband"]]

    return list(Person.people.values())
