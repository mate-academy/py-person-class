class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person_info in people:
        Person(person_info["name"], person_info["age"])
    for person_info in people:
        person_instance = Person.people[person_info["name"]]
        if "wife" in person_info and person_info["wife"]:
            person_instance.wife = Person.people[person_info["wife"]]
        if "husband" in person_info and person_info["husband"]:
            person_instance.husband = Person.people[person_info["husband"]]

    return list(Person.people.values())
