class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    result = []
    for element in people:
        result.append(Person(element["name"], element["age"]))

    for num in range(len(people)):
        k_val = list(people[num].keys())
        if k_val[2] == "wife" and people[num]["wife"] is not None:
            result[num].wife = Person.people[people[num]["wife"]]
        else:
            if k_val[2] == "husband" and people[num]["husband"] is not None:
                result[num].husband = Person.people[people[num]["husband"]]
    return result
