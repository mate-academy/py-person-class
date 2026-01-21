class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_person = [Person(person.get("name"),
                             person.get("age")) for person in people]

    for person in people:
        person_name = person.get("name")
        if "wife" in person and person.get("wife") in Person.people:
            Person.people[person_name].wife = Person.people[person.get("wife")]

        elif "husband" in person and person.get("husband") in Person.people:
            Person.people[person_name].husband = (
                Person.people)[person.get("husband")]

    return list_of_person
