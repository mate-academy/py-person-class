class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    new_people_list = []
    for person in people:
        new_people_list.append(Person(person["name"], person["age"]))
    for index, dict_person in enumerate(people):
        if "wife" in dict_person:
            new_people_list[index].wife = dict_person["wife"]
        else:
            new_people_list[index].husband = dict_person["husband"]
    for men in new_people_list:
        for women in new_people_list:
            if men.wife == women.name:
                men.wife = women
                women.husband = men
    for single in new_people_list:
        if single.wife is None:
            del single.wife
        if single.husband is None:
            del single.husband
    return new_people_list
