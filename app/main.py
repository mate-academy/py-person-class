class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for individ in people:
        name = individ["name"]
        age = individ["age"]
        person = Person(name, age)
        person_list.append(person)

    for individ in people:
        name = individ["name"]
        person = Person.people[name]
        if "wife" in individ and individ["wife"] is not None:
            wife_name = individ["wife"]
            person.wife = Person.people[wife_name]
            Person.people[wife_name].husband = person

        if "husband" in individ and individ["husband"] is not None:
            husband_name = individ["husband"]
            person.husband = Person.people[husband_name]
            Person.people[husband_name].wife = person

    return person_list
