class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        if person_dict.get("wife") is not None:
            person.wife = person_dict.get("wife")
        if person_dict.get("husband") is not None:
            person.husband = person_dict.get("husband")
        list_of_people.append(person)
    for person_data in list_of_people:
        if hasattr(person_data, "wife"):
            person_data.wife = person_data.people[person_data.wife]
        if hasattr(person_data, "husband"):
            person_data.husband = person_data.people[person_data.husband]
    return list_of_people
