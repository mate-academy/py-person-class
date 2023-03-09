# import time
#
#
# def timer(func):
#     print("timer")
#
#     def wrapper(*args, **kwargs):
#         print("wrapper")
#         start_ = time.time()
#         func(people)
#         end_ = time.time()
#         print(end_ - start_)
#
#     return wrapper


class Person:
    people = {}
    wife_name = None
    husband_name = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Person.people[name] = self

        print(Person.people)


# @timer
def create_person_list(people: list) -> list:
    to_iterate = people
    print(to_iterate)
    for i in people:
        if "wife" in i.keys():
            print("3d woman exist")
            if i["wife"] is not None:
                print("wife is not None")

    res = [Person(current["name"], current["age"]) for current in to_iterate]
    # res = []  # [i for i in range(100_000_000)]
    # for i in range(100_000_000):
    #     res.append(i)
    # print(len(res))
    return res


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

person_list = create_person_list(people)
print(person_list)

# print(person_list[0].husband)
