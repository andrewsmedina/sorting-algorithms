def bubble_sort(elements):
    for i in range(len(elements)):
        for j in range(i+1, len(elements)):
            if elements[i] > elements[j]:
                temp = elements[i]
                elements[i] = elements[j]
                elements[j] = temp
    return elements
