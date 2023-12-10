class Person:
    people = {}

    def __init__(self, name: str, age: int, *args) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        person_instance = Person(name, age)
        if person.get("wife") is not None:
            person_instance.wife = Person.people.get(person["wife"])
            if person_instance.wife is not None:
                person_instance.wife.husband = person_instance
        elif person.get("husband") is not None:
            person_instance.husband = Person.people.get(person["husband"])
            if person_instance.husband is not None:
                person_instance.husband.wife = person_instance
        person_list.append(person_instance)
    return person_list
