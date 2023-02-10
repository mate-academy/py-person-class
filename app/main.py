class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts: dict) -> list:
    person_list = []
    for item in people_dicts:
        person = Person(item["name"], item["age"])
        if item.get("wife") is not None:
            person.wife = item["wife"]
        if item.get("husband") is not None:
            person.husband = item["husband"]
        person_list.append(person)

    for person in person_list:
        if hasattr(person, "wife"):
            person.wife = Person.people[person.wife]
        if hasattr(person, "husband"):
            person.husband = Person.people[person.husband]

    return person_list
