import datetime
from multiprocessing import Pool, cpu_count
from time import time
from tqdm import tqdm


def abstractfunc(func):
    func.__isabstract__ = True
    return func


class Interface(type):

    def __init__(self, name, bases, _namespace):
        for base in bases:
            must_implement = getattr(base, 'abstract_methods', [])
            class_methods = getattr(self, 'all_methods', [])
            for method in must_implement:
                if method not in class_methods:
                    err_str = f"""Can't create abstract class {name}!
                    {name} must implement abstract method {method} of class {base.__name__}!"""
                    raise TypeError(err_str)

    def __new__(metaclass, name, bases, namespace):
        namespace['abstract_methods'] = Interface._get_abstract_methods(namespace)
        namespace['all_methods'] = Interface._get_all_methods(namespace)
        cls = super().__new__(metaclass, name, bases, namespace)
        return cls

    def _get_abstract_methods(namespace):
        return [name for name, val in namespace.items() if callable(val) and getattr(val, '__isabstract__', False)]

    def _get_all_methods(namespace):
        return [name for name, val in namespace.items() if callable(val)]


class ShapeInterface(metaclass=Interface):
    @abstractfunc
    def area(self) -> float:
        pass


class Rectangle(ShapeInterface):

    def __init__(self, a, b):
        if a <= 0:
            raise ValueError("a must be a positive number")

        if b <= 0:
            raise ValueError("b must be a positive number")

        self._a = a
        self._b = b

    def area(self):
        do_work(2)
        return self._a * self._b


class Triangle(ShapeInterface):

    def __init__(self, base, height):
        if base <= 0:
            raise ValueError("base must be a positive number")

        if height <= 0:
            raise ValueError("height must be a positive number")

        self._base = base
        self._height = height

    def area(self):
        do_work(3)
        return 0.5 * self._base * self._height


def sum_shapes_areas(*shapes) -> float:
    sum_of_areas = 0
    for shape in tqdm(shapes, desc="Calculating areas of all shapes", miniters=1):
        sum_of_areas += shape.area()

    return sum_of_areas


def sum_shapes_areas_multiprocessing(*shapes) -> float:
    sum_of_areas = 0
    with Pool(processes=min(len(shapes), cpu_count())) as pool:
        jobs = [
            pool.apply_async(func=shape.area)
            for shape in shapes
        ]
        for job in tqdm(jobs, desc="Calculating areas of all shapes", miniters=1):
            sum_of_areas += job.get()

    return sum_of_areas


def do_work(seconds):
    t_end = time() + seconds
    while time() < t_end:
        a = time() * time()
    return a


if __name__ == "__main__":
    rec = Rectangle(2, 4)
    tri = Triangle(2, 3)
    shapes_args = [rec, tri, tri, rec, tri, tri]

    start = datetime.datetime.now()
    print("Running sum_shapes_areas...")
    print(f"Sum of all areas is {sum_shapes_areas(*shapes_args)}")
    duration_of_sum_shapes_areas = datetime.datetime.now() - start
    print(f"sum_shapes_areas took {duration_of_sum_shapes_areas.total_seconds() * 1000:.2f} ms")

    start = datetime.datetime.now()
    print("Running sum_shapes_areas_multiprocessing...")
    print(f"Sum of all areas is {sum_shapes_areas_multiprocessing(*shapes_args)}")
    duration_of_sum_shapes_areas = datetime.datetime.now() - start
    print(f"sum_shapes_areas_multiprocessing took {duration_of_sum_shapes_areas.total_seconds() * 1000:.2f} ms")
