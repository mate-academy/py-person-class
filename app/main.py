class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    final_list = []

    for human in people:
        person_object = (
            Person(human["name"], human["age"])
            if human["name"] not in Person.people
            else Person.people[human["name"]]
        )
        final_list.append(person_object)

    for human in people:
        husband_wife = "husband" if "husband" in human else "wife"
        name_of_husband_wife = human[husband_wife]

        if name_of_husband_wife:
            wife_husband_object = None

            if name_of_husband_wife in Person.people:
                wife_husband_object = Person.people[name_of_husband_wife]

            if husband_wife == "wife":
                Person.people[human["name"]].wife = wife_husband_object
            else:
                Person.people[human["name"]].husband = wife_husband_object
    return final_list
