class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_list: list) -> list:
    out_list = []
    for man in people_list:
        new_person = Person(man["name"], man["age"])
        if man.get("husband"):
            new_person.husband = man["husband"]
        elif man.get("wife"):
            new_person.wife = man["wife"]
        out_list.append(new_person)

    for name, man in Person.people.items():
        print(name, "   ", man)
        if "wife" in man.__dict__:
            man.wife = Person.people[man.wife]
        elif "husband" in man.__dict__:
            man.husband = Person.people[man.husband]

    return out_list
