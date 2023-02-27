class Person:
    people = {}

    def __init__(self, name: str, age: int, *args, **kwargs):
        self.name = name
        self.age = age
        if kwargs == "husband":
            self.husband = kwargs
        elif kwargs == "wife":
            self.wife = kwargs


def create_person_list(people: list) -> list:
    list_of_people = []
    for people_person in people:
        if "wife" in people_person.keys():
            pers = Person(people_person["name"], people_person["age"], people_person["wife"])
            Person.people[people_person["name"]] = pers
            list_of_people.append(pers)
        elif "husband" in people_person.keys():
            pers = Person(people_person["name"], people_person["age"], people_person["husband"])
            Person.people[people_person["name"]] = pers
            list_of_people.append(pers)
        elif len(people_person) <= 2:
            pers = Person(people_person["name"], people_person["age"])
            Person.people[people_person["name"]] = pers
            list_of_people.append(pers)
    return list_of_people
