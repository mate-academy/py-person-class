class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_list: list[dict]) -> list[Person]:
    Person.people.clear()

    created_people = [
        Person(
            person_dict["name"],
            person_dict["age"]
        )
        for person_dict in people_list
    ]

    for person_dict in people_list:
        person_obj = Person.people[person_dict["name"]]
        if person_dict.get("wife"):
            person_obj.wife = Person.people[person_dict["wife"]]
            Person.people[person_dict["wife"]].husband = person_obj
        if person_dict.get("husband"):
            person_obj.husband = Person.people[person_dict["husband"]]
            Person.people[person_dict["husband"]].wife = person_obj
    return created_people
