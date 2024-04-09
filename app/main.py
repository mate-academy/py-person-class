class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # self.spouse = None
        Person.people[self.name] = self

    def __str__(self) -> str:
        return f"{self.name}, {self.age}"


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        person_list.append(Person(person_data["name"], person_data["age"]))
    for person in people:
        person_instance = Person.people.get(person["name"])
        if person.get("wife"):
            person_instance.wife = Person.people[person["wife"]]
        if person.get("husband"):
            person_instance.husband = Person.people[person["husband"]]
    return person_list


if __name__ == "__main__":
    people = [
        {"name": "Ross", "age": 30, "wife": "Rachel"},
        {"name": "Joey", "age": 29, "wife": None},
        {"name": "Rachel", "age": 28, "husband": "Ross"},
    ]

    person_list = create_person_list(people)
    print(isinstance(person_list[0], Person))  # True
    print(person_list[0].name == "Ross")
    print(person_list[0].wife is person_list[2])  # True
    print(person_list[0].wife.name)  # == "Rachel"

    for person_instance in create_person_list(people):
        print(person_instance)
