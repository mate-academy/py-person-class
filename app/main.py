class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        name = person_data["name"]
        person = Person.people[name]

        wife_name = person_data.get("wife")
        if wife_name is not None:
            person.wife = Person.people[wife_name]
        husband_name = person_data.get("husband")
        if husband_name is not None:
            person.husband = Person.people[husband_name]
    return person_list


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
