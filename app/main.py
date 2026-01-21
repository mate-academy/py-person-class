class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    lover_list = ["husband", "wife"]
    for data in people:
        person = Person(data["name"], data["age"])
        for elem in lover_list:
            if elem in data and data[elem] is not None:
                if elem == "wife" and data[elem] in Person.people:
                    person.wife = Person.people[data[elem]]
                    Person.people[data[elem]].husband = person
                elif elem == "husband" and data[elem] in Person.people:
                    person.husband = Person.people[data[elem]]
                    Person.people[data[elem]].wife = person
        person_list.append(person)
    return person_list
