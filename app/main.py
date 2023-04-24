class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self

    @classmethod
    def get_person(cls, name: str):
        return cls.people[name]


def create_person_list(people: list) -> list:
    res = []
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        res.append(person)
    for i, person_data in enumerate(people):
        if person_data.get("wife") is not None:
            res[i].wife = res[i].get_person(person_data["wife"])
        if person_data.get("husband") is not None:
            res[i].husband = res[i].get_person(person_data["husband"])
    return res
