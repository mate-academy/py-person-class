class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.__class__.people[name] = self


def create_person_list(people: list[dict[str, str | int]]) -> list[Person]:
    person_list: list[Person] = []
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        person_list.append(person)

    for person_data in people:
        if person_data.get("wife"):
            person = Person.people[person_data["name"]]
            person.wife = Person.people[person_data["wife"]]
            if person.wife:
                person.wife.husband = person
        if person_data.get("husband"):
            person = Person.people[person_data["name"]]
            person.husband = Person.people[person_data["husband"]]
            if person.husband:
                person.husband.wife = person

    return person_list
