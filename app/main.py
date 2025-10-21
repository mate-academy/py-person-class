class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for person_dic in people:
        person = Person(person_dic["name"], person_dic["age"])
        result.append(person)

    for person_dic in people:
        name = person_dic["name"]
        if "wife" in person_dic and person_dic["wife"]:
            Person.people[name].wife = Person.people[person_dic["wife"]]
        if "husband" in person_dic and person_dic["husband"]:
            Person.people[name].husband = Person.people[person_dic["husband"]]

    return result
