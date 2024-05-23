class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> None:
    person_list = []

    person_list.extend([Person
                        (person_dict["name"], person_dict["age"])
                        for person_dict in people])

    for person_dict in people:
        name = person_dict["name"]
        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")

        if wife_name is not None:
            Person.people[name].wife = Person.people[wife_name]
        elif husband_name is not None:
            Person.people[name].husband = Person.people[husband_name]

    return person_list
