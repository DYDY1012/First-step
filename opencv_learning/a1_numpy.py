import numpy


def show(m: str, o: numpy.ndarray):
    print("--" * 10)
    print(m, f"shape: {o.shape}, dtype: {o.dtype}")
    print("--" * 10)
    print(o)
    print("--" * 10)


def main():
    array1 = numpy.array([1, 2, 3], dtype=numpy.int8)
    show("array1", array1)
    # print(array1)
    # print(array1.ndim)
    # print(array1.shape)
    # print(array1.dtype)


if __name__ == "__main__":
    main()
