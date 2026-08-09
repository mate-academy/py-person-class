class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    list_of_people = [
        Person(human["name"], human["age"])
        for human in people
    ]

    for human in people:
        person = Person.people[human["name"]]

        wife = human.get("wife")
        if wife and wife in Person.people:
            person.wife = Person.people[wife]

        husband = human.get("husband")
        if husband and husband in Person.people:
            person.husband = Person.people[husband]

    return list_of_people
