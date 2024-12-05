class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list[dict]) -> list[Person]:
    [Person(person["name"], person["age"]) for person in people_list]

    for person in people_list:
        person_instance = Person.people[person["name"]]
        if wife_name := person.get("wife"):
            person_instance.wife = Person.people[wife_name]
        elif husband_name := person.get("husband"):
            person_instance.husband = Person.people[husband_name]

    return list(Person.people.values())
