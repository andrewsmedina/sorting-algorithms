def merge_sort(elements):
    if len(elements) <= 1:
        return elements

    middle = len(elements) / 2

    left = elements[:middle]
    right = elements[middle:]

    result = merge(merge_sort(left), merge_sort(right))
    return result


def merge(left, right):
    result = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))

    return result

