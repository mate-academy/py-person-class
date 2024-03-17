class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(peoples: list) -> list:
    created_people = []
    for member in peoples:
        person = Person(name=member.get("name"), age=member.get("age"))
        created_people.append(person)

    for member in peoples:
        if member.get("wife"):
            wife_instance = Person.people.get(member.get("wife"))
            wife_instance.husband = Person.people.get(member.get("name"))
        elif member.get("husband"):
            husband_instance = Person.people.get(member.get("husband"))
            husband_instance.wife = Person.people.get(member.get("name"))

    return created_people
