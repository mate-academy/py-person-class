class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_persons = []
    for item in people:
        person = Person(name=item["name"], age=item["age"])
        list_of_persons.append(person)

    for item in range(len(people)):
        if "wife" in people[item].keys() \
                and people[item]["wife"] is not None:
            list_of_persons[item].wife = \
                Person.people[people[item]["wife"]]
        if "husband" in people[item].keys() \
                and people[item]["husband"] is not None:
            list_of_persons[item].husband = \
                Person.people[people[item]["husband"]]
    return list_of_persons
