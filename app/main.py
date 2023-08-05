class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.add_object(self)

    @classmethod
    def add_object(cls, obj: object) -> None:
        cls.people[obj.name] = obj


def create_person_list(people: list[dict]) -> list[Person]:
    result = []

    for pers in people:
        person = Person(name=pers["name"], age=pers["age"])
        if "wife" in pers and pers["wife"] is not None:
            for i in Person.people.values():
                if i.name == pers["wife"]:
                    person.wife = i
                    i.husband = person
        elif "husband" in pers and pers["husband"] is not None:
            for i in Person.people.values():
                if i.name == pers["husband"]:
                    person.husband = i
                    i.wife = person
        result.append(person)
    return result
