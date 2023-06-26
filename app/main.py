class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    answer = {}
    for i in people:
        answer[i["name"]] = Person(list(i.items())[0][1],
                                   list(i.items())[1][1])
    for ob in people:
        if ob.get("husband") is not None:
            answer[ob["name"]].husband = answer[ob.get("husband")]
        elif ob.get("wife") is not None:
            answer[ob["name"]].wife = answer[ob.get("wife")]

    Person.people = answer
    return list(answer.values())
