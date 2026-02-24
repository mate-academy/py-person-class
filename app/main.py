class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    persons_list = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person_data in people:
        current_person = Person.people[person_data["name"]]
        if person_data.get("wife"):
            wife_obj = Person.people[person_data["wife"]]
            current_person.wife = wife_obj
            wife_obj.husband = current_person
        if person_data.get("husband"):
            husband_obj = Person.people[person_data["husband"]]
            current_person.husband = husband_obj
            husband_obj.wife = current_person

    return persons_list
