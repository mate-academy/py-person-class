class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = ([Person(item["name"], item["age"]) for item in people])
    for item in people:
        person = Person.people[item["name"]]
        if item.get("wife"):
            wife = item.get("wife")
            person.wife = Person.people[wife]
        if item.get("husband"):
            husband = item.get("husband")
            person.husband = Person.people[husband]
    return people_list
