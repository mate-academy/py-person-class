class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    Person.people = {}
    persons = [Person(d["name"], d["age"]) for d in people]
    for data in people:
        person = Person.people[data["name"]]
        for key in ("wife", "husband"):
            partner_name = data.get(key)
            if partner_name is None:
                continue
            if partner_name in Person.people:
                setattr(person, key, Person.people[partner_name])

    return persons


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"},
]

#
#
# person_list = create_person_list(people)
# print(isinstance(person_list[0], Person))  # True
# print(person_list[0].name) # "Ross"
# print(person_list[0].wife is person_list[2])  # True
# print(person_list[0].wife.name)# "Rachel"
#
# print(person_list[1].name)# "Joey"
# print(person_list[1].wife)
# # AttributeError
#
# print(isinstance(person_list[2], Person))  # True
# print(person_list[2].name) #"Rachel"
# print(person_list[2].husband is person_list[0])  # True
# # The same as person_list[0]
# print(person_list[2].husband.name)# "Ross"
# print(person_list[2].husband.wife is person_list[2])  # True
# #
# # Person.people == {
# #     "Ross": <__main__.Person object at 0x10c20ca60>,
# #     "Joey": <__main__.Person object at 0x10c180a00>,
# #     "Rachel": <__main__.Person object at 0x10c1804f0>
# # }
