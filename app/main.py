class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    for info in people:
        Person(info["name"], info["age"])
    result = []
    for info in people:
        person = Person.people[info["name"]]
        if info.get("wife"):
            partner_name = info["wife"]
            person.wife = Person.people[partner_name]
        elif info.get("husband"):
            partner_name = info["husband"]
            person.husband = Person.people[partner_name]
        result.append(person)
    return result
