class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    classes_people = [
        Person(person["name"], person["age"])
        for person in people
    ]
    for human in people:
        if human.get("wife"):
            wife = Person.people[human["wife"]]
            Person.people[human["name"]].wife = wife
        elif human.get("husband"):
            husband = Person.people[human["husband"]]
            Person.people[human["name"]].husband = husband
    return classes_people
