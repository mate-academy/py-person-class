class Person:
    people = {}
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        p = Person(person["name"], person["age"])
        person_list.append(p)

    for p in people:
        name = p["name"]
        instance = Person.people[name]

        if "wife" in p and p["wife"] is not None:
            spouse_name = p["wife"]
            instance.wife = Person.people[spouse_name]

        if "husband" in p and p["husband"] is not None:
            spouse_name = p["husband"]
            instance.husband = Person.people[spouse_name]

    return person_list