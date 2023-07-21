class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        Person.people[name] = self

    def get_wife(self) -> None:

        return self.wife

    def get_husband(self) -> None:

        return self.husband


def create_person_list(people: [dict]) -> None:
    person_list = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)

    for person in person_list:
        for person_data in people:
            if person.name == person_data["name"]:
                if "wife" in person_data and person_data["wife"]:
                    person.wife = Person.people[person_data["wife"]]
                if "husband" in person_data and person_data["husband"]:
                    person.husband = Person.people[person_data["husband"]]

    return person_list
