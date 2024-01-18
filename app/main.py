class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_people_list = [Person(person_dict["name"], person_dict["age"])
                       for person_dict in people]
    for person in new_people_list:
        for person_dict in people:
            if person_dict["name"] == person.name:
                if person_dict.get("wife"):
                    person.wife = Person.people[person_dict["wife"]]
                if person_dict.get("husband"):
                    person.husband = Person.people[person_dict["husband"]]
    return new_people_list
