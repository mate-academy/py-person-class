class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(
            Person(person["name"], person["age"])
        )
    for i in range(len(Person.people)):
        if "wife" in people[i].keys() and people[i]["wife"] is not None:
            Person.people.get(people[i]["name"]).wife \
                = Person.people.get(people[i]["wife"])
        elif "husband" in people[i].keys():
            Person.people.get(people[i]["name"]).husband \
                = Person.people.get(people[i]["husband"])
    return person_list
