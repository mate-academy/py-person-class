class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(incoming_list: list) -> list:
    persons_list = [Person(part_of_list["name"], part_of_list["age"])
                    for part_of_list in incoming_list]

    for index, part_of_list in enumerate(incoming_list):
        if part_of_list.get("wife"):
            persons_list[index].wife = Person.people[
                part_of_list.get("wife")]

        if part_of_list.get("husband"):
            persons_list[index].husband = Person.people[
                part_of_list.get("husband")]

    return persons_list
