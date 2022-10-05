class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people_dict: list) -> list:
    result = []
    for person in people_dict:
        new_person = Person(person["name"], person["age"])
        result.append(new_person)
    for par in people_dict:
        if par.get("wife") is not None:
            Person.people[par["name"]].wife = Person.people[par["wife"]]
        elif par.get("husband") is not None:
            Person.people[par["name"]].husband = Person.people[par["husband"]]
        else:
            continue

    return result
