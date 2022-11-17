class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people.update({name: self})


def create_person_list(people: list) -> list[Person]:
    list_of_persons = []
    for person in people:
        instance_person = Person(person["name"], person["age"])
        list_of_persons.append(instance_person)

    for person in range(len(people)):
        if "wife" in people[person] and people[person]["wife"] is not None:
            list_of_persons[person].wife = \
                Person.people[people[person]["wife"]]
        if "husband" in people[person] and \
                people[person]["husband"] is not None:
            list_of_persons[person].husband = \
                Person.people[people[person]["husband"]]

    return list_of_persons
