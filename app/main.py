class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_data: list) -> list:
    Person.people = {}
    for person_item in people_data:
        new_person = Person(person_item["name"],
                            person_item["age"])
        if person_item.get("wife") and person_item["wife"] is not None:
            new_person.wife = person_item["wife"]
        if person_item.get("husband") and person_item["husband"] is not None:
            new_person.husband = person_item["husband"]

    for person_item in Person.people.values():
        if hasattr(person_item, "wife"):
            person_item.wife = Person.people[person_item.wife]
        if hasattr(person_item, "husband"):
            person_item.husband = Person.people[person_item.husband]

    return [person for person in Person.people.values()]
