class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    @classmethod
    def pair_check(cls, people: list) -> None:
        for person_ in people:
            curr_person = cls.people[person_["name"]]
            if "wife" in person_ and person_["wife"]:
                curr_person.wife = cls.people[person_["wife"]]
                curr_person.wife.husband = curr_person


def create_person_list(people: list) -> list:
    for person_ in people:
        Person(name=person_["name"],
               age=person_["age"])
    Person.pair_check(people)
    return [person_ for person_ in Person.people.values()]
