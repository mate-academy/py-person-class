class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    def get_hsbn_or_wife(other_people: list, target: str) -> dict | None:
        for value in other_people:
            if value["name"] == target:
                return value
        return None

    def set_lovers(human_1: Person, role_1: str, human_2: Person) -> None:
        if role_1 == "wife":
            human_1.wife = human_2
            human_2.husband = human_1

        else:
            human_2.wife = human_1
            human_1.husband = human_2

    answer = []

    for index, human in enumerate(people):
        if human["name"] in Person.people.keys():
            answer.append(Person.people[human["name"]])
            continue

        Person.people[human["name"]] = Person(human["name"], human["age"])
        answer.append(Person.people[human["name"]])
        role_person_2 = list(human.keys())[-1]

        if human[role_person_2] is not None:

            second_human = get_hsbn_or_wife(
                people[index + 1:], human[role_person_2])

            Person.people[human[role_person_2]] = Person(
                second_human["name"], second_human["age"])

            set_lovers(Person.people[human["name"]],
                       role_person_2,
                       Person.people[human[role_person_2]])

    return answer
