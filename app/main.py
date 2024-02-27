class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people = {person_info["name"]: Person(person_info["name"],
                                                 person_info["age"])
                     for person_info in people}
    for person_info in people:
        person_instance = Person.people[person_info["name"]]
        if "wife" in person_info and \
                (wife_name := person_info["wife"]):
            person_instance.wife = Person.people[wife_name]
        if "husband" in person_info and \
                (husband_name := person_info["husband"]):
            person_instance.husband = Person.people[husband_name]

    return list(Person.people.values())
