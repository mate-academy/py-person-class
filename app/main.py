class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person_data in people:
        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")
        person = Person.people[person_data["name"]]
        if wife_name is not None:
            person.wife = Person.people[wife_name]
        if husband_name is not None:
            person.husband = Person.people[husband_name]
    return person_list
