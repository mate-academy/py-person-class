class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self

    @property
    def wife(self) -> "Person":
        return self._wife

    @wife.setter
    def wife(self, person: "Person") -> None:
        if person is not None and person.name != self.name:
            self._wife = person
            person._husband = self

    @property
    def husband(self) -> "Person":
        return self._husband

    @husband.setter
    def husband(self, person: "Person") -> None:
        if person is not None and person.name != self.name:
            self._husband = person
            person._wife = self


def create_person_list(people: list) -> list:
    people_instances = []

    for data in people:
        person = Person(data["name"], data["age"])
        people_instances.append(person)

    for data in people:
        person = Person.people[data["name"]]
        if "wife" in data and data["wife"] is not None:
            wife = Person.people.get(data["wife"])
            if wife:
                person.wife = wife
        if "husband" in data and data["husband"] is not None:
            husband = Person.people.get(data["husband"])
            if husband:
                person.husband = husband

    return people_instances
