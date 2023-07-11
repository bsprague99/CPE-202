# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set VI
# Term:         Winter 2021

from typing import List, Optional


class Entry:

    def __init__(self, key: Optional[int], val: Optional[str],
                 ref: Optional["Entry"]) -> None:
        self.key: Optional[int] = key
        self.val: Optional[str] = val
        self.ref = ref

    def __eq__(self, other: Optional["Entry"]) -> bool:
        if other is None:
            return False
        return (self.key == other.key and self.val == other.val
                and self.ref == other.ref)

    def __repr__(self) -> str:
        s = f"{self.key}:{self.val}"
        return s if self.ref is None else s + " " + str(self.ref)

    def __len__(self) -> int:
        """
        Return the number of entries chained together.

        >>> len(Entry(1, "A", Entry(2, "B", Entry(3, "C", None))))
        3
        """
        return 1 if self.ref is None else 1 + len(self.ref)

    def nullify(self) -> None:
        """
        Set the key and value of this object to None. A nullified object serves
        as a placeholder for a removed entry in a hash table.

        >>> e = Entry(1, "A", None)
        >>> e.nullify()
        >>> assert e.key == None
        >>> assert e.val == None
        """
        self.key = None
        self.val = None


def hash_key(key: int, size: int) -> int:
    """
    Return an integer for the given key to be used as an index to a table of
    the given size.

    >>> hash_key(10, 7)
    3
    """
    return key % size


def get_load_factor(table: List[Optional[Entry]]) -> float:
    """
    Return the load factor of the given table. Entries of None should count
    as empty slots when computing the load factor.

    >>> table = [None, Entry(1, "A", Entry(5, "B", None)), None, None]
    >>> get_load_factor(table)
    0.5

    >>> table = [Entry(0, "A", None), Entry(5, "B", None), None, None, None]
    >>> get_load_factor(table)
    0.4
    """
    count = 0
    for i in table:
        if i is not None:
            count += 1
            if i.ref is not None:
                while i.ref is not None:
                    i = i.ref
                    count += 1
    return round(count / len(table), 2)


def resize(table: List[Optional[Entry]], mode: str) -> List[Optional[Entry]]:
    """
    Resize and return the given table to twice its length plus one and rehash
    all integer keys from the original table into the resized table using the
    given collision resolution mode, which will be either "chain" or "probe".
    Rehash lower-indexed keys first; for separate chaining only, rehash keys at
    the head of the chain first.

    >>> table = [Entry(0, "A", Entry(3, "B", Entry(6, "C", None))),
    Entry(7, "D", Entry(1, "E", None)), None]
    >>> resize(table, "chain")
    [Entry(7, "D", Entry(0, "A", None)), Entry(1, "E", None), None,
     Entry(3, "B", None), None, None, Entry(6, "C", None)]

   >>> table = [Entry(0, "A", None), Entry(3, "B", None), Entry(8, "C", None)]
    >>> resize(table, "probe")
  [Entry(0, "A", None), Entry(8, "C", None), None, Entry(3, "B", None), None,\
     None, None]
    """
    if table is None:
        return None

    new_table: List[Optional[Entry]] = [None] * (len(table) * 2 + 1)
    if mode == "chain":
        for x in table:
            xs = x
            if x is not None:
                if x.ref is not None:
                    while x.ref is not None:
                        x = x.ref
                        ss = None
                        loc = hash_key(x.key, len(new_table))
                        if new_table[loc] is not None:
                            ss = new_table[loc]
                        new_table[loc] = Entry(x.key, x.val, ss)
                ss = None
                x = xs
                loc = hash_key(x.key, len(new_table))
                if new_table[loc] is not None:
                    ss = new_table[loc]
                new_table[loc] = Entry(x.key, x.val, ss)
    elif mode == "probe":
        for x in table:
            if x is not None:
                loc = hash_key(x.key, len(new_table))
                if new_table[loc] is not None:
                    while new_table[loc] is not None:
                        loc += 1
                        if loc == len(table):
                            loc = 0
                new_table[loc] = x
    return new_table


def chain_get(table: List[Optional[Entry]], key: int) -> str:
    """
    Return the value corresponding to the given key in the table, following
    separate chaining collision resolution. If the key does not exist in the
    table, raise a KeyError.

    >>> table = [Entry(3, "B", Entry(0, "A", None)), None, None]
    >>> chain_get(table, 0)
    "A"
    """
    locate = hash_key(key, len(table))
    if table[locate] is None:
        raise KeyError

    loc = table[locate]
    while loc.key != key:
        if loc.ref is None:
            raise KeyError
        loc = loc.ref

    return loc.val


