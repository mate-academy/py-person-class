class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    if people:
        [Person(person["name"], person["age"]) for person in people]
        for person in people:
            obj = Person.people[person["name"]]
            wife_name = person.get("wife")
            husband_name = person.get("husband")
            if wife_name is not None:
                obj.wife = Person.people[wife_name]
            if husband_name is not None:
                obj.husband = Person.people[husband_name]
    return [Person.people[person["name"]] for person in people]
