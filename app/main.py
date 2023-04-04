class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        if "husband" in kwargs.keys() and kwargs["husband"] is not None:
            self.husband = kwargs["husband"]
        elif "wife" in kwargs.keys() and kwargs["wife"] is not None:
            self.wife = kwargs["wife"]
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = []

    for people_person in people:
        human = Person(people_person["name"], people_person["age"])
        list_of_people.append(human)

    for people_person in people:
        human = Person.people[people_person["name"]]

        if "husband" in people_person and people_person["husband"] is not None:
            husband = Person.people[people_person["husband"]]
            human.husband = husband
            husband.wife = human
        elif "wife" in people_person and people_person["wife"] is not None:
            wife = Person.people[people_person["wife"]]
            human.wife = wife
            wife.husband = human

    return list_of_people
