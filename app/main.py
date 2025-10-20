class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife"):
            wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife
        if person.get("husband"):
            husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband

    return person_list


### My Debuger
"""
people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"},
    {"name": "Chendler", "age": 30, "wife": "Monica"},
    {"name": "Monica", "age": 28, "husband": "Chendler"},
    {"name": "Phoebe", "age": 29, "husband": "Mike"},
    {"name": "Mike", "age": 28, "wife": "Phoebe"}
]

person_list = create_person_list(people)

for i in range(len(people)):

    if hasattr(person_list[i], "husband"):
        wh_name = person_list[i].husband.name
        wh_type = type(person_list[i].husband)
        wh_instance = person_list[i].husband
    elif hasattr(person_list[i], "wife"):
        wh_name = person_list[i].wife.name
        wh_type = type(person_list[i].wife)
        wh_instance = person_list[i].wife
    else:
        wh_name = "No wife or husband"
        wh_type = "No type"
        wh_instance = "No instance"

    print("-" * 20)
    print(person_list[i].name, person_list[i].age, "husband/wife: ", wh_name)
    print(f"Instance: {wh_instance} of type: {wh_type}")

print("-" * 80)
# print(Person.people)
"""
