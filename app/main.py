class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for row_dict in people:
        person = Person(row_dict["name"], row_dict["age"])
        person_instances.append(person)

    for row_dict in people:
        if row_dict.get("wife"):
            Person.people[row_dict.get("name")].wife \
                = Person.people[row_dict.get("wife")]
        if row_dict.get("husband"):
            Person.people[row_dict.get("name")].husband \
                = Person.people[row_dict.get("husband")]
    return person_instances
