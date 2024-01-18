class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_people_list = []
    for person_dict in people:
        new_person = Person(person_dict["name"], person_dict["age"])
        new_people_list.append(new_person)
    for person in new_people_list:
        for person_dict in people:
            if person_dict["name"] == person.name:
                if "wife" in person_dict:
                    if person_dict["wife"] is not None:
                        person.wife = Person.people[person_dict["wife"]]
                if "husband" in person_dict:
                    if person_dict["husband"] is not None:
                        person.husband = Person.people[person_dict["husband"]]
    return new_people_list
