class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs: any) -> None:
        self.name = name
        self.age = age
        self.wife = kwargs.get("wife")
        self.husband = kwargs.get("husband")
        Person.people[self.name] = self

    def set_partner(self, people: dict) -> type:
        if self.wife is not None:
            self.wife = Person.people.get(self.wife)
            del self.husband
        elif self.husband is not None:
            self.husband = Person.people.get(self.husband)
            del self.wife
        else:
            del self.wife
            del self.husband
        return self


def create_person_list(people: list) -> list:
    list_person = [Person(**person) for person in people]
    return [person.set_partner(Person.people) for person in list_person]
