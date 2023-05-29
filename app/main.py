class Person:
    people = {}

    def __init__(self, name: str, age: int, ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = []

    for individ in people:
        list_of_people.append(Person(individ["name"], individ["age"]))

    for individ in people:
        if "wife" in individ and individ["wife"] is not None:
            Person.people[individ["name"]].wife\
                = Person.people[individ["wife"]]

        if "husband" in individ and individ["husband"] is not None:
            Person.people[individ["name"]].husband\
                = Person.people[individ["husband"]]

    return list_of_people
