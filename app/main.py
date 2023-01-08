class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    new_list = list()
    for person in people:
        if None in person.values():
            new_list.append(Person(person["name"], person["age"]))
        else:
            keys = list(person.keys())
            new_person = Person(person["name"], person["age"])
            if keys[2] == "wife":
                new_person.wife = person["wife"]
            else:
                new_person.husband = person["husband"]
            new_list.append(new_person)

    for person in new_list:
        if "wife" in dir(person):
            person.wife = Person.people[person.wife]
        elif "husband" in dir(person):
            person.husband = Person.people[person.husband]
    return new_list
