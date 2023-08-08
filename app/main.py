class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = {}
    for each in people:
        name = each["name"]
        age = each["age"]
        persons[name] = Person(name, age)

    for each in people:
        if "wife" in each and each["wife"] in persons:
            wife = each["wife"]
            persons[each["name"]].wife = persons[wife]
        if "husband" in each and each["husband"] in persons:
            husband = each["husband"]
            persons[each["name"]].husband = persons[husband]

    return list(persons.values())
