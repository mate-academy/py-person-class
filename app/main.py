class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    ans = []
    for person in people:
        ans.append(Person(person.get("name"), person.get("age")))
    for human in people:
        name_pare_w = human.get("wife")
        if name_pare_w is not None:
            Person.people.get(human.get("name")).wife = (
                Person.people.get(name_pare_w))
        name_pare_h = human.get("husband")
        if name_pare_h is not None:
            Person.people.get(human.get("name")).husband = (
                Person.people.get(name_pare_h))
    return ans

#
# people = [
#     {"name": "Ross", "age": 30, "wife": "Rachel"},
#     {"name": "Joey", "age": 29, "wife": None},
#     {"name": "Rachel", "age": 28, "husband": "Ross"}
# ]
#
# person_list = create_person_list(people)
# print(Person.people)
# print(person_list[0])
# print(person_list[0].wife)
