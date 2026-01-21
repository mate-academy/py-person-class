class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    [Person(human["name"], human["age"]) for human in people]

    for human in people:
        instance = Person.people[human["name"]]

        spouse_name = human.get("wife")
        if spouse_name:
            instance.wife = Person.people[spouse_name]

        spouse_name = human.get("husband")
        if spouse_name:
            instance.husband = Person.people[spouse_name]

    return [Person.people[human["name"]] for human in people]
