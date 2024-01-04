class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = list()
    for person_data in people:
        person_data = Person(person_data["name"], person_data["age"])

    for person_data in people:
        tmp = Person.people[person_data["name"]]
        if "wife" in person_data:
            if person_data["wife"]:
                tmp.wife = Person.people[person_data["wife"]]
        elif "husband" in person_data:
            if person_data["husband"]:
                tmp.husband = Person.people[person_data["husband"]]
        person_list.append(tmp)

    return person_list
