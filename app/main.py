class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    people_mapping = {}

    for person_data in people:
        name = person_data["name"]
        age = person_data.get("age", None)
        person = Person(name, age)
        people_mapping[name] = person
        person_list.append(person)

    for person_data in people:
        name = person_data["name"]
        person = people_mapping[name]

        wife_name = person_data.get("wife", None)
        if wife_name:
            person.wife = people_mapping.get(wife_name, None)

        husband_name = person_data.get("husband", None)
        if husband_name:
            person.husband = people_mapping.get(husband_name, None)

    return person_list
