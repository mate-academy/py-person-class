class Person:
    people = {}

    def __init__(self,
                 name: str,
                 age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = []
    for citizen in people:
        person = Person(citizen["name"], citizen["age"])
        persons.append(person)

    for citizen in people:
        spouse_name = citizen.get("wife")
        if spouse_name is not None:
            person = Person.people[citizen["name"]]
            spouse = Person.people[citizen["wife"]]
            person.wife = spouse
            spouse.husband = person

    return persons
