class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    instances = [Person(p["name"], p["age"]) for p in people]
    for data, inst in zip(people, instances):
        spouse_name = data.get("wife")
        spouse = Person.people.get(spouse_name) if spouse_name else None
        if spouse:
            inst.wife = spouse
        spouse_name = data.get("husband")
        spouse = Person.people.get(spouse_name) if spouse_name else None
        if spouse:
            inst.husband = spouse
    return instances
