class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = [Person(person.get("name"), person.get("age"))
                   for person in people]

    for person in people:
        name = person.get("name")
        obj = Person.people[name]
        if "wife" in person and person.get("wife") is not None:
            wife_name = person.get("wife")
            obj.wife = Person.people[wife_name]
        elif "husband" in person and person.get("husband") is not None:
            husband_name = person.get("husband")
            obj.husband = Person.people[husband_name]

    return result_list
