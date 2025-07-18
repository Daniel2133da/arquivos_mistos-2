from functools import cmp_to_key
from typing import Tuple, Sequence, List, NamedTuple, Callable


class Point(NamedTuple):
    x: int
    y: int


class LineSegment:
    """
    Represents line_segment which is either horizontal or vertical.
    """

    def __init__(self, start_point: Point, end_point: Point) -> None:
        if start_point.x == end_point.x:
            self._start_point = (start_point, end_point)[start_point.y > end_point.y]
            self._end_point = (start_point, end_point)[start_point.y < end_point.y]
        else:
            self._start_point = (start_point, end_point)[start_point.x > end_point.x]
            self._end_point = (start_point, end_point)[start_point.x < end_point.x]

    def does_intersect(self, target_line_segment: 'LineSegment') -> bool:
        is_vertical = self.is_segment_vertical
        is_target_vertical = target_line_segment.is_segment_vertical

        # Check for parallel segments
        if is_vertical and is_target_vertical:
            return False

        if is_vertical:
            return (
                target_line_segment._start_point.x <= self._start_point.x <= target_line_segment._end_point.x and
                self._start_point.y <= target_line_segment._start_point.y <= self._end_point.y
            )
        else:
            return (
                target_line_segment._start_point.y <= self._start_point.y <= target_line_segment._end_point.y and
                self._start_point.x <= target_line_segment._start_point.x <= self._end_point.x
            )

    @property
    def is_segment_vertical(self) -> bool:
        return self._start_point.x == self._end_point.x

    @property
    def value(self) -> int:
        if self.is_segment_vertical:
            return self._start_point.x
        else:
            return self._start_point.y

    @property
    def non_constant_start_coordinate(self) -> int:
        if self.is_segment_vertical:
            return self._start_point.y
        else:
            return self._start_point.x

    @property
    def non_constant_end_coordinate(self) -> int:
        if self.is_segment_vertical:
            return self._end_point.y
        else:
            return self._end_point.x


class IndexedSegment(NamedTuple):
    segment: LineSegment
    index: int


# Line segment comparator
def compare(item_1: IndexedSegment, item_2: IndexedSegment) -> int:
    return item_1.segment.value - item_2.segment.value


def binary_search_comparator(segment: IndexedSegment, search_value: int) -> int:
    return segment.segment.value - search_value


def binary_search(
    sorted_collection: Sequence[IndexedSegment],
    search_value: int,
    comparator: Callable[[IndexedSegment, int], int],
) -> Tuple[
    int,  # index
    int,  # low
    int,  # high
]:
    high = len(sorted_collection) - 1
    low = 0
    index = -1
    
    while low <= high:
        mid = (low + high)//2
        comparator_value = comparator(sorted_collection[mid], search_value)
        if comparator_value < 0:
            low = mid + 1
        elif comparator_value > 0:
            high = mid - 1
        else:
            index = mid
            break

    return index, low, high


def split_path_in_segments(path_points: Sequence[Point]) -> Tuple[
    List[IndexedSegment],  # vert segments
    List[IndexedSegment],  # horz segments
]:
    vertical_segment_start_index = (0, 1) [path_points[0].x == path_points[1].x]

    vertical_segments = [
        IndexedSegment(LineSegment(path_points[index], path_points[index + 1]), index)
        for index in range(vertical_segment_start_index, len(path_points) - 1, 2)
    ]

    horizontal_segments = [
        IndexedSegment(LineSegment(path_points[index], path_points[index + 1]), index)
        for index in range(int(not vertical_segment_start_index), len(path_points) - 1, 2)
    ]

    return vertical_segments, horizontal_segments


def find_segments_in_range(
    segments: Sequence[IndexedSegment],
    range_start: int,
    range_end: int,
) -> Tuple[
    int,  # start low
    int,  # end high
]:
    start_index, start_low, start_high = binary_search(segments, range_start, binary_search_comparator)
    end_index, end_low, end_high = binary_search(segments, range_end, binary_search_comparator)
    return start_low, end_high


# Input: Ordered set of points representing rectilinear paths
# which is made up of alternating horizontal and vertical segments
def check_loop(path_points: Sequence[Tuple[int, int]]) -> bool:

    # For loop we need 4 or more segments. Hence more than 5 points
    if len(path_points) <= 4:
        return False

    points = [Point(*point) for point in path_points]

    vertical_segments, horizontal_segments = split_path_in_segments(points)

    # Sort vertical segments for easy search
    vertical_segments = sorted(vertical_segments,  key=cmp_to_key(compare))

    # Iterate through horizontal segments, find vertical segments
    # which fall in range of horizontal segment and check for intersection
    for horizontal_counter in range(len(horizontal_segments)):
        horizontal_segment = horizontal_segments[horizontal_counter][0]
        horizontal_segment_index = horizontal_segments[horizontal_counter][1]

        start, end = find_segments_in_range(
            vertical_segments,
            horizontal_segment.non_constant_start_coordinate,
            horizontal_segment.non_constant_end_coordinate,
        )

        for vertical_counter in range(start, end + 1):
            vertical_segment = vertical_segments[vertical_counter][0]
            vertical_segment_index = vertical_segments[vertical_counter][1]

            # Avoid adjacent segments. They will always have one endpoint in common
            if abs(horizontal_segment_index - vertical_segment_index) <= 1:
                continue

            if horizontal_segment.does_intersect(vertical_segment):
                return True

    return False





if __name__ == '__main__':
    print(check_loop([(0,0), (5,0), (5, 5)]))
    print(check_loop([(0,0), (5,0), (5, 5), (4, 5)]))
    print(check_loop([(0,0), (5,0), (5, 5), (4, 5), (4, 2)]))
    print(check_loop([(0,0), (5,0), (5, 5), (8, 5), (8, 2), (10, 2)]))
    print(check_loop([(0,0), (5,0), (5, 5), (8, 5), (8, 2), (10, 2),
                            (11, 2), (11, 1), (-5, 1), (-5, 15)]))
    print(check_loop([(0,0), (5,0), (5, 5), (0, 5), (0, 0)]))
    print(check_loop([(0,0), (5,0), (5, 5), (4, 5), (4, -1)]))
    print(check_loop([(0,0), (5,0), (5, 5), (4, 5), (4, 0)]))
    print(check_loop([(0,0), (5,0), (5, 5), (8, 5), (8, 2), (10, 2), (10, -1), (2, -1), (2, 15)]))