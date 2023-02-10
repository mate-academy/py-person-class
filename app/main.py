class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    married_people = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        if "wife" in person.keys() and person["wife"]:
            wife = Person(person["name"], person["age"])
            wife.husband = new_person
            new_person.wife = wife
        elif "husband" in person.keys() and person["husband"]:
            husband = Person(person["name"], person["age"])
            husband.wife = new_person
            new_person.husband = husband
        married_people.append(new_person)
    return married_people
