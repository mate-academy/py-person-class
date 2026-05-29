class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        current_person = Person.people[person_data["name"]]

        wife = person_data.get("wife")
        husband = person_data.get("husband")

        if wife:
            current_person.wife = Person.people[wife]

        if husband:
            current_person.husband = Person.people[husband]

    return person_list
