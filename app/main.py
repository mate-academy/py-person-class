class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for data in people:
        person = Person(data["name"], data["age"])
        if "wife" in data and data["wife"] is not None:
            if data["wife"] in person.__class__.people:
                person.wife = person.__class__.people[data["wife"]]
                person.wife.husband = person
        elif "husband" in data and data["husband"] is not None:
            if data["husband"] in person.__class__.people:
                person.husband = person.__class__.people[data["husband"]]
                person.husband.wife = person
        person_list.append(person)
    return person_list
