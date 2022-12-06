class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for man_or_woman in people:
        person_list.append(Person(name=man_or_woman["name"],
                                  age=man_or_woman["age"]))
    for man_or_woman in people:
        if "wife" in man_or_woman and man_or_woman["wife"] is not None:
            Person.people[man_or_woman["name"]].wife\
                = Person.people[man_or_woman["wife"]]
        elif "husband" in man_or_woman and man_or_woman["husband"] is not None:
            Person.people[man_or_woman["name"]].husband\
                = Person.people[man_or_woman["husband"]]
    return person_list
