class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    inst_peoples = []
    for dict_person in people:
        name, age = dict_person["name"], dict_person["age"]
        inst_peoples.append(Person(name, age))

    for i in range(len(people)):
        dict_person = people[i]
        inst_people = inst_peoples[i]

        if "wife" in dict_person and dict_person["wife"] is not None:
            wife_name = dict_person["wife"]
            inst_people.wife = Person.people[wife_name]

        if "husband" in dict_person and dict_person["husband"] is not None:
            husband_name = dict_person["husband"]
            inst_people.husband = Person.people[husband_name]

    return inst_peoples
