class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_instances = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people_list
    ]

    for human in people_list:
        if human.get("wife") is not None:
            human_in_people = Person.people[human["name"]]
            human_in_people.wife = Person.people[human["wife"]]
        if human.get("husband") is not None:
            human_in_people = Person.people[human["name"]]
            human_in_people.husband = Person.people[human["husband"]]
    return person_instances

# people = [
#     {"name": "Ross", "age": 30, "wife": "Rachel"},
#     {"name": "Joey", "age": 29, "wife": None},
#     {"name": "Rachel", "age": 28, "husband": "Ross"}
# ]
# #
# person_list = create_person_list(people)
# print(person_list)
# print(Person.people)
# print(Person.people["Rachel"].husband.name)
# # for person_dict in people_list:
# #     name = person_dict["name"]
# #     age = person_dict["age"]
# #     person_instance = Person(name, age)
# #     person_instances.append(person_instance)
