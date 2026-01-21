class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # First create all Person instances
    for person_data in people:
        Person(person_data["name"], person_data["age"])

    # Then establish relationships
    for person_data in people:
        current_person = Person.people[person_data["name"]]

        # Check for wife relationship
        if "wife" in person_data and person_data["wife"] is not None:
            spouse_name = person_data["wife"]
            if spouse_name in Person.people:  # Check if spouse exists
                current_person.wife = Person.people[spouse_name]

        # Check for husband relationship
        if "husband" in person_data and person_data["husband"] is not None:
            spouse_name = person_data["husband"]
            if spouse_name in Person.people:  # Check if spouse exists
                current_person.husband = Person.people[spouse_name]

    return [Person.people[p["name"]] for p in people]


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
person_list = create_person_list(people)

print(person_list[2].husband.name)
print(person_list[0].wife.age)
print(person_list[0].wife is person_list[2])
print(person_list[2].husband.age)

print(type(person_list))
