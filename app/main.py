class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    result = []

    for person in people:
        new_person = Person(person["name"], person["age"])
        result.append(new_person)

    for person_data in people:
        current_person = Person.people[person_data["name"]]
        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        if husband_name is not None:
            current_person.husband = Person.people[husband_name]

        if wife_name is not None:
            current_person.wife = Person.people[wife_name]

    return result
