# Check Your Code Against the Following Points

## Code Style

1. Use descriptive and correct variable names.

Good example:

```python
def get_full_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"
```

Bad example:
```python
def get_full_name(x: str, y: str) -> str:
    return f"{x} {y}"
```

2. Avoid nested `if` by using `and`, `or` logical operators.
3. When creating a list of instances from a collection (such as a list of dictionaries), it is  recommended to use **list comprehension** rather than traditional `for` loops. 
4. When accessing values in a dictionary, it is better to use the `dict.get()` method instead of explicitly checking for the presence of a key. This approach simplifies the code and avoids potential `KeyError` exceptions, making it cleaner and more concise.

 Cood example:

```python
if person.get('wife'):
    pass
```

 Bad example:
```python
if "wife" in person and person["wife"]:
    pass
```
## Clean Code
There is no need to add comments to the code as it is clear and self-explanatory.
