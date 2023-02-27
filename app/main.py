class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    new_person_list = [Person(person.get("name"), person.get("age")) for person in people_list]

    for person in people_list:
        if person.get("wife"):
            wife = Person.people[person.get("wife")]
            Person.people[person.get("name")].wife = wife

        if person.get("husband"):
            husband = Person.people[person.get("husband")]
            Person.people[person.get("name")].husband = husband

        return new_person_list


#     # print(new_person_list[2].husband)
#
#     for i in new_person_list:
#         print(i.__dict__)
#
#
# people_list = [
#     {"name": "Ross", "age": 30, "wife": "Rachel"},
#     {"name": "Joey", "age": 29, "wife": None},
#     {"name": "Rachel", "age": 28, "husband": "Ross"}
# ]
#
# create_person_list(people_list)
#

