class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person_info["name"], person_info["age"])
                   for person_info in people]

    for person_info in people:
        person_inst = Person.people[person_info["name"]]

        if person_info.get("wife"):
            person_inst.wife = Person.people[person_info["wife"]]

        if person_info.get("husband"):
            person_inst.husband = Person.people[person_info["husband"]]

    return person_list
