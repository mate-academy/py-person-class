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

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(people)


# @timer
def create_person_list(people: list) -> list:
    # res = []  # [i for i in range(100_000_000)]
    # for i in range(100_000_000):
    #     res.append(i)
    # print(len(res))
    print([Person(current["name"], current["age"]) for current in people])
    return [Person(current["name"], current["age"]) for current in people]


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

person_list = create_person_list(people)
