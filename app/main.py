class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        person_info = list(person.values())
        person_inst = Person(person_info[0], person_info[1])
        if person_info[2] and list(person.keys())[2] == "wife":
            person_inst.wife = person_info[2]
        elif person_info[2] and list(person.keys())[2] == "husband":
            person_inst.husband = person_info[2]
    for name in Person.people:
        for person in Person.people.values():
            if Person.people[name] != person:
                if hasattr(person, "husband"):
                    if person.husband == name:
                        person.husband = Person.people[name]
                if hasattr(person, "wife"):
                    if person.wife == name:
                        person.wife = Person.people[name]
    return [person for person in Person.people.values()]
