class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[str(self.name)] = self


def create_person_list(people: list[dict]) -> list:
    result = []
    for member in people:
        result.append(Person(member["name"], member["age"]))

    for member in people:
        if member.get("wife"):
            wife_name = Person.people[member["wife"]]
            Person.people[member["name"]].wife = wife_name
        elif member.get("husband"):
            husband_name = Person.people[member["husband"]]
            Person.people[member["name"]].husband = husband_name

    return result
