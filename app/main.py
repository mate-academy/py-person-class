class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]

    for person_data in people:
        person = Person.people[person_data["name"]]

        wife = person_data.get("wife")
        husband = person_data.get("husband")

        if wife:
            person.wife = Person.people[wife]

        if husband:
            person.husband = Person.people[husband]

    return person_list
