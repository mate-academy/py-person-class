class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for i in range(len(people)):
        person_list.append(Person(people[i]["name"], people[i]["age"]))

    for i in range(len(people)):
        if "wife" in people[i] and people[i]["wife"]:
            person = Person.people[people[i]["name"]]
            wife = Person.people.get(people[i]["wife"])
            if wife:
                person.wife = wife

        if "husband" in people[i] and people[i]["husband"]:
            person = Person.people[people[i]["name"]]
            husband = Person.people.get(people[i]["husband"])
            if husband:
                person.husband = husband

    return person_list
