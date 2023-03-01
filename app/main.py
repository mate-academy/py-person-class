class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    final_list = []

    for human in people:
        person_object = Person(human["name"], human["age"]) \
            if human["name"] not in Person.people \
            else Person.people[human["name"]]
        final_list.append(person_object)

    for human in people:
        wife_husband = "wife" if "wife" in human else "husband"
        name_of_wife_husband = human[wife_husband]

        print(name_of_wife_husband)

        if name_of_wife_husband:
            wife_husband_object = None

            print(human["name"], "human[name]")

            if name_of_wife_husband not in Person.people:
                wife_husband_object = Person(name_of_wife_husband, 0)
            else:
                wife_husband_object = Person.people[name_of_wife_husband]

            if wife_husband == "wife":
                Person.people[human["name"]].wife = wife_husband_object
            else:
                Person.people[human["name"]].husband = wife_husband_object

    return final_list


# people = [
#     {"name": "Ross", "age": 30, "wife": "Rachel"},
#     {"name": "Joey", "age": 29, "wife": None},
#     {"name": "Rachel", "age": 28, "husband": "Ross"}
# ]
