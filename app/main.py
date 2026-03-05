class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    Person.people.clear()
    for person in people:
        person_obj = Person(person["name"], person["age"])
        if person.get("wife"):
            person_obj.wife = person["wife"]
        elif person.get("husband"):
            person_obj.husband = person["husband"]
        Person.people[person["name"]] = person_obj

    for person_obj in Person.people.values():
        if hasattr(person_obj, "wife"):
            person_obj.wife = Person.people.get(person_obj.wife)
        elif hasattr(person_obj, "husband"):
            person_obj.husband = Person.people.get(person_obj.husband)
    return list(Person.people.values())
