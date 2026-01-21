class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for person in people:
        item_person = Person(person["name"], person["age"])
        if person.get("wife"):
            wife = Person.people.get(person["wife"])
            if wife:
                item_person.wife = wife
                wife.husband = item_person
        if person.get("husband"):
            husband = Person.people.get(person["husband"])
            if husband:
                item_person.husband = husband
                husband.wife = item_person
        persons.append(item_person)

    return persons
