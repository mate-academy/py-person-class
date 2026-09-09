class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(i["name"], i["age"]) for i in people]
    for i in people:
        wife_name = i.get("wife")
        if wife_name is not None:
            Person.people[i["name"]].wife = Person.people[wife_name]
        husband_name = i.get("husband")
        if husband_name is not None:
            Person.people[i["name"]].husband = Person.people[husband_name]
    return people_list
