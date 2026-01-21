class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people["name"] = self.name
        Person.people["age"] = self.age


def create_person_list(people: list) -> list:
    list_of_persons = []
    for person in people:
        tmp = Person(person["name"], person["age"])
        if "wife" in people:
            tmp.wife = person["wife"]
        elif "husband" in people:
            tmp.wife = person["husband"]
        list_of_persons.append(tmp)
    return list_of_persons
