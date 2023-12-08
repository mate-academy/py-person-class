
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_list = [
        Person(person_info["name"],
               person_info["age"]) for person_info in people
    ]

    for person_data in people:
        obj = Person.people.get(person_data.get("name"))
        if obj:
            if person_data.get("wife"):
                obj.wife = Person.people.get(person_data.get("wife"))
            elif person_data.get("husband"):
                obj.husband = Person.people.get(person_data.get("husband"))

    return person_list
