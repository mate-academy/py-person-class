class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.age = age
        self.name = name
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []

    for person in people:
        Person(person["name"], person["age"])

    for person in people:

        if person.get("wife") is not None:
            wife = person["wife"]
            Person.people[person["name"]].wife = Person.people[wife]
            result_list.append(Person.people[person["name"]])

        elif person.get("husband") is not None:
            husband = person["husband"]
            Person.people[person["name"]].husband = Person.people[husband]
            result_list.append(Person.people[person["name"]])

        else:
            result_list.append(Person.people[person["name"]])

    return result_list
