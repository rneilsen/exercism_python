from collections import deque

NUM_FRAMES = 10
NUM_PINS = 10

class BowlingGame:
    def __init__(self):
        self.total = 0
        self.frame_prev = None
        self.cur_frame = 1
        self.multipliers = deque([1,1])
        self.last_frame_bowls = []
        self.game_over = False

    def roll(self, pins):
        if self.game_over:
            raise Exception("Extra bowls not allowed")

        if not (0 <= pins <= NUM_PINS): 
            raise Exception("Invalid pinfall")

        if self.frame_prev is not None and self.frame_prev + pins > NUM_PINS:
            raise Exception("Invalid frame total")
        
        mult = self.multipliers.popleft()
        self.multipliers.append(1)
        self.total += mult * pins
        
        if self.cur_frame == NUM_FRAMES:    # Last frame
            self.last_frame_bowls.append(pins)
            
            if len(self.last_frame_bowls) == 3:
                self.game_over = True
            elif len(self.last_frame_bowls) == 2:
                if self.last_frame_bowls[0] == NUM_PINS:
                    if pins < NUM_PINS:
                        self.frame_prev = pins
                elif sum(self.last_frame_bowls) == NUM_PINS:
                    self.frame_prev = None
                else:
                    self.game_over = True
            elif len(self.last_frame_bowls) == 1:
                if pins < NUM_PINS:
                    self.frame_prev = pins
            return
        
        if self.frame_prev is not None:
            # this is the second bowl of a frame
            if self.frame_prev + pins == NUM_PINS:
                # spare!
                self.multipliers[0] += 1
            self.frame_prev = None
            self.cur_frame += 1
        elif pins == NUM_PINS:
            # strike!:
            self.multipliers[0] += 1
            self.multipliers[1] += 1
            self.cur_frame += 1
        else:
            self.frame_prev = pins


    def score(self):
        return self.total


# game = BowlingGame()
# testrolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 6]
# for roll in testrolls:
#     if roll == 10:
#         pass
#     game.roll(roll)

# print(game.score())