class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:

        people_data = Person(person["name"], person["age"])

        if "wife" in person:
            for wife in people_data.people.values():
                if wife.name == person["wife"]:
                    people_data.wife = wife
                    wife.husband = people_data

        if "husband" in person:
            for husband in people_data.people.values():
                if husband.name == person["husband"]:
                    people_data.husband = husband
                    husband.wife = people_data

        person_list.append(people_data)

    return person_list
