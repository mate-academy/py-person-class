class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int,
    ) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    @classmethod
    def get_people_by_name(cls, people_name: str) -> object:
        return cls.people.get(people_name)


def create_person_list(people: list) -> list:
    person_objects = [Person(raw_person["name"], raw_person["age"])
                      for raw_person in people]

    for raw_person in people:
        person = Person.get_people_by_name(raw_person["name"])
        if raw_person.get("wife"):
            person.wife = Person.get_people_by_name(raw_person["wife"])
        elif raw_person.get("husband"):
            person.husband = Person.get_people_by_name(raw_person["husband"])

    return person_objects
