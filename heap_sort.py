def main():
    sample = [1, 4, 10, 14, 7, 9, 3, 2, 8, 16]

    # This ensures max heap is built and follows the max heap property
    build_max_heap(sample)

    print(extract_max_element(sample))
    print(heap_sort(sample))

# Build the max heap structure from the list


def build_max_heap(data):
    for i in range(len(data) // 2, -1, -1):
        max_heapify(data, i)

# Read the max element from the heap without removing it


def read_max_element(data):
    if not data:
        raise Exception('Heap is empty')
    return data[0]

# Remove and return the max element from the heap and maintain the max heap property


def extract_max_element(data):
    max_element = read_max_element(data)
    data[0] = data[-1]
    data.pop()
    max_heapify(data, 0)
    return max_element

# Perform heap sort on the list and return a sorted list


def heap_sort(data):
    build_max_heap(data)
    # Creates a list filled with zeros, same length as data
    result = [0] * len(data)

    for i in range(len(data) - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        result[i] = data[i]
        data.pop()
        max_heapify(data, 0)  # Heapify the reduced heap

    result[0] = data[0]  # Last remaining element is the smallest
    return result

# Function to ensure the heap follows the max heap property at a given index


def max_heapify(data, i):
    left_idx = 2 * i + 1
    right_idx = 2 * i + 2
    largest = i

    if left_idx < len(data) and data[left_idx] > data[largest]:
        largest = left_idx

    if right_idx < len(data) and data[right_idx] > data[largest]:
        largest = right_idx

    if largest != i:
        # Swap current node with the largest
        data[i], data[largest] = data[largest], data[i]
        max_heapify(data, largest)


if __name__ == "__main__":
    main()
