PITCHES_SH = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
PITCHES_FL = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

FLAT_SCALES = {'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb', 'eb'}

INTERVALS = {'m': 1, 'M': 2, 'A': 3}


class Scale:
    def __init__(self, tonic):
        if tonic in FLAT_SCALES:
            start = PITCHES_FL.index(tonic[0].upper() + tonic[1:])
            self.scale = PITCHES_FL[start:] + PITCHES_FL[:start]
        else:
            start = PITCHES_SH.index(tonic[0].upper() + tonic[1:])
            self.scale = PITCHES_SH[start:] + PITCHES_SH[:start]

    def chromatic(self):
        return self.scale

    def interval(self, intervals):
        i = 0
        scale = []
        for step in intervals:
            # note: last step in intervals is *supposed* to be skipped,
            # obviously for no apparent reason (classic music theory, amirite)
            scale.append(self.scale[i % len(self.scale)])
            i += INTERVALS[step]
        
        return scale
