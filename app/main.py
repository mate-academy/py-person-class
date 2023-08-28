class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = []

    for person in people:
        name = person["name"]
        wife_or_husband = list(person.keys())[2]

        if name in Person.people:
            Person.people[name].age = person["age"]
        else:
            Person.people[name] = Person(name, person["age"])
        if (person[wife_or_husband] is not None
                and person[wife_or_husband] in Person.people):
            setattr(Person.people[name],
                    wife_or_husband,
                    Person.people[person[wife_or_husband]])
        elif person[wife_or_husband] is not None:
            setattr(Person.people[name],
                    wife_or_husband,
                    Person(person[wife_or_husband], 0))
        result_list.append(Person.people[name])

    return result_list
