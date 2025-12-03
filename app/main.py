class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    instances_of_persons = \
        [
            Person(human["name"], human["age"])
            for human in people
        ]
    for person_dict in people:
        current = Person.people[person_dict["name"]]
        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")
        if wife_name is not None:
            current.wife = Person.people[wife_name]
        if husband_name is not None:
            current.husband = Person.people[husband_name]
    return instances_of_persons
