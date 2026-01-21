class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    instances = [Person((person_dict["name"])
                        , person_dict["age"]) for person_dict in people]

    for person_dict in people:
        inst = Person.people[person_dict["name"]]
        wife_name = person_dict.get("wife")
        if wife_name is not None:
            inst.wife = Person.people.get(wife_name)
        husband_name = person_dict.get("husband")
        if husband_name is not None:
            inst.husband = Person.people.get(husband_name)
    return instances
