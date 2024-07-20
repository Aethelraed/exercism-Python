"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[-1]


def convert_coordinate(coord):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return (str(coord)[0], str(coord[-1]))


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    return convert_coordinate(azara_record[-1]) == rui_record[1]


def create_record(a_rec, r_rec):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    if not compare_records(a_rec, r_rec):
        return "not a match"
    return (a_rec[0], a_rec[-1], r_rec[0], r_rec[1], r_rec[-1])


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    h_string = ""
    for rec in combined_record_group:
        h_string = (
            h_string
            + "("
            + ", ".join(
                ["'" + rec[0] + "'"]
                + ["'" + rec[2] + "'"]
                + [str(rec[3])]
                + ["'" + rec[4] + "'"]
            )
            + ")\n"
        )
    return h_string
