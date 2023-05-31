class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []
    for person_dict in people:
        person = Person(person_dict.get("name"), person_dict.get("age"))
        person_list.append(person)
    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if person_dict.get("wife") is not None:
            person.wife = Person.people[person_dict["wife"]]
        elif person_dict.get("husband") is not None:
            person.husband = Person.people[person_dict["husband"]]
    return person_list


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

person_list = create_person_list(people)

print(isinstance(person_list[0], Person))  # True
print(person_list[0].name == "Ross")  # True
print(person_list[0].wife is person_list[2])  # True
print(person_list[0].wife.name == "Rachel")  # True

print(person_list[1].name == "Joey")  # True
print(person_list[1].wife is None)  # True

print(isinstance(person_list[2], Person))  # True
print(person_list[2].name == "Rachel")  # True
print(person_list[2].husband is person_list[0])  # True
print(person_list[2].husband.name == "Ross")  # True
print(person_list[2].husband.wife is person_list[2])  # True

print(Person.people)
