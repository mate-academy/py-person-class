class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # self.wife = None
        # self.husband = None


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        pers = Person(person["name"], person["age"])

        if "wife" in person and person["wife"] is not None:
            pers.wife = person["wife"]
        if "husband" in person and person["husband"] is not None:
            pers.husband = person["husband"]

        person_list.append(pers)
        Person.people[person["name"]] = pers

    for person in person_list:

        if hasattr(person, "wife") and person.wife is not None:
            person.wife = Person.people[person.wife]

        if hasattr(person, "husband") and person.husband is not None:
            person.husband = Person.people[person.husband]

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

    if hasattr(person_list[i] ,"husband"):
        wh_name = person_list[i].husband.name
    elif hasattr(person_list[i], "wife"):
        wh_name = person_list[i].wife.name
    else: wh_name = None

    print("-" * 20)
    print(person_list[i].name, person_list[i].age, "husband/wife: ", wh_name)

print("-" * 80)
print(Person.people)
"""
