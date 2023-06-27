class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_persons = []
    for person in people:
        one_per = Person(person["name"], person["age"])
        if "wife" in person.keys():
            if person["wife"] is not None:
                one_per.wife = person["wife"]
        elif "husband" in person.keys():
            if person["husband"] is not None:
                one_per.husband = person["husband"]
        list_of_persons.append(one_per)

    for item in list_of_persons:
        if "wife" in item.__dict__:
            item.wife = Person.people[item.wife]
        elif "husband" in item.__dict__:
            item.husband = Person.people[item.husband]

    return list_of_persons
