class Person:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    people = {}


def create_person_list(people: list) -> list:
    result = []
    for pers in range(len(people)):
        obj = people[pers]
        the_name = obj["name"][:]
        the_name = Person(obj["name"], obj["age"])
        Person.people[obj["name"][:]] = the_name
        if "wife" in obj:
            setattr(the_name, "wife", obj["wife"])
        if "husband" in obj:
            setattr(the_name, "husband", obj["husband"])

        result.append(the_name)

    for el in result:
        if hasattr(el, "wife"):
            if el.wife is not None:
                for obj_el in result:
                    if obj_el.name == el.wife:
                        el.wife = obj_el
            else:
                delattr(el, "wife")
        if hasattr(el, "husband"):
            print(el.husband)
            if el.husband is not None:
                for obj_el in result:
                    if obj_el.name == el.husband:
                        el.husband = obj_el
            else:
                delattr(el, "husband")
    return result

# people = [
#     {"name": "Ross", "age": 30, "wife": "Rachel"},
#     {"name": "Joey", "age": 29, "wife": None},
#     {"name": "Rachel", "age": 28, "husband": "Ross"}
# ]
#
# person_list = create_person_list(people)
# print(Person.people)
# print(person_list[2].name)
# print(person_list[2].husband.name)
# print(person_list[2].husband.wife is person_list[2])
# print(isinstance(person_list[2], Person))
# print(person_list[1].name)
