class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    new_people_list = []
    for dict_pers in people:
        person = Person(dict_pers["name"], dict_pers["age"])
        new_people_list.append(person)
    for person in new_people_list:
        if "wife" in dict_pers:
            person.wife = Person.people[dict_pers["wife"]]
            person.wife.husband = person
        if "husband" in dict_pers:
            person.husband = Person.people[dict_pers["husband"]]
            person.husband.wife = person
    return new_people_list
