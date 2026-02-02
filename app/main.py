class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    result = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        wife_name = person.get("wife")
        if wife_name:
            p_obj = Person.people[person["name"]]
            p_obj.wife = Person.people[wife_name]
        husband_name = person.get("husband")
        if husband_name:
            p_obj = Person.people[person["name"]]
            p_obj.husband = Person.people[husband_name]
    return result
