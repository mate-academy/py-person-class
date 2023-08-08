class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    new_people = []

    for person_from_list in people:
        person_for_class = Person(person_from_list["name"],
                                  person_from_list["age"])
        new_people.append(person_for_class)

    for person_from_list in people:
        if ("wife" in person_from_list
                and person_from_list["wife"] is not None):
            main_person = Person.people[person_from_list["name"]]
            person_wife = Person.people[person_from_list["wife"]]
            main_person.wife = person_wife
        elif ("husband" in person_from_list
              and person_from_list["husband"] is not None):
            main_person = Person.people[person_from_list["name"]]
            person_husband = Person.people[person_from_list["husband"]]
            main_person.husband = person_husband

    return new_people
