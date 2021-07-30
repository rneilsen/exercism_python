class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if len(records) == 0:
        return None
    
    records.sort(key=lambda x: x.record_id)
    if [r.record_id for r in records] != list(range(len(records))):
        raise ValueError('Record IDs must be continuous starting from 0')
    
    nodes = []
    for r in records:
        if r.record_id == 0 and r.parent_id != 0:
            raise ValueError('Root node cannot have a parent')
        elif r.record_id != 0 and r.record_id == r.parent_id:
            raise ValueError('Non-root node cannot be its own parent')
        elif r.record_id < r.parent_id:
            raise ValueError('Parent id must be lower than child id')
        nodes.append(Node(r.record_id))

    # build tree (works because records and nodes are sorted and continuous)
    for i in range(1, len(nodes)):
        parent = records[i].parent_id
        nodes[parent].children.append(nodes[i])
    
    return nodes[0]
