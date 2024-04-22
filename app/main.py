class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person_dict in people:
        Person(name=person_dict["name"], age=person_dict["age"])

    for person_dict in people:
        current_person = Person.people.get(person_dict["name"])
        if "wife" in person_dict and person_dict["wife"]:
            current_person.wife = Person.people.get(person_dict["wife"])
            if current_person.wife:
                current_person.wife.husband = current_person
        if "husband" in person_dict and person_dict["husband"]:
            current_person.husband = Person.people.get(person_dict["husband"])
            if current_person.husband:
                current_person.husband.wife = current_person

    return list(Person.people.values())
