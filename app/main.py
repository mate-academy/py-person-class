class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for person in people:
        result_list.append(Person(
            name=person.get("name"),
            age=person.get("age")
        ))
    for person in people:
        if "wife" in person and person.get("wife") is not None:
            husband_name = person.get("name")
            husband = Person.people.get(husband_name)
            wife_name = person.get("wife")
            wife = Person.people.get(wife_name)
            husband.wife = wife
            wife.husband = husband

    return result_list
