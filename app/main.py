class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(list_of_people: list) -> list:
    people_list = [Person(person["name"], person["age"])
                   for person in list_of_people]

    for person_dict in list_of_people:
        person = Person.people[person_dict["name"]]
        if person_dict.get("wife"):
            wife = Person.people[person_dict["wife"]]
            person.wife = wife
        elif person_dict.get("husband"):
            husband = Person.people[person_dict["husband"]]
            person.husband = husband

    return people_list
