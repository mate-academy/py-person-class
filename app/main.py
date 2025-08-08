class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    new_list = []
    for person in people:
        obj = Person(person["name"], person["age"])
        new_list.append(obj)

    for status in people:
        if status.get("wife"):
            name = status["name"]
            wife_name = status["wife"]
            Person.people[name].wife = Person.people[wife_name]
        if status.get("husband"):
            name = status["name"]
            husband_name = status["husband"]
            Person.people[name].husband = Person.people[husband_name]

    return new_list
