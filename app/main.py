class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        people_list.append(person)
    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"]:
            spouse = Person.people.get(person_dict["wife"])
            if spouse:
                person.wife = spouse
        if "husband" in person_dict and person_dict["husband"]:
            spouse = Person.people.get(person_dict["husband"])
            if spouse:
                person.husband = spouse
    return people_list
