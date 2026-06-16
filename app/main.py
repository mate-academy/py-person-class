class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # List comprehension creates instances in input order
    person_instances = [Person(data["name"], data["age"]) for data in people]

    # Use zip to iterate over both lists together
    for person_data, person in zip(people, person_instances):
        wife_name = person_data.get("wife")
        if wife_name:
            person.wife = Person.people.get(wife_name)

        husband_name = person_data.get("husband")
        if husband_name:
            person.husband = Person.people.get(husband_name)

    return person_instances
