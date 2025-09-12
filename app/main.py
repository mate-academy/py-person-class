class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [
        Person(person_input["name"], person_input["age"])
        for person_input in people
    ]

    for person_input in people:
        wife_name = person_input.get("wife")
        if wife_name:
            wife_ref = Person.people.get(wife_name)
            if wife_ref is not None:
                Person.people[person_input["name"]].wife = wife_ref

        husband_name = person_input.get("husband")
        if husband_name:
            husband_ref = Person.people.get(husband_name)
            if husband_ref is not None:
                Person.people[person_input["name"]].husband = husband_ref

    return result
