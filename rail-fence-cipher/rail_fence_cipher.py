from typing import List, Sequence, Generator

def encode(message: str, num_rails: int) -> str:
    """Use a rail-fence cipher to encipher a given message"""
    rails = ['' for i in range(num_rails)]
    rail_cycle = rail_cycler(num_rails)

    for char in message:
        rails[next(rail_cycle)] += char

    return ''.join(rails)


def decode(encoded_message: str, num_rails: int) -> str:
    """Use a rail-fence cipher to decipher a given message"""

    # calculate split lengths for each rail
    rail_lengths = [0] * num_rails
    rail_cycle = rail_cycler(num_rails)
    for _ in range(len(encoded_message)):
        rail_lengths[next(rail_cycle)] += 1

    # split ciphertext across rails
    rails = [list(string) for string in split_by_sizes(encoded_message, rail_lengths)]

    # reconstruct plaintext from rails
    rail_cycle = rail_cycler(num_rails)
    return ''.join([  rails[next(rail_cycle)].pop(0)
                        for _ in range(len(encoded_message)) ])


def split_by_sizes(to_split: Sequence, sizes: List[int]) -> List[Sequence]:
    """Return a list of Sequences consisting of the given Sequence split into
    consecutive chunks of sizes in the given list of sizes
    e.g. split_by_sizes('abcdef', [2,1,3]) -> ['ab', 'c', 'def'] """
    return [to_split[sum(sizes[:i]):sum(sizes[:i+1])] for i in range(len(sizes))]


def rail_cycler(num_rails: int) -> Generator[int, None, None]:
    """Generator yielding an integer that zigzags from 0 to num_rails and back"""
    cur_rail = 0
    cur_step = 1

    while True:
        yield cur_rail
        cur_rail += cur_step

        # reverse direction if we hit top or bottom rail
        if cur_rail == 0:
            cur_step = 1
        elif cur_rail == num_rails - 1:
            cur_step = -1
