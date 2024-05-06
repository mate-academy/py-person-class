class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list[dict]) -> list:
    ans_list: list = []
    for person in people:
        person_inst = Person(
            name=person["name"],
            age=person["age"]
        )
        ans_list.append(person_inst)

    for index, person in enumerate(people):
        if person.get("wife"):
            ans_list[index].wife = Person.people[person["wife"]]
        elif person.get("husband"):
            ans_list[index].husband = Person.people[person["husband"]]

    return ans_list