class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    list_with_people = []

    for person in people:
        new_person = Person(person["name"], person["age"])
        list_with_people.append(new_person)

    for index, hum in enumerate(people):
        if "wife" in hum:
            name = hum["wife"]
            if name is not None:
                list_with_people[index].wife = Person.people[name]
        if "husband" in hum:
            name = hum["husband"]
            if name is not None:
                list_with_people[index].husband = Person.people[name]

    return list_with_people
