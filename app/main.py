class Person:
    person_list = {}
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.person_list[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        if person.get('wife') != None:
            person["wife"] = Person.person_list.get(person["name"])
        if person.get('husband') != None:
            person["husband"] = Person.person_list.get(person["name"])
    print(people)

    # print(Person.person_list)
    # new_arr = []
    # for person in people:
    #      if person.get("name") in Person.person_list:
    #          new_arr.append({person.get("name"): person})
    #          # Person.person_list[person.get("name")] = person
    #
    # print(new_arr)

    # for person in Person.person_list:
    #     print(person)
# if  person's key wife/husband is not None - create_person_list
# should add attribute wife/husband respectively to its instance.
# This attribute should be a link to a Person instance
# with name the same as wife/husband key in person's dict.

people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

person_1 = Person("Rachel", 25)
person_2 = Person("Joey", 35)
person_3 = Person("Ross", 36)
create_person_list(people)

#print(Person.person_list)
