class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for one_people in people:
        one_person = Person(one_people["name"], one_people["age"])
        person_list.append(one_person)
    for i, one_people in enumerate(people):
        if None not in one_people.values():
            if "wife" in one_people:
                person_list[i].wife = Person.people[one_people["wife"]]
            if "husband" in one_people:
                person_list[i].husband = Person.people[one_people["husband"]]
    return person_list
