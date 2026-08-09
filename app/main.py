class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person({self.name}, {self.age})"


def create_person_list(people_list: list) -> list:
    list_person = [
        Person(person["name"], person["age"])
        for person in people_list
    ]

    for i in range(len(people_list)):
        person_dict = people_list[i]
        person_obj = list_person[i]

        if person_dict.get("wife"):
            person_obj.wife = Person.people[person_dict["wife"]]

        if person_dict.get("husband"):
            person_obj.husband = Person.people[person_dict["husband"]]

    return list_person
