class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Creating instances
    result = [
        Person(person.get("name"), person.get("age")) for person in people
    ]

    # Setting husbands/wives to created persons
    for person in people:
        if person.get("wife") is not None:
            wife = Person.people.get(person["wife"])
            Person.people.get(person["name"]).wife = wife
        if person.get("husband") is not None:
            husband = Person.people.get(person["husband"])
            Person.people.get(person["name"]).husband = husband
    return result
