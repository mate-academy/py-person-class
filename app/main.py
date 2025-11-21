class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(p["name"], int(p["age"]))
        for p in people
    ]

    for person_dict in people:
        person = Person.people[person_dict["name"]]

        wife_name = person_dict.get("wife")
        if wife_name:
            person.wife = Person.people[wife_name]

        husband_name = person_dict.get("husband")
        if husband_name:
            person.husband = Person.people[husband_name]

    return person_list
