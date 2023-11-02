class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self

    @classmethod
    def get_person(cls, name: str) -> str:
        return cls.people.get(name)


def create_person_list(people: dict) -> list:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_data, person_inst in zip(people, person_list):
        if "wife" in person_data and person_data["wife"]:
            person_inst.wife = Person.get_person(person_data["wife"])
        if "husband" in person_data and person_data["husband"]:
            person_inst.husband = Person.get_person(person_data["husband"])

    return person_list
