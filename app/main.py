class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    person_list = [Person(d["name"], d["age"]) for d in people]

    for people_dict, obj in zip(people, person_list):
        if people_dict.get("wife") is not None:
            obj.wife = Person.people[people_dict["wife"]]
        if people_dict.get("husband") is not None:
            obj.husband = Person.people[people_dict["husband"]]
    return person_list
