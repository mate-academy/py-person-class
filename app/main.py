class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(item["name"], item["age"]) for item in people]
    for item in people:
        if item.get("wife"):
            wife_name = item.get("wife")
            Person.people[item["name"]].wife = Person.people[wife_name]
        if item.get("husband"):
            husband_name = item.get("husband")
            Person.people[item["name"]].husband = Person.people[husband_name]
    return person_list
