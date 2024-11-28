class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        if name not in Person.people:
            Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people: list) -> list:
    person_list = []

    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]

        if name not in Person.people:
            person = Person(name, age)
        else:
            person = Person.people[name]

        person_list.append(person)

    for person_dict in people:
        person = Person.people[person_dict["name"]]

        if "wife" in person_dict and person_dict["wife"]:
            spouse_name = person_dict["wife"]
            if spouse_name in Person.people:
                person.wife = Person.people[spouse_name]

        if "husband" in person_dict and person_dict["husband"]:
            spouse_name = person_dict["husband"]
            if spouse_name in Person.people:
                person.husband = Person.people[spouse_name]

    return person_list
