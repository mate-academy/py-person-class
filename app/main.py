class Person:
    people = {}
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people: list) -> list:

    res_lis = [Person(person["name"], person["age"]) for person in people]

    for per in people:
        cur_per = Person.people[per["name"]]
        if "wife" in per and per["wife"]:
            cur_per.wife = Person.people[per["wife"]]
        elif "husband" in per and per["husband"]:
            cur_per.husband = Person.people[per["husband"]]
    return res_lis



