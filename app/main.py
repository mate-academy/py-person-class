class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    result_list = []
    for person in people:
        inst = Person(name=person["name"], age=person["age"])
        # if "wife" in person and person["wife"] is not None:
        #     inst.wife = Person.people[person["wife"]]
        # elif "husband" in person and person["husband"] is not None:
        #     inst.husband = Person.people[person["husband"]]
        result_list.append(inst)
    for index, person in enumerate(people):
        if "wife" in person and person["wife"] is not None:
            result_list[index].wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            result_list[index].husband = Person.people[person["husband"]]
    return result_list
