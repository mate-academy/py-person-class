class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    people_list_cls = [Person(p["name"], p["age"]) for p in people]

    for single_person in people:
        person_obj = Person.people[single_person["name"]]

        if single_person.get("wife"):
            person_obj.wife = Person.people[single_person["wife"]]
        if single_person.get("husband"):
            person_obj.husband = Person.people[single_person["husband"]]

    return people_list_cls

# def create_person_list(people: list) -> None:
#     people_list_cls = []
#     for person in people:
#         people_list_cls.append(Person(person["name"], person["age"]))
#
#     a = range(len(people))
#     for i in a:
#         if people[i].get("wife"):
#             wife_name = people[i].get("wife")
#             for single_person in people_list_cls:
#                 if single_person.name == wife_name:
#                     people_list_cls[i].wife = single_person
#
#         if people[i].get("husband"):
#             husband_name = people[i].get("husband")
#             for single_person in people_list_cls:
#                 if single_person.name == husband_name:
#                     people_list_cls[i].husband = single_person
