class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_with_people = []

    for person in people:
        new_person = Person(person["name"], person["age"])
        list_with_people.append(new_person)

    for index, human in enumerate(people):
        if human.get("wife") is not None:
            name = human["wife"]
            list_with_people[index].wife = Person.people[name]
        if human.get("husband") is not None:
            name = human["husband"]
            list_with_people[index].husband = Person.people[name]

    return list_with_people
