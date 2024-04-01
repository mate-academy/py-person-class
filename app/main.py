class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        name = person["name"]
        age = person["age"]
        new_person = Person(name, age)

        if person.get("wife"):
            new_person.wife = Person.people.get(person["wife"])
            if new_person.wife:
                new_person.wife.husband = new_person
        elif person.get("husband"):
            new_person.husband = Person.people.get(person["husband"])
            if new_person.husband:
                new_person.husband.wife = new_person

        person_list.append(new_person)

    return person_list
