class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        person_list.append(person)

    for person_data in people:
        person = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"] is not None:
            person.wife = Person.people[person_data["wife"]]
            person.wife.husband = person

        elif "husband" in person_data and person_data["husband"] is not None:
            person.husband = Person.people[person_data["husband"]]
            person.husband.wife = person

        else:
            person.wife = None
            person.husband = None

    return person_list
