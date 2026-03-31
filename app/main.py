class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_list: list) -> list:
    Person.people.clear()
    person_list = [
        Person(human["name"], human["age"]) for human in people_list
    ]
    for person_data, human in zip(person_list, people_list):
        print(person_data, human)
        if human.get("wife"):
            person_data.wife = human["wife"]
        if human.get("husband"):
            person_data.husband = human["husband"]

    for name, human in Person.people.items():
        if hasattr(human, "wife"):
            human.wife = Person.people[human.wife]
        elif hasattr(human, "husband"):
            human.husband = Person.people[human.husband]

    return person_list
