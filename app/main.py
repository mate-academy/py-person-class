class Person:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    people = {}


def create_person_list(people: list) -> list:
    result = []
    for pers in people:
        # obj = pers["name"][:]
        obj = Person(pers["name"], pers["age"])
        Person.people[pers["name"]] = obj
        result.append(obj)

    for el in people:
        person_name = el["name"]
        if "wife" in el and el["wife"] is not None:
            (setattr
             (Person.people[person_name],
              "wife",
              Person.people[el["wife"]]))
        if "husband" in el and el["husband"] is not None:
            (setattr
             (Person.people[person_name],
              "husband",
              Person.people[el["husband"]]))

    return result


# people = [
#     {"name": "Ross", "age": 30, "wife": "Rachel"},
#     {"name": "Joey", "age": 29, "wife": None},
#     {"name": "Rachel", "age": 28, "husband": "Ross"}
# ]
#
# person_list = create_person_list(people)
# print(f"people: {people}")
# print(f"Person(objects): {Person.people}")
# print(person_list)
#
# print(person_list[2].name)
# print(person_list[2].husband.name)
# print(person_list[2].husband.wife is person_list[2])
# print(isinstance(person_list[2], Person))
# print(person_list[1].name)
# print(Person.people)
