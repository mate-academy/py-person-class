class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    persons = list()
    for human in people:
        persons.append(Person(human["name"], human["age"]))

        persons_index = persons.index(persons[-1])
        if human.get("wife"):
            setattr(persons[persons_index], "wife", human["wife"])
        elif human.get("husband"):
            setattr(persons[persons_index], "husband", human["husband"])

    for person in persons:
        if hasattr(person, "wife"):
            person.wife = Person.people.get(person.wife)
        elif hasattr(person, "husband"):
            person.husband = Person.people.get(person.husband)

    return persons
