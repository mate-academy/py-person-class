from __future__ import annotations


class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people_list: list) -> list:
    person_list = []
    for pers in people_list:
        name = pers["name"]
        age = pers["age"]
        new_person = Person(name, age)
        wife, husband = pers.get("wife"), pers.get("husband")
        if wife:
            new_person.wife = wife
        if husband:
            new_person.husband = husband
        person_list.append(new_person)
    for human in person_list:
        if "wife" in human.__dict__.keys():
            wife_name = human.wife
            human.wife = Person.people.get(wife_name)
        if "husband" in human.__dict__.keys():
            husband_name = human.husband
            human.husband = Person.people.get(husband_name)
    return person_list

peoples = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]




person_list = create_person_list(peoples)
print(isinstance(person_list[0], Person))


print(Person.people)

print(person_list)
#
#
#
#
#
print(person_list[0].wife is person_list[2])
print(person_list[0].wife.name)
