class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        (Person(name=person["name"], age=person["age"]))
    print(Person.people)

    for person in people:

        if "husband" in person and person["husband"] is not None:
            Person.people[person["name"]].husband =\
                Person.people[person["husband"]]
            person_list.append(Person.people[person["name"]])

        elif "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
            person_list.append(Person.people[person["name"]])

        else:
            person_list.append(Person.people[person["name"]])

    print(person_list)
    return person_list
