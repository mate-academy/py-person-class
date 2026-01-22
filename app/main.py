class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person_data in people:
        Person(person_data["name"], person_data["age"])

    for person_data in people:
        current_person = Person.people[person_data["name"]]

        wife_name = person_data.get("wife")
        if wife_name and wife_name in Person.people:
            current_person.wife = Person.people[wife_name]

        husband_name = person_data.get("husband")
        if husband_name and husband_name in Person.people:
            current_person.husband = Person.people[husband_name]

    return [Person.people[person["name"]] for person in people]
