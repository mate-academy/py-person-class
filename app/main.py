class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for dict_person in people:
        person = Person(dict_person["name"], dict_person["age"])
        # wife_name = Person.people.get(dict_person["wife"], False)
        # if wife_name:
        #     # wife_name = dict_person["wife"]
        #     person.wife = Person.people.get(wife_name)
        #     # wife =
        #     # person.wife = Person.people[person["wife"]]
        #     # person.wife = Person.people[f'{dict_person["name"]}']
        #
        # husband_name = Person.people.get(dict_person["husband"], False)
        # if husband_name:
        #     # husband_name = dict_person["husband"]
        #     person.husband = Person.people.get(husband_name)
        #     # person.husband = Person.people[dict_person["husband"]]

        person_list.append(person)

    return person_list
