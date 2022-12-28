class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for human in people:
        person = Person(human["name"], human["age"])
        person_list.append(person)

    for human in people:
        for person in person_list:
            if (person.name == human["name"]) \
                    and ("wife" in human) \
                    and (human["wife"] is not None):
                person.wife = person.__class__.people[human["wife"]]
            elif (person.name == human["name"]) \
                    and ("husband" in human) \
                    and (human["husband"] is not None):
                person.husband = person.__class__.people[human["husband"]]
            else:
                pass

    return person_list
