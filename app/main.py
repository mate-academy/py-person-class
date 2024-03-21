class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(list_of_people: list) -> list:
    our_list = []

    for person in list_of_people:
        person = Person(person["name"], person["age"])
        our_list.append(person)

    for person in list_of_people:
        if person.get("wife"):
            wife_name = person["wife"]
            wife = Person.people[wife_name]
            name_of_person = person["name"]
            person = Person.people[name_of_person]
            person.wife = wife
        elif person.get("husband"):
            husband_name = person["husband"]
            husband = Person.people[husband_name]
            name_of_person = person["name"]
            person = Person.people[name_of_person]
            person.husband = husband

    return our_list
