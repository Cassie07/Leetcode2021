class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        sum_unit = 0
        boxTypes = sorted(boxTypes, key=lambda x: x[1])

        for num_box, num_unit in reversed(boxTypes):

            if truckSize >= num_box:
                sum_unit += num_box * num_unit
                truckSize -= num_box
            else:
                sum_unit += truckSize * num_unit

                return sum_unit
     
        return sum_unit