def chain_insert(table: List[Optional[Entry]], key: int,
                 val: str) -> List[Optional[Entry]]:
    """
    Add the given key-value pair (as a Entry object) to the table and return
    this updated table, following separate chaining collision resolution.

    If performing this update results in the load factor reaching 1.5, resize
    the table to be one more than twice the original length and rehash the
    entire table before returning it.

    >>> table = [Entry(3, "C", Entry(0, "A", None)),
    Entry(4, "D", Entry(1, "B", None)), None]
    >>> chain_insert(table, 8, "E")
    [Entry(0, "A", None), Entry(8, "E", Entry(1, "B", None)), None, \
     Entry(3, "C", None), Entry(4, "D", None), None, None]
    """
    entry = Entry(key, val, None)
    idx = hash_key(key, len(table))

    if table[idx] is not None:
        entry.ref = table[idx]
    table[idx] = entry

    if get_load_factor(table) > 1.5:
        table = resize(table, "chain")

    return table


def chain_remove(table: List[Optional[Entry]],
                 key: int) -> List[Optional[Entry]]:
    """
    Remove the Entry object containing the given key and return this updated
    table. If such an entry does not exist, raise a KeyError.

   >>> table = [Entry(6, "C", Entry(3, "B", Entry(0, "A", None))), None, None]
    >>> chain_remove(table, 3)
    [Entry(6, "C", Entry(0, "A", None)), None, None]
    """
    loc = hash_key(key, len(table))
    entry = table[loc]
    if table[loc] is not None:
        if entry.key != key:
            while entry.ref.key != key:
                entry = entry.ref
            entry.ref = entry.ref.ref
            return table
        elif entry.key == key:
            entry = entry.ref
            table[loc] = entry
            return table
    raise KeyError


def probe_get(table: List[Optional[Entry]], key: int) -> str:
    """
    Return the value corresponding to the given key in the table, following
    linear probing collision resolution and terminating early if an empty slot
    (but not a nullified entry) is encountered. If the key does not exist in
    the table, raise a KeyError.

    >>> table = [Entry(0, "A", None), Entry(3, "B", None), None]
    >>> probe_get(table, 3)
    "B"
    """
    for i in table:
        if i is not None:
            if i.key == key:
                return i.val

        if i is None:
            break

    raise KeyError


def probe_insert(table: List[Optional[Entry]], key: int,
                 val: str) -> List[Optional[Entry]]:
    """
    Add the given key-value pair (as a Entry object) to the table and return
    this updated table, following linear probing collision resolution by
    replacing either an empty slot or a nullified entry with the new entry.

    If performing this update results in the load factor reaching 0.75, resize
    the table to be one more than twice the original length and rehash the
    entire table before returning it.

    >>> table = [Entry(0, "A", None), Entry(1, "B", None), None]
    >>> probe_insert(table, 2, "C")
    [Entry(0, "A", None), Entry(1, "B", None), Entry(2, "C", None), None, \
     None, None, None]
    """
    location = hash_key(key, len(table))
    entry = Entry(key, val, None)
    if table[location] is not None:
        while table[location] is not None:
            if table[location].key is None:
                break

            location += 1
            if location == len(table):
                location = 0
    table[location] = entry
    if get_load_factor(table) > .75:
        table = resize(table, "probe")

    return table


def probe_remove(table: List[Optional[Entry]],
                 key: int) -> List[Optional[Entry]]:
    """
    Call the nullify method on the Entry object containing the given key and
    return this updated table. If such an entry does not exist, raise a
    KeyError.

    >>> table = [Entry(0, "A", None), Entry(1, "B", None), None]
    >>> probe_remove(table, 0)
    [Entry(None, None, None), Entry(1, "B", None), None]
    """
    if table:
        index = hash_key(key, len(table))
        if len(table) > index:
            current = table[index]
            loc = index

            while current:
                if current.key != key:
                    index += 1

                if current.key == key:
                    current.nullify()
                    return table

                if index == loc:
                    raise KeyError

                if index >= len(table):
                    index = len(table) % index
                current = table[index]
    raise KeyError
