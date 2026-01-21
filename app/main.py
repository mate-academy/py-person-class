class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    person_list = [Person(man["name"], man["age"]) for man in people]

    for index, man in enumerate(person_list):

        if ("wife" in people[index] and people[index]["wife"]
                is not None):
            person_list[index].wife = (
                Person.people)[people[index]["wife"]]
        elif ("husband" in people[index] and people[index]["husband"]
              is not None):
            person_list[index].husband = (
                Person.people)[people[index]["husband"]]

    return person_list
