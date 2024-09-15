def main():
    sample = [1, 4, 10, 14, 7, 9, 3, 2, 8, 16]
    # max_heapify(sample, 0)
    # build_max_heap(sample)
    # print(sample)
    print(heap_sort(sample))


def build_max_heap(d):
    for i in range(len(d) // 2, -1, -1):
        max_heapify(d, i)


def heap_sort(data):
    build_max_heap(data)
    result = [0] * len(data)
    for i in range(len(data) - 1, 0, -1):
        temp = data[i]
        data[i] = data[0]
        data[0] = temp
        result[i] = data[i]
        data.pop()  # remove last element
        max_heapify(data, 0)
    return result


def max_heapify(data, i):
    left_index = 2 * i + 1
    right_i = 2 * i + 2
    largest = i
    if left_index < len(data) and data[left_index] > data[largest]:
        largest = left_index
    if right_i < len(data) and data[right_i] > data[largest]:
        largest = right_i
    if largest != i:
        temp = data[largest]
        data[largest] = data[i]
        data[i] = temp
        max_heapify(data, largest)


if __name__ == "__main__":
    main()
