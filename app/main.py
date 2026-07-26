class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person["name"], person["age"]) for person in people
    ]

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")

        if wife_name:
            person.wife = Person.people[wife_name]

        if husband_name:
            person.husband = Person.people[husband_name]

    return person_list
