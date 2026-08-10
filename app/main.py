class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.age = age
        self.name = name


def create_person_list(people: list) -> list:
    result_list = []

    for person in people:
        name = person["name"]
        age = person["age"]
        self = Person(name, age)
        Person.people[name] = self

    for person in people:
        name = person["name"]

        if person.get("wife") is not None:
            wife = person["wife"]
            self.people[name].wife = self.people[name].people[wife]
            result_list.append(self.people[name])

        elif person.get("husband") is not None:
            husband = person["husband"]
            self.people[name].husband = self.people[name].people[husband]
            result_list.append(self.people[name])

        else:
            result_list.append(self.people[name])

    return result_list
