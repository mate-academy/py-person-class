class Person:
    people = {}

    def __init__(self, name: str, age: int, *args) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list[Person]:

    persons = [Person(temp_person["name"], temp_person["age"])
               for temp_person in people_list
               ]

    for person, value in zip(persons, people_list):
        if value.get("wife"):
            wife = Person.people.get(value["wife"])
            if wife:
                person.wife = wife
        if value.get("husband"):
            husband = Person.people.get(value["husband"])
            if husband:
                person.husband = husband
    return persons
