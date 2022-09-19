class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.add_person(self)

    @classmethod
    def add_person(cls, person: "Person"):
        cls.people[person.name] = person

    @classmethod
    def get_person(cls, name: str):
        return cls.people[name]


def create_person_list(people: list) -> list:
    res = []
    i = 0
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        res.append(person)
    for person_data in people:
        try:
            if person_data["wife"] is not None:
                res[i].wife = res[i].get_person(person_data["wife"])
        except KeyError:
            pass
        try:
            if person_data["husband"] is not None:
                res[i].husband = res[i].get_person(person_data["husband"])
        except KeyError:
            pass
        i += 1
    return res
