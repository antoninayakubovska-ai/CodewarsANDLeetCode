def tree_by_levels(node):
    if not node:
        return []

    result = []
    queue = [node]
    while queue:
        curr = queue.pop(0)
        result.append(curr.value)

        if curr.left:
            queue.append(curr.left)

        if curr.right:
            queue.append(curr.right)

    return result
            