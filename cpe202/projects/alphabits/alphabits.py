# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   AlphaBits
# Term:         Winter 2021

from typing import Optional, List, Tuple


class HuffmanNode:

    def __init__(self, char: str, count: int, l_ref: Optional["HuffmanNode"],
                 r_ref: Optional["HuffmanNode"]) -> None:
        self.char = char
        self.count = count
        self.l_ref = l_ref
        self.r_ref = r_ref

    def __eq__(self, other: Optional["HuffmanNode"]) -> bool:
        if other is None:
            return False
        return (self.char == other.char and self.count == other.count
                and self.l_ref == other.l_ref and self.r_ref == other.r_ref)

    def __repr__(self) -> str:
        s = f"{self.char}:{self.count}"
        if self.l_ref is not None:
            s += " " + str(self.l_ref)
        if self.r_ref is not None:
            s += " " + str(self.r_ref)
        return s


def frequency(chars: str) -> List[HuffmanNode]:
    if len(chars) == 0:
        return None
    heap_list = []
    frequency = [0] * 256
    for c in chars:
        frequency[ord(c)] += 1

    for x in range(0, len(frequency)):
        if frequency[x] != 0:
            heap_list.append(HuffmanNode(chr(x), frequency[x], None, None))
    return heap_list


def create_tree(chars: str) -> Optional[HuffmanNode]:
    """
    Build a Huffman tree by analyzing the frequency of each character in the
    given string and return the root node of the tree.
    """
    if chars == "":
        return None
    heap_list = frequency(chars)
    while len(heap_list) > 1:
        heap_list, low, lowest = remove_two(heap_list)
        parent = HuffmanNode(" ", lowest.count + low.count, None, None)
        if low.count > lowest.count:
            parent.l_ref = lowest
            parent.r_ref = low
        elif low.count < lowest.count:
            parent.r_ref = lowest
            parent.l_ref = low
        else:
            if ord(low.char) < ord(lowest.char):
                parent.l_ref = low
                parent.r_ref = lowest
            else:
                parent.l_ref = lowest
                parent.r_ref = low
        if ord(low.char) < ord(lowest.char):
            parent.char = low.char
        else:
            parent.char = lowest.char
        heap_list.append(parent)
    return heap_list[0]

'''
def remove_two(heap_list: List[HuffmanNode]) -> Tuple[List[HuffmanNode], \
                                                HuffmanNode, HuffmanNode]:
    low = HuffmanNode("■", 1000, None, None)
    lowest = HuffmanNode("■", 1000, None, None)
    for x in heap_list:
        if x.count < low.count:
            low = x
        elif x.count < lowest.count:
            lowest = x
        elif x.count == lowest.count or x.count == low.count:
            if ord(x.char) < ord(low.char):
                low = x
            elif ord(x.char) < ord(lowest.char):
                lowest = x
    heap_copy = []
    for x in heap_list:
        if x.char != low.char and x.char != lowest.char:
            heap_copy.append(x)
    root = heap_copy
    return root, low, lowest
'''

def remove_two1(char, char2, heap_list) -> List[HuffmanNode]:
    heap_copy = []
    for x in heap_list:
        if x.char != char and x.char != char2:
            heap_copy.append(x)


def encode(chars: str, root: Optional[HuffmanNode]) -> str:
    """
    Return the Huffman code (bit string) of the given characters, using the
    provided Huffman tree.To encode a string, for each of its characters
     search the Huffman tree for the leaf node containing that character.
      While searching, keep track of which branch (the left or right) was
      traversed at each node to get to the leaf with the target character.
      Whenever a left node is taken, "0" is added to the code; similarly,
      whenever a right node is taken, "1" is added to the code. In the tree
       above, the character "B" has the code "1010" because the tree was
       traversed (from the root) in the order right-left-right-left to get

       to the leaf node with the character "B". In constructing these codes,
        it is easiest to use recursion with an accumulator that builds up
        the code as the recursive calls are made, then returns the completed
         code in the base case.

Decoding is more straightforward than encoding. Given a code "10100",
traverse left for each "0" and right for each "1". When a leaf is reached,
 add that leaf's character to the decoded string and continue with the next
  character in the code from the root of the tree. This example produces
  the string "BE".
    """

    bit_string = ""
    for x in chars:
        bit_string = bit_string + encode_helper(x, root)
    return bit_string


def encode_helper(x: str, root: Optional[HuffmanNode]) -> str:
    if root.r_ref is None and root.l_ref is None:
        if root.char == x:
            return ''
    if root.l_ref is not None:
        ans = encode_helper(x, root.l_ref)
        if ans is not None:
            return "0" + ans
    if root.r_ref is not None:
        ans = encode_helper(x, root.r_ref)
        if ans is not None:
            return "1" + ans
    return None


def decode(bits: str, root: Optional[HuffmanNode]) -> str:
    """
    Given a code "10100", traverse left for each "0" and right for each "1".
    When a leaf is reached, add that leaf's character to the
    decoded string and continue with the next character in the
    code from the root of the tree. This example produces
    the string "BE".
    """
    string = ""
    head = root
    for x in bits:
        if x == "1":
            head = head.r_ref
            if head.r_ref is None and head.l_ref is None:
                string = string + head.char
                head = root

        if x == "0":
            head = head.l_ref
            if head.l_ref is None and head.r_ref is None:
                string = string + head.char
                head = root

    return string


# do not modify code below this line
def main() -> None:
    chars = input("Treeify: ")  # initial chars used to create Huffman tree
    root = create_tree(chars)
    while True:
        try:
            chars = input(">>> ")  # chars to encode
            code = encode(chars, root)
            assert decode(code, root) == chars
            print(code)
        except AssertionError:
            print("Encode/Decode Failure")
        except EOFError:  # loop breaks with CTRL+d
            break
    print()


if __name__ == "__main__":
    main()
