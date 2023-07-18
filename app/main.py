class Person:
    people = {}  # Initialize as an empty dictionary

    def __init__(self, name, age, wife=None, husband=None):
        self.name = name
        self.age = age
        self.wife = wife
        self.husband = husband
        Person.people[name] = self


def create_person_list(people):
    for p in people:
        name = p["name"]
        age = p["age"]
        spouse_name = p.get("wife") or p.get("husband")
        person = Person(name, age)
        if spouse_name:
            if spouse_name in Person.people:
                spouse = Person.people[spouse_name]
                if "wife" in p:
                    person.wife = spouse
                else:
                    person.husband = spouse
                if spouse.wife is None and "wife" in p:
                    spouse.wife = person
                elif spouse.husband is None and "husband" in p:
                    spouse.husband = person
            else:
                # Handle spouse not found
                if "wife" in p:
                    person.wife = None
                else:
                    person.husband = None

    return list(Person.people.values())


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
