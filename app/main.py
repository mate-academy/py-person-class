class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data.get("age", None)
        person = Person(name, age)

        wife_name = person_data.get("wife", None)
        if wife_name and wife_name in Person.people:
            person.wife = Person.people[wife_name]

        husband_name = person_data.get("husband", None)
        if husband_name and husband_name in Person.people:
            person.husband = Person.people[husband_name]

        person_list.append(person)

    return person_list
