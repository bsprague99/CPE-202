# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Tile Driver
# Term:         Winter 2021

import random
from typing import List, Tuple, Optional


class PuzzleState:  # do not modify

    def __init__(self, tiles: Tuple[int, ...], path: str) -> None:
        self.tiles = tiles
        self.width = int(len(tiles) ** 0.5)
        self.path = path

    def __eq__(self, other: "PuzzleState") -> bool:
        return self.tiles == other.tiles and self.path == other.path

    def __repr__(self) -> str:
        return self.path


def state_generator(spot: int, target: int, path: str, \
                    tiles: Tuple[int, ...]) -> Optional[PuzzleState]:
    if "HL" in path or "LH" in path or "KJ" in path or "JK" in path:
        return None
    else:

        new_state = list(tiles)
        new_state[spot], new_state[target] = new_state[target], new_state[spot]
        new_board = PuzzleState(tuple(new_state), path)
        return new_board


def make_adjacent(state: PuzzleState) -> List[PuzzleState]:
    """
    Return a list of PuzzleState objects that represent valid, non-opposing
    moves from the given PuzzleState. A move is considered valid if it moves a
    tile adjacent to the blank tile into the blank tile. A move is considered
    non-opposing if it does not undo the previous move.

    >>> state = PuzzleState((3, 2, 1, 0), "")
    >>> make_adjacent(state)
    [PuzzleState((3, 0, 1, 2), "J"), PuzzleState((3, 2, 0, 1), "L")]
    """
    possible_solutions = []
    spot = state.tiles.index(0)
    if state.width == 3:
        if spot % state.width != 0:  # [-1:L]
            possible_solutions.append(state_generator
                            (spot, spot - 1, state.path + "L", state.tiles))
        if spot < 6:  # [+3:K]
            possible_solutions.append(state_generator
                            (spot, spot + 3, state.path + "K", state.tiles))

        if spot > 2:  # [-3:J]
            possible_solutions.append(state_generator
                        (spot, spot - 3, state.path + "J", state.tiles))

        if spot % state.width != 2:  # [+1:H]
            possible_solutions.append(state_generator
                            (spot, spot + 1, state.path + "H", state.tiles))
    if state.width == 2:
        if spot % 2 == 0:
            possible_solutions.append(state_generator(spot,
                                spot + 1, state.path + "H", state.tiles))

        if spot % 2 != 0:
            possible_solutions.append(state_generator(spot, spot - 1,
                                        state.path + "L", state.tiles))

        if spot < 2:
            possible_solutions.append(state_generator(spot, spot
                                    + 2, state.path + "K", state.tiles))

        if spot > 1:
            possible_solutions.append(state_generator(spot, spot - 2, \
                                    state.path + "J", state.tiles))

    possible_solutions = [x for x in possible_solutions if x is not None]

    return possible_solutions


def is_solvable(tiles: Tuple[int, ...]) -> bool:
    """
    Return a Boolean indicating whether the given tuple represents a solvable
    puzzle. Use the Merge Sort algorithm (possibly in a helper function) to
    efficiently count the number of inversions.

    >>> is_solvable((3, 2, 1, 0))
    True
    >>> is_solvable((0, 2, 1, 3))
    False
    """
    inv_count = 0
    n = len(tiles)
    for i in range(n):
        for j in range(i + 1, n):
            if tiles[i] > tiles[j] != 0:
                inv_count += 1

    blank = tiles.index(0)

    width = int(len(tiles)) ** 0.5
    rows = blank // width

    if width % 2 == 0:  # Even
        if rows % 2 == 0:  # even
            return bool(inv_count % 2 == 0)

        else:
            return bool(inv_count % 2 == 1)
    else:
        return bool(inv_count % 2 == 0)


def remove_unsolvable(frontier: List[PuzzleState]) -> List:
    copy = []

    for i in frontier:
        if is_solvable(i.tiles):
            copy.append(i)

    return copy


def solve_puzzle(tiles: Tuple[int, ...]) -> str:
    """
    Return a string (containing characters "H", "J", "K", "L") representing the
    optimal number of moves to solve the given puzzle using Uniform Cost Search.
    A state is considered a solution if its tiles are sorted.

    >>> solve_puzzle((3, 2, 1, 0))
    "JLKHJL"
    """
    answer = tuple(sorted(tiles))
    start = PuzzleState(tiles, "")
    frontier = make_adjacent(start)
    frontier2 = frontier
    while frontier is not None:
        frontier = frontier2
        frontier2 = remove_unsolvable(frontier)
        shortest = get_shortest(frontier2)
        if answer == shortest.tiles:
            return shortest.path
        else:
            frontier2.extend(make_adjacent(shortest))
            frontier2.remove(shortest)
    return "not solvable"


def get_shortest(frontier: List[PuzzleState]) -> PuzzleState:
    shortest = frontier[0]

    for i in frontier:
        if len(i.path) < len(shortest.path):
            shortest = i

    return shortest


def main() -> None:
    random.seed(int(input("Random Seed: ")))
    tiles = list(range(int(input("Puzzle Width: ")) ** 2))  # use 2 or 3
    random.shuffle(tiles)
    print("Tiles:", "[", " ".join(str(t) for t in tiles), "]")
    if not is_solvable(tuple(tiles)):
        print("Unsolvable")
    else:
        print("Solution:", solve_puzzle(tuple(tiles)))


if __name__ == "__main__":
    main()
