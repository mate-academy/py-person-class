class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_info in people:
        name = person_info["name"]
        age = person_info["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_info in people:
        person = Person.people[person_info["name"]]

        if "wife" in person_info and person_info["wife"]:
            wife = Person.people.get(person_info["wife"])
            if wife:
                person.wife = wife
                wife.husband = person

        if "husband" in person_info and person_info["husband"]:
            husband = Person.people.get(person_info["husband"])
            if husband:
                person.husband = husband
                husband.wife = person

    return person_list
