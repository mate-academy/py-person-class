class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    result = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person_dict in people:
        current_person = Person.people[person_dict["name"]]
        if person_dict.get("wife") :
            wife_person = Person.people[person_dict["wife"]]
            current_person.wife = wife_person
        if person_dict.get("husband") :
            husband_person = Person.people[person_dict["husband"]]
            current_person.husband = husband_person
    return result
