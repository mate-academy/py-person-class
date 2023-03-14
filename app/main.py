class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        if "husband" in kwargs.keys() and kwargs["husband"] is not None:
            self.husband = kwargs["husband"]
        elif "wife" in kwargs.keys() and kwargs["wife"] is not None:
            self.wife = kwargs["wife"]
        Person.people[name] = self  # Add person to dictionary


def create_person_list(people: list) -> list:
    list_of_people = []
    for people_person in people:
        if "husband" in people_person and people_person["husband"] is not None:
            husband = Person(people_person["husband"], 0)
            pers = Person(people_person["name"], people_person["age"], husband=husband)
            husband.wife = pers
        elif "wife" in people_person and people_person["wife"] is not None:
            wife = Person(people_person["wife"], 0)
            pers = Person(people_person["name"], people_person["age"], wife=wife)
            wife.husband = pers
        else:
            pers = Person(people_person["name"], people_person["age"])
        Person.people[people_person["name"]] = pers
        list_of_people.append(pers)
    return list_of_people
