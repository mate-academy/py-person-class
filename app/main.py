class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        person_instance = Person.people[person["name"]]
        wife_name = person.get("wife")
        if wife_name:
            person_instance.wife = Person.people.get(wife_name)
        husband_name = person.get("husband")
        if husband_name:
            person_instance.husband = Person.people.get(husband_name)
    return persons
