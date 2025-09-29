class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    Person.people.clear()

    person_instances = [Person(name=p["name"], age=p["age"]) for p in people]

    for person_data in people:
        name = person_data["name"]
        person = Person.people[name]

        wife_name = person_data.get("wife")
        if wife_name:
            setattr(person, "wife", Person.people[wife_name])

        husband_name = person_data.get("husband")
        if husband_name:
            setattr(person, "husband", Person.people[husband_name])

    return person_instances
