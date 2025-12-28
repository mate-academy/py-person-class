class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = [
        Person(name=person["name"], age=person["age"]) for person in people
    ]
    for current_person in people:
        if current_person.get("wife") is not None:
            Person.people.get(
                current_person.get("name")).wife = Person.people.get(
                current_person["wife"]
            )

        elif current_person.get("husband") is not None:
            Person.people.get(
                current_person.get("name")).husband = Person.people.get(
                current_person["husband"]
            )

    return person_list
