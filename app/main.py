class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> None:
    person_list = [Person(person_dict["name"], person_dict["age"])
                   for person_dict in people]

    for person_dict in people:
        if person_dict.get("wife") is not None:
            Person.people[person_dict["name"]].wife = Person.people[
                person_dict.get("wife")]

        elif person_dict.get("husband") is not None:
            Person.people[person_dict["name"]].husband = Person.people[
                person_dict.get("husband")]

    return person_list
