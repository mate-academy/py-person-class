class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_info in people:
        person_inst = Person(person_info["name"], person_info["age"])
        person_list.append(person_inst)

    for person_info in people:
        name = person_info["name"]
        person_inst = Person.people[name]

        if person_info.get("wife"):
            spouse_inst = Person.people[person_info["wife"]]
            person_inst.wife = spouse_inst

        if person_info.get("husband"):
            spouse_inst = Person.people[person_info["husband"]]
            person_inst.husband = spouse_inst

    return person_list
