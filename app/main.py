class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self
        #Person.people[self] = self


def create_person_list(people: list) -> list:
    people_by_name = []
    for person in people:
        person_by_name = Person(person["name"], person["age"])
        people_by_name.append(person_by_name)

    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if person.get("husband"):
            Person.people[person["name"]].husband = Person.people[person["husband"]]

    return people_by_name


# people = [
#     {"name": "Ross", "age": 30, "wife": "Rachel"},
#     {"name": "Joey", "age": 29, "wife": None},
#     {"name": "Rachel", "age": 28, "husband": "Ross"}
# ]
#
#
# person_list = create_person_list(people)
# print(isinstance(person_list[0], Person))
# print(person_list[0].name == "Ross")
# print(person_list[0].wife is person_list[2])