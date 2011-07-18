def insertion_sort(elements):
    for j in range(1, len(elements)):
        key = elements[j]

        i = j - 1

        while i > -1 and elements[i] > key:
            elements[i + 1] = elements[i]
            i -= 1
        elements[i + 1 ] = key
    return elements
