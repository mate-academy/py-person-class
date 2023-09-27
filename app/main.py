class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []

    for person_list in people:
        name = person_list["name"]
        wife_or_husband = list(person_list.keys())[2]

        if name in Person.people:
            Person.people[name].age = person_list["age"]

        else:
            Person.people[name] = Person(name, person_list["age"])
        if (person_list[wife_or_husband] is not None
                and person_list[wife_or_husband] in Person.people):
            setattr(Person.people[name],
                    wife_or_husband,
                    Person.people[person_list[wife_or_husband]])
        elif person_list[wife_or_husband] is not None:
            setattr(Person.people[name],
                    wife_or_husband,
                    Person(person_list[wife_or_husband], 0))
        result_list.append(Person.people[name])

    return result_list
