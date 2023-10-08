class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        get_person = Person.people[person["name"]]
        if person.get("wife"):
            person.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            get_person.husband = Person.people[person["husband"]]
    return people_list


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

person_list = create_person_list(people)
ab = Person.people
ac = (ab["name"])
