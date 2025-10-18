
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    user_list = [Person(name=user.get("name"), age=user.get("age")) for user in people]
    for user in people:
        person_name = user.get("name")
        current = Person.people[person_name]
        wife_name = user.get("wife")
        husband_name = user.get("husband")
        if wife_name:
            current.wife = Person.people[wife_name]
        if husband_name:
            current.husband = Person.people[husband_name]
    return user_list
