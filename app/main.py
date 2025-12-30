class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for man in people:
        temp = Person(man["name"], man["age"])
        result.append(temp)
    for i in range(len(people)):
        if "wife" in people[i] and people[i]["wife"] is not None:
            result[i].wife = [
                res for res in result
                for human in people
                if human["name"] == result[i].name
                and res.name == human["wife"]
            ][0]
        if "husband" in people[i] and people[i]["husband"] is not None:
            result[i].husband = [
                res for res in result
                for human in people
                if human["name"] == result[i].name
                and res.name == human["husband"]
            ][0]
    return result
