class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    res = []
    for di in people:
        person = Person(di["name"], di["age"])
        Person.people[di["name"]] = person
        res.append(person)
    for di in people:
        for cls in res:
            if "wife" in di:
                if di["name"] == cls.name and di["wife"] is not None:
                    cls.wife = Person.people[di["wife"]]
            if "husband" in di:
                if di["name"] == cls.name and di["husband"] is not None:
                    cls.husband = Person.people[di["husband"]]
    return res
