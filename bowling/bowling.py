from collections import deque

NUM_FRAMES = 10
NUM_PINS = 10

class BowlingGame:
    """Tracks the score for a single player's bowling game"""
    def __init__(self):
        self.total = 0                      # running total score
        self.prev_pinfall_in_frame = None   # stores the previous pinfall in
                                            # the current frame (for spares etc)
        self.cur_frame = 1                  # number of the current frame
        self.multipliers = deque([1,1])     # store multipliers for upcoming rolls
        self.last_frame_bowls = []          # stores pinfalls in the last frame
        self.game_over = False

    def roll(self, pins):
        """Add a new roll to this game. Rejects invalid rolls, updates score"""
        if self.game_over:
            raise IndexError("Extra bowls not allowed")
        if not 0 <= pins <= NUM_PINS:
            raise ValueError("Invalid pinfall")
        if self.prev_pinfall_in_frame is not None and \
                self.prev_pinfall_in_frame + pins > NUM_PINS:
            raise ValueError("Invalid frame total")

        # Add pins using bonus multiplier from previous strikes & spares
        mult = self.multipliers.popleft()
        self.multipliers.append(1)
        self.total += mult * pins

        # If we're on the last frame, handle it differently
        if self.cur_frame == NUM_FRAMES:
            self._handle_last_frame(pins)
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

    def _handle_last_frame(self, pins):
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

    def score(self):
        return self.total
