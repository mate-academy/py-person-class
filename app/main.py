class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    dictionary = []
    for man in people:
        dictionary.append(Person(man["name"], man['age']))
    for index, man in enumerate(people):
        if 'wife' in man and man['wife'] is not None:
            Person.people[man["name"]].wife = Person.people[man["wife"]]
        if "husband" in man and man['husband'] is not None:
            Person.people[man["name"]].husband = Person.people[man["husband"]]

    return dictionary
