class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_list: list) -> list:
    person_list = []
    for one_person in people_list:
        person = Person(name=one_person["name"], age=one_person["age"])
        person_list.append(person)

    for one_person in people_list:
        if "wife" in one_person.keys() \
                and one_person["wife"] is not None:
            name = one_person["name"]
            wife = one_person["wife"]
            Person.people[name].wife = Person.people[wife]
        elif "husband" in one_person.keys() \
                and one_person["husband"] is not None:
            name = one_person["name"]
            husband = one_person["husband"]
            Person.people[name].husband = Person.people[husband]

    return person_list
