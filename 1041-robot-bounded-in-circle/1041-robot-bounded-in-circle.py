class Solution:
    def turn(self,direction, move):
        arr = ['North', 'West', 'South', 'East']
        if move == 'L':
            # val = min(4-arr.index(direction)+1, arr.index(direction)+1)
            return arr[(arr.index(direction)+1)%4]
        else:
            return arr[(arr.index(direction)-1)%4]
    
    def move(self, direction, tup):
        x,y = tup
        if direction=='North':
            return (x, y+1)
        elif direction=='South':
            return (x, y-1)
        elif direction=='West':
            return (x-1, y)
        if direction=='East':
            return (x+1, y)
        
    def isRobotBounded(self, instructions: str) -> bool:
        current_place = (0,0)
        initial_place = (0,0)
        current_direction = 'North'
        possible = True
        # while possible:
        for instruction in instructions:
            if instruction == 'G':
                current_place = self.move(current_direction, current_place)
            else:
                current_direction = self.turn(current_direction, instruction)
        print(current_place, current_direction)
        if current_place == (0,0) or current_direction != 'North':
            return True
        # elif current_direction != 'North':
        #     recursive_helper(instructions, current_place, current_direction,possible)
        else:
            return False
        # return recursive_helper(instructions, current_place, current_direction,False)
        # ans =  self.recursive_helper(instructions, current_place, current_direction,False)
        # print(ans)
            # travel_vector = [current_place[0] - initial_place[0], current_place[1]-inital_place[1]]