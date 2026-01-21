class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_people = []
    for person in people:
        list_people.append(Person(person["name"], person["age"]))

    for person_in_list in people:
        if "wife" in person_in_list and person_in_list["wife"]:
            wife = Person.people.get(person_in_list["wife"])
            if wife:
                Person.people[person_in_list["name"]].wife = wife
                wife.husband = Person.people[person_in_list["name"]]

        if "husband" in person_in_list and person_in_list["husband"]:
            husband = Person.people.get(person_in_list["husband"])

            if husband:
                Person.people[person_in_list["name"]].husband = husband
                husband.wife = Person.people[person_in_list["name"]]

    return list_people
