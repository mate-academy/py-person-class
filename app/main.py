class Person:
    people = {}

    def __init__(
        self,
        name: str,
        age: int
    ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instance = []
    for person in people:
        person_data = Person(person["name"], person["age"])
        person_instance.append(person_data)

    for person in people:
        person_data = Person.people[person["name"]]
        wife = person.get("wife")
        husband = person.get("husband")
        if wife:
            person_data.wife = Person.people[wife]
        elif husband:
            person_data.husband = Person.people[husband]

    return person_instance
