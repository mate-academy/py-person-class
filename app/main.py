class Person:

    people = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age
        self.people.update({self.name: self})

    def add_wife(self, wife: object) -> None:
        if wife:
            self.wife = wife

    def add_husband(self, husband: object) -> None:
        if husband:
            self.husband = husband


def create_person_list(people1: list) -> list:
    person_list1 = []
    for person in people1:
        one_person = Person(person["name"], person["age"])
        one_person.add_wife(person.get("wife", None))
        one_person.add_husband(person.get("husband", None))
        person_list1.append(one_person)
    for person in person_list1:
        try:
            if person.wife:
                for object1 in person_list1:
                    if object1.name == person.wife:
                        person.wife = object1
        except AttributeError:
            pass
        try:
            if person.husband:
                for object1 in person_list1:
                    if object1.name == person.husband:
                        person.husband = object1
        except AttributeError:
            pass
    return person_list1
