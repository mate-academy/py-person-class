class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        current_person = Person.people[person_data["name"]]

        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        if wife_name:
            current_person.wife = Person.people[wife_name]

        if husband_name:
            current_person.husband = Person.people[husband_name]

    return persons
