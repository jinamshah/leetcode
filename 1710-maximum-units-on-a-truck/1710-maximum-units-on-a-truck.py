class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        total_count = 0
        remainingTruckCapacity = truckSize
        for box in boxTypes:
            if truckSize > 0:
                boxCount = min(truckSize, box[0])
                total_count += (boxCount * box[1])
                truckSize -= boxCount
            else:
                break
        return total_count