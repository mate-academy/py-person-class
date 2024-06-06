class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    output_list = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        output_list.append(person)
    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if person_dict.get("wife"):
            person.wife = Person.people[person_dict["wife"]]
        if person_dict.get("husband"):
            person.husband = Person.people[person_dict["husband"]]
    return output_list
