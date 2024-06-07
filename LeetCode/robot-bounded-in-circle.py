class Solution:
    dct = {'E': {'L': 'N', 'R': 'S'},
           'W': {'L': 'S', 'R': 'N'},
           'N': {'L': 'W', 'R': 'E'},
           'S': {'L': 'E', 'R': 'W'}}

    def movement(self, instructions, d, x, y):
        for i in range(len(instructions)):
            if instructions[i] in ['L', 'R']:
                d = self.dct[d][instructions[i]]
            elif instructions[i] == 'G':
                if d == 'E':
                    x += 1
                if d == 'W':
                    x -= 1
                if d == 'N':
                    y += 1
                if d == 'S':
                    y -= 1
        return d, x, y

    def isRobotBounded(self, instructions: str) -> bool:

        d = 'N'
        x, y = 0, 0

        d, x, y = self.movement(instructions, d, x, y)

        if d != 'N' or (x, y) == (0, 0):
            # while (x, y) != (0, 0):
            #     d, x, y = self.movement(instructions, d, x, y)
            return True
        else:
            return False


f = Solution()
print(f.isRobotBounded('GGLLGG'))  # true
print(f.isRobotBounded('GG'))  # false
print(f.isRobotBounded('GL'))  # true
print(f.isRobotBounded('GLGLGGLGL'))  # false
