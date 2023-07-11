class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        self.__class__.people[name] = self

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people: list) -> list:
    person_list = []
    person_dict = {}

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)
        person_dict[name] = person

    for person_data in people:
        person = person_dict[person_data["name"]]

        if person_data.get("wife"):
            person.wife = person_dict.get(person_data["wife"])

        if person_data.get("husband"):
            person.husband = person_dict.get(person_data["husband"])

    return person_list
