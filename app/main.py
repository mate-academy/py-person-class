class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_objects = [Person(person["name"], person["age"])
                      for person in people]

    for person_el in people:
        if person_el.get("wife"):
            person_with_wife = Person.people[person_el["name"]]
            person_with_wife.wife = Person.people[person_el["wife"]]

        elif person_el.get("husband"):
            person_with_husband = Person.people[person_el["name"]]
            person_with_husband.husband = Person.people[person_el["husband"]]

    return person_objects
