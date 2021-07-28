class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    root = None
    records.sort(key=lambda x: x.record_id)
    ordered_id = [i.record_id for i in records]
    if [r.record_id for r in records] != list(range(len(records))):
        raise ValueError('Record IDs must be continuous starting from 0')

    trees = []
    parent = {}

    for r in records:
        if r.record_id == 0 and r.parent_id != 0:
            raise ValueError('Root node cannot have a parent')
        elif r.record_id != 0 and r.record_id == r.parent_id:
            raise ValueError('Non-root node cannot be its own parent')
        elif r.record_id < r.parent_id:
            raise ValueError('Parent id must be lower than child id')
        trees.append(Node(r.record_id))

    for i in range(len(ordered_id)):
        for j in trees:
            if i == j.node_id:
                parent = j
        for j in records:
            if j.parent_id == i:
                for k in trees:
                    if k.node_id == 0:
                        continue
                    if j.record_id == k.node_id:
                        child = k
                        parent.children.append(child)
    if len(trees) > 0:
        root = trees[0]
    return root
