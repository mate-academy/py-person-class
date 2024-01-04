# class Person:
#     people = {}
#
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age
#         Person.people.update({name: self})
#
#
# def create_person_list(people: list) -> list:
#     list_of_people = []
#     for d_person in people:
#         c_person = Person(d_person.get("name"), d_person["age"])
#         if "husband" in d_person:
#             if d_person.get("husband") is not None:
#                 c_person.husband = d_person.get("husband")
#         if "wife" in d_person:
#             if d_person.get("wife") is not None:
#                 c_person.wife = d_person.get("wife")
#         list_of_people.append(c_person)
#
#     for person in list_of_people:
#         if hasattr(person, "husband"):
#             if isinstance(person.husband, str):
#                 person.husband = Person.people.get(person.husband)
#         if hasattr(person, "wife"):
#             if isinstance(person.wife, str):
#                 person.wife = Person.people.get(person.wife)
#     return list_of_people
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list) -> list:
    list_of_people = []

    for d_person in people:
        c_person = Person(d_person.get("name"), d_person.get("age"))
        husband = d_person.get("husband")
        wife = d_person.get("wife")

        if husband is not None:
            c_person.husband = husband

        if wife is not None:
            c_person.wife = wife

        list_of_people.append(c_person)

    for person in list_of_people:
        if hasattr(person, "husband"):
            person.husband = Person.people.get(person.husband)

        if hasattr(person, "wife"):
            person.wife = Person.people.get(person.wife)

    return list_of_people
