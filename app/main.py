class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_data, person_inst in zip(people, person_list):
        if person_data.get("wife"):
            person_inst.wife = Person.people.get(person_data["wife"])
        if person_data.get("husband"):
            person_inst.husband = Person.people.get(person_data["husband"])

    return person_list
