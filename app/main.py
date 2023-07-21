class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.wife = None
        self.husband = None
        Person.people[name] = self

    def get_wife(self) -> None:

        return self.wife

    def get_husband(self) -> None:

        return self.husband


def create_person_list(people: [dict]) -> None:
    person_list = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)

    for person in person_list:
        for person_data in people:
            if person.name == person_data["name"]:
                if "wife" in person_data and person_data["wife"]:
                    person.wife = Person.people[person_data["wife"]]
                if "husband" in person_data and person_data["husband"]:
                    person.husband = Person.people[person_data["husband"]]

    return person_list


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]


person_list = create_person_list(people)

print(isinstance(person_list[0], Person))  # True
print(person_list[0].name == "Ross")  # True
if person_list[0].wife:
    print(person_list[0].wife.name == "Rachel")  # True
else:
    print(person_list[0].wife)  # None

print(person_list[1].name == "Joey")  # True
if person_list[1].wife:
    print(person_list[1].wife.name)  # None
else:
    print(person_list[1].wife)  # None

print(isinstance(person_list[2], Person))  # True
print(person_list[2].name == "Rachel")  # True
print(person_list[2].husband is person_list[0])  # True
print(person_list[2].husband.name == "Ross")  # True
print(person_list[2].husband.wife is person_list[2])  # True

print(Person.people)
