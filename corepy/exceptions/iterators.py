iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
iterator = iter(iterable)
print(next(iterator))  # Spring
print(next(iterator))  # Summer
print(next(iterator))  # Autumn
print(next(iterator))  # Winter
print(next(iterator))  # StopIteration exception
