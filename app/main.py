
class Person:
    people = {}

    def __init__(self, name : str, age : int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        the_person = Person(person["name"], person["age"])
        person_list.append(the_person)
    for index, person in enumerate(people):
        wife = person.get("wife")
        husband = person.get("husband")
        if wife is not None:
            person_list[index].wife = Person.people[wife]
        if husband is not None:
            person_list[index].husband = Person.people[husband]

    return person_list
