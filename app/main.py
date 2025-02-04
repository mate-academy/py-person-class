class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_info in people:
        name = person_info["name"]
        age = person_info["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_info in people:
        name = person_info["name"]
        person = Person.people[name]
        if "wife" in person_info and person_info["wife"]:
            person.wife = Person.people[person_info["wife"]]
        elif "husband" in person_info and person_info["husband"]:
            person.husband = Person.people[person_info["husband"]]
    return person_list
