class Person:
    people = {}

    def __init__(self, name: str, age: int) -> any:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        person_in_progress = Person(person["name"], person["age"])
        if "wife" in person.keys():
            if person["wife"] is not None:
                if person["wife"] in Person.people:
                    wife_link = Person.people[person["wife"]]
                    person_in_progress.wife = wife_link
                    wife_link.husband = person_in_progress

        if "husband" in person.keys():
            if person["husband"] is not None:
                if person["husband"] in Person.people:
                    husband_link = Person.people[person["husband"]]
                    person_in_progress.husband = husband_link
                    husband_link.wife = person_in_progress
        result.append(person_in_progress)
    return result
