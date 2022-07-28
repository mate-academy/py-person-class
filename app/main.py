class Person:
    people = dict()

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_list = list()
    for human in people:
        person = Person(human["name"], human["age"])
        new_list.append(person)

    for number, individ in enumerate(people):
        if "wife" in individ.keys() and individ["wife"] is not None:
            setattr(new_list[number], "wife", Person.people[individ["wife"]])
        elif "husband" in individ.keys() and individ["husband"] is not None:
            setattr(
                new_list[number], "husband", Person.people[individ["husband"]]
            )
    return new_list
