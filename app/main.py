class Person:
    people = {}

    def __init__(self, name: str, age: int, ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = []

    for individ in people:
        list_of_people.append(Person(individ["name"], individ["age"]))

    for individ in people:
        if individ.get("wife"):
            wife_reference = Person.people[individ["wife"]]
            Person.people[individ["name"]].wife = wife_reference

        if individ.get("husband"):
            husband_reference = Person.people[individ["husband"]]
            Person.people[individ["name"]].husband = husband_reference

    return list_of_people
