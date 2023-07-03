class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = []
    for human in people:
        persons.append(Person(persons["name"], persons["age"]))
        if human.get("wife"):
            for human1 in people:
                name = persons.get("name")
                wife = persons.get("wife")
                husband = persons.get("husband")
                if wife:
                    Person.people.get(name).wife = Person.people.get(wife)
                if husband:
                    Person.people.get(name).husband = Person.people.get(husband)
            return persons

    return persons
