class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(peoples: list) -> list:
    [Person(member["name"], member["age"]) for member in peoples]

    for member in peoples:
        new_person = Person.people.get(member["name"])
        if wife_name := member.get("wife"):
            new_person.wife = Person.people.get(wife_name)

        elif husband_name := member.get("husband"):
            new_person.husband = Person.people.get(husband_name)

    return list(Person.people.values())
