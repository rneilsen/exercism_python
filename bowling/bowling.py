from collections import deque

NUM_FRAMES = 10
NUM_PINS = 10

class BowlingGame:
    """Tracks the score for a single player's bowling game"""
    def __init__(self):
        self.total = 0                      # running total score
        self.cur_frame = 1                  # number of the current frame
        self.game_over = False              # track whether this game has ended

        self._multipliers = deque([1,1])    # stores multipliers for upcoming rolls
        self._last_frame_bowls = []         # stores pinfalls in the last frame
        self._prev_pinfall_in_frame = None  # stores the previous pinfall in
                                            # the current frame (for spares etc)


    def roll(self, pins):
        """Add a new roll to this game. Rejects invalid rolls, updates score"""
        if self.game_over:
            raise IndexError("Extra bowls not allowed")
        if not 0 <= pins <= NUM_PINS:
            raise ValueError("Invalid pinfall")
        if self._prev_pinfall_in_frame is not None and \
                self._prev_pinfall_in_frame + pins > NUM_PINS:
            raise ValueError("Invalid frame total")

        # Add pins using bonus multiplier from previous strikes & spares
        mult = self._multipliers.popleft()
        self._multipliers.append(1)
        self.total += mult * pins

        # If we're on the last frame, handle it differently
        if self._is_last_frame():
            self._handle_last_frame(pins)
            return

        # Multiplier incrementing for strikes & spares
        if self._prev_pinfall_in_frame is not None:
            # this is the second bowl of a frame
            if self._prev_pinfall_in_frame + pins == NUM_PINS:  # spare!
                self._multipliers[0] += 1
            self._prev_pinfall_in_frame = None
            self.cur_frame += 1
        elif pins == NUM_PINS:  # strike!:
            self._multipliers[0] += 1
            self._multipliers[1] += 1
            self.cur_frame += 1
        else:
            # this is the first bowl of a frame
            self._prev_pinfall_in_frame = pins


    def _is_last_frame(self):
        return self.cur_frame == NUM_FRAMES


    def _handle_last_frame(self, pins):
        self._last_frame_bowls.append(pins)

        if len(self._last_frame_bowls) == 3:
            self.game_over = True
        elif len(self._last_frame_bowls) == 2:
            if self._last_frame_bowls[0] == NUM_PINS:
                if pins < NUM_PINS:
                    # first bowl strike, second bowl not, retain score
                    self._prev_pinfall_in_frame = pins
            elif sum(self._last_frame_bowls) == NUM_PINS:
                # first two bowls formed a spare (1 fill ball)
                self._prev_pinfall_in_frame = None
            else:
                # first two bowls were not a spare, game over
                self.game_over = True
        else:
            if pins < NUM_PINS:
                # first bowl was not a strike, retain score
                self._prev_pinfall_in_frame = pins


    def score(self):
        return self.total
