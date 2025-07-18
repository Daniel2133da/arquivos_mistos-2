#Code for Algorithm 2
from  functools import cmp_to_key
    
# Represents line_segment which is either horizontal or vertical.
class line_segment:
    __start_point = (0, 0)
    __end_point = (0, 0)
    
    def __init__(self, start_point, end_point):
        if start_point[0] == end_point[0]:
            self.__start_point = (start_point, end_point)[start_point[1] > end_point[1]]
            self.__end_point = (start_point, end_point)[start_point[1] < end_point[1]]
        else:
            self.__start_point = (start_point, end_point)[start_point[0] > end_point[0]]
            self.__end_point = (start_point, end_point)[start_point[0] < end_point[0]]
    
    def does_intersect(self, target_line_segment):        
        is_vertical = self.is_segment_vertical()
        is_traget_vertical = target_line_segment.is_segment_vertical()
        
        # Check for parallel segments
        if is_vertical and is_traget_vertical:
            return False
       
        if is_vertical:
            return self.__start_point[0] >= target_line_segment.__start_point[0] and \
                    self.__start_point[0] <= target_line_segment.__end_point[0] and \
                    target_line_segment.__start_point[1] >= self.__start_point[1] and \
                    target_line_segment.__start_point[1] <= self.__end_point[1]            
        else:
            return target_line_segment.__start_point[0] >= self.__start_point[0] and \
                    target_line_segment.__start_point[0] <= self.__end_point[0] and \
                    self.__start_point[1] >= target_line_segment.__start_point[1] and \
                    self.__start_point[1] <= target_line_segment.__end_point[1]            
        
    
    def is_segment_vertical(self):
        return self.__start_point[0] ==  self.__end_point[0]
    
    def get_value(self):
        if self.is_segment_vertical():
            return self.__start_point[0]
        else:
            return self.__start_point[1]       
   
    def get_non_constant_start_coordinate(self):
        if self.is_segment_vertical():
            return self.__start_point[1]
        else:
            return self.__start_point[0]
        
    def get_non_constant_end_coordinate(self):
        if self.is_segment_vertical():
            return self.__end_point[1]
        else:
            return self.__end_point[0]

        
# Line segment comparator
def compare(item_1, item_2):
    return item_1[0].get_value() - item_2[0].get_value()

def binary_serach_comparator(segment, search_value):
    return segment[0].get_value() - search_value

def binary_serach(sorted_collection, serach_value, comparator):
    high = len(sorted_collection) - 1
    low = 0
    index = -1
    mid = 0
    while(low <= high):
        mid = int((low + high)/2)
        comparator_value = comparator(sorted_collection[mid], serach_value)
        if comparator_value < 0:
            low = mid + 1
        elif comparator_value > 0:
            high = mid - 1
        else:
            index = mid 
            break
    
    return (index, low, high)

def split_path_in_segments(path_points):
    vertical_segment_start_index = (0, 1) [path_points[0][0] == path_points[1][0]]
    
    vertical_segments  = [(line_segment(path_points[index], path_points[index + 1]), index)\
                          for index in range(vertical_segment_start_index, len(path_points) - 1, 2)]
    
    horizontal_segments  = [(line_segment(path_points[index], path_points[index + 1]), index)\
                            for index in range(int(not(vertical_segment_start_index)), len(path_points) - 1, 2)]
    return vertical_segments, horizontal_segments

def find_segments_in_range(segments, range_start, range_end):
    (start_index, start_low, start_high) = binary_serach(segments, range_start, binary_serach_comparator)
    (end_index, end_low, end_high) = binary_serach(segments, range_end, binary_serach_comparator)    
    return (start_low, end_high)


# Input: Ordered set of points representing rectilinear paths
# which is made up of alternating horizontal and vertical segments
def check_loop(path_points):
    
    # For loop we need 4 or more segments. Hence more than 5 points
    if len(path_points) <= 4: 
        return False    
    
    vertical_segments, horizontal_segments = split_path_in_segments(path_points)    
    
    # Sort vertical segmnets for easy serach
    vertical_segments = sorted(vertical_segments,  key=cmp_to_key(compare))
    
    # Iterate through horizontal segments, find vertical segments
    # which fall in rane of horizontal segment and check for intersection
    for horizontal_counter in range(len(horizontal_segments)):
        horizontal_segment = horizontal_segments[horizontal_counter][0]
        horizontal_segment_index = horizontal_segments[horizontal_counter][1]        
        
        (start, end) =  find_segments_in_range(vertical_segments,\
                                               horizontal_segment.get_non_constant_start_coordinate(),\
                                              horizontal_segment.get_non_constant_end_coordinate())
        
        for vertical_counter in range(start, end + 1):
            vertical_segment = vertical_segments[vertical_counter][0]
            vertical_segment_index = vertical_segments[vertical_counter][1]
            
            # Avoid adjacent segments. They will always have one endpoint in common
            if abs(horizontal_segment_index - vertical_segment_index) <= 1:
                continue
                
            if horizontal_segment.does_intersect(vertical_segment):
                return True
    
    return False
        

print(check_loop([(0,0), (5,0), (5, 5)])) # False
print(check_loop([(0,0), (5,0), (5, 5), (0, 5), (0, 0)])) # True
print(check_loop([(0,0), (5,0), (5, 5), (4, 5)])) # False
print(check_loop([(0,0), (5,0), (5, 5), (4, 5), (4, 2)])) # False
print(check_loop([(0,0), (5,0), (5, 5), (4, 5), (4, -1)])) # True
print(check_loop([(0,0), (5,0), (5, 5), (4, 5), (4, 0)])) # True
print(check_loop([(0,0), (5,0), (5, 5), (8, 5), (8, 2), (10, 2)]))# False
print(check_loop([(0,0), (5,0), (5, 5), (8, 5), (8, 2), (10, 2), (11, 2), (11, 1), (-5, 1), (-5, 15)]))# False
print(check_loop([(0,0), (5,0), (5, 5), (8, 5), (8, 2), (10, 2), (10, -1), (2, -1), (2, 15)]))# True