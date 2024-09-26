class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        attr = person["name"]
        attr = Person(person["name"], person["age"])
        result.append(attr)
        Person.people.update({person["name"]: attr})

    for count_wife in range(len(people)):
        if people[count_wife].get("wife") is not None:
            for count_husband in range(len(people)):
                if people[count_wife]["wife"] == people[count_husband]["name"]:
                    result[count_wife].wife = result[count_husband]
                    result[count_husband].husband = result[count_wife]

    return result
