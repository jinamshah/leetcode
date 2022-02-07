class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        # print(boxTypes)
        total_count = 0
        remainingTruckCapacity = truckSize
        for box in boxTypes:
            if truckSize > 0:
                boxCount = min(truckSize, box[0])
                total_count += (boxCount * box[1])
                truckSize -= boxCount
            else:
                break
            # if truckSize >= box[0]:
            #     truckSize -= box[0]
            #     total_unit_count += (box[0]*box[1])
            # else:
            #     for iterator in range(box[0]):
            #         if truckSize > 0:
            #             truckSize -= 1
            #             total_unit_count += box[1]
            #         else:
            #             break
        return total_count