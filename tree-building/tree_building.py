class Record:
    def __init__(self, id, parent_id):
        self.node_id, self.id, self.parent_id, self.children = id, id, parent_id, []


def BuildTree(recs):
    recs.sort(key=lambda x: x.id)
    if recs and (recs[-1].id != len(recs) - 1):
        raise ValueError("Record id is invalid or out of order.")
    if any(j.id < j.parent_id for j in recs):
        raise ValueError("Node parent_id should be smaller than it's record_id.")
    if any((j.id == j.parent_id) for j in recs[1:]):
        raise ValueError("Only root should have equal record and parent id.")
    for parent in recs:
        parent.children = [child for child in recs[1:] if parent.id == child.parent_id]
    return recs[0] if recs else None  # Root
