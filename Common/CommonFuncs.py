import os
import re

import numpy as np


def clear():
	os.system('cls')


def trim_inner_spaces(string):
	return re.sub(r"\s+", " ", str(string))


def remove_inner_spaces(string):
	return re.sub(r"\s+", "", str(string))


def sorted_unique_list(iterable):
	return np.unique(iterable).tolist()


def is_ascending(iterable):
	return all(iterable[i] > iterable[i - 1] for i in range(1, len(iterable)))


def are_ascending(*items):
	return is_ascending(items)


def transliterate_mk_to_en(string, chars_map):
	return "".join(chars_map[c] if c in chars_map else c for c in string)