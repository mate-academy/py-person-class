class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.age = age
        self.name = name
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []

    [Person(person["name"], person["age"])for person in people]

    for person in people:

        if person.get("wife") is not None:
            Person.people[person["name"]].wife = (
                Person.people)[person["wife"]]
            result_list.append(Person.people[person["name"]])

        elif person.get("husband") is not None:
            Person.people[person["name"]].husband\
                = Person.people[person["husband"]]
            result_list.append(Person.people[person["name"]])

        else:
            result_list.append(Person.people[person["name"]])

    return result_list
