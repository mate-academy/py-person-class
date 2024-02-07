class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []

    for person in people:
        name = person["name"]
        age = person["age"]
        new_person = Person(name, age)
        people_list.append(new_person)

        if "wife" in person:
            wife_name = person["wife"]
            if wife_name in Person.people:
                wife_instance = Person.people[wife_name]
                new_person.wife = wife_instance
                wife_instance.husband = new_person

        elif "husband" in person:
            husband_name = person["husband"]
            if husband_name in Person.people:
                husband_instance = Person.people[husband_name]
                new_person.husband = husband_instance
                husband_instance.wife = new_person

    return people_list
