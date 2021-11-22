from collections import deque

NUM_FRAMES = 10
NUM_PINS = 10

class BowlingGame:
    """Tracks the score for a single player's bowling game"""
    def __init__(self):
        self.total = 0
        self.prev_pinfall_in_frame = None
        self.cur_frame = 1
        self.multipliers = deque([1,1])
        self.last_frame_bowls = []
        self.game_over = False

    def roll(self, pins):
        """Add a new roll to this game. Rejects invalid rolls, updates score"""
        if self.game_over:
            raise Exception("Extra bowls not allowed")
        if not 0 <= pins <= NUM_PINS:
            raise Exception("Invalid pinfall")
        if self.prev_pinfall_in_frame is not None and \
                self.prev_pinfall_in_frame + pins > NUM_PINS:
            raise Exception("Invalid frame total")

        # Add pins using bonus multiplier from previous strikes & spares
        mult = self.multipliers.popleft()
        self.multipliers.append(1)
        self.total += mult * pins

        # Special handling for the last frame (skips multiplier incrementing)
        if self.cur_frame == NUM_FRAMES:
            self.last_frame_bowls.append(pins)

            if len(self.last_frame_bowls) == 3:
                self.game_over = True
            elif len(self.last_frame_bowls) == 2:
                if self.last_frame_bowls[0] == NUM_PINS:
                    if pins < NUM_PINS:
                        # first bowl strike, second bowl not, retain score
                        self.prev_pinfall_in_frame = pins
                elif sum(self.last_frame_bowls) == NUM_PINS:
                    # first two bowls formed a spare (1 fill ball)
                    self.prev_pinfall_in_frame = None
                else:
                    # first two bowls were not a spare, game over
                    self.game_over = True
            else:
                if pins < NUM_PINS:
                    # first bowl was not a strike, retain score
                    self.prev_pinfall_in_frame = pins
            return

        # Multiplier incrementing for strikes & spares
        if self.prev_pinfall_in_frame is not None:
            # this is the second bowl of a frame
            if self.prev_pinfall_in_frame + pins == NUM_PINS:  # spare!
                self.multipliers[0] += 1
            self.prev_pinfall_in_frame = None
            self.cur_frame += 1
        elif pins == NUM_PINS:  # strike!:
            self.multipliers[0] += 1
            self.multipliers[1] += 1
            self.cur_frame += 1
        else:
            self.prev_pinfall_in_frame = pins


    def score(self):
        return self.total
