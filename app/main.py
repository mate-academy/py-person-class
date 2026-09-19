class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_x = Person(person["name"], person["age"])
        if person.get("husband") is not None:
            person_x.husband = person["husband"]
        if person.get("wife") is not None:
            person_x.wife = person["wife"]
        person_list.append(person_x)

    for person_x in person_list:
        if getattr(person_x, "husband", None) is not None:
            for person_y in person_list:
                if person_y.name == person_x.husband:
                    person_x.husband = person_y
        if getattr(person_x, "wife", None) is not None:
            for person_y in person_list:
                if person_y.name == person_x.wife:
                    person_x.wife = person_y
    return person_list
