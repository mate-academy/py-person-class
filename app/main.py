class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.age = age
        self.name = name
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    result = [Person(p["name"], p["age"]) for p in people]
    for original, inst in zip(people, result):
        for key in ("wife", "husband"):
            partner = original.get(key)
            if partner is not None:
                setattr(inst, key, Person.people[partner])
    print(Person.people.keys())
    print([p.name for p in result])
    return result
