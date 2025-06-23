class Person:
    people = {}

    def __init__(self, name: str, age: int, *args, **kwargs) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_people = []

    for person in people:
        list_of_people.append(Person(person["name"], person["age"]))

    for person in people:
        print(Person.people[person["name"]])
        person_instance = Person.people[person["name"]]
        if person.get("wife") is not None:
            person_instance.wife = Person.people[person["wife"]]
        if person.get("husband") is not None:
            person_instance.husband = Person.people[person["husband"]]

    return list_of_people


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
