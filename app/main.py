class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    personal_list = [
        Person(one_people["name"], one_people["age"]) for one_people in people
    ]

    for one_people in people:
        if "wife" in one_people and one_people["wife"] is not None:
            Person.people[one_people["name"]].wife\
                = Person.people[one_people["wife"]]

        if "husband" in one_people and one_people["husband"] is not None:
            Person.people[one_people["name"]].husband\
                = Person.people[one_people["husband"]]

    return personal_list
#
# people = [
#     {"name": "Ross", "age": 30, "wife": "Rachel"},
#     {"name": "Joey", "age": 29, "wife": None_people},
#     {"name": "Rachel", "age": 28, "husband": "Ross"}
# ]
#
# create_person_list(people)

# person_list = create_person_list(people)
# isinstance(person_list[0], Person) # True
# person_list[0].name == "Ross"
# person_list[0].wife is person_list[2] # True
# person_list[0].wife.name == "Rachel"
#
# person_list[1].name == "Joey"
# person_list[1].wife
# # AttributeError
#
# isinstance(person_list[2], Person) # True
# person_list[2].name == "Rachel"
# person_list[2].husband is person_list[0] # True
# # The same as person_list[0]
# person_list[2].husband.name == "Ross"
# person_list[2].husband.wife is person_list[2]  # True
#
# Person.people == {
#     "Ross": <__main__.Person object at 0x10c20ca60>,
#     "Joey": <__main__.Person object at 0x10c180a00>,
#     "Rachel": <__main__.Person object at 0x10c1804f0>
# }
