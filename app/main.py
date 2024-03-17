class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(peoples: list) -> list:
    for member in peoples:
        Person(name=member["name"], age=member["age"])

    for member in peoples:
        if "wife" in member and member["wife"] is not None:
            wife_instance = Person.people.get(member["wife"])
            wife_instance.husband = Person.people.get(member["name"])
        elif "husband" in member and member["husband"] is not None:
            husband_instance = Person.people.get(member["husband"])
            husband_instance.wife = Person.people.get(member["name"])
    return [member for member in Person.people.values()]
