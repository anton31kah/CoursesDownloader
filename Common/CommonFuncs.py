import importlib
import os
import re
import sys
from os.path import basename

import numpy as np

from Common.CommonVars import CommonVars


class CommonFuncs:
	@staticmethod
	def clear():
		os.system('cls')

	@staticmethod
	def trim_inner_spaces(string):
		return re.sub(r"\s+", " ", str(string))

	@staticmethod
	def remove_inner_spaces(string):
		return re.sub(r"\s+", "", str(string))

	@staticmethod
	def sorted_unique_list(iterable):
		return np.unique(iterable).tolist()

	@staticmethod
	def is_ascending(iterable):
		return all(iterable[i] > iterable[i - 1] for i in range(1, len(iterable)))

	@staticmethod
	def are_ascending(*items):
		return CommonFuncs.is_ascending(items)

	@staticmethod
	def transliterate_mk_to_en(string, chars_map):
		return "".join(chars_map[c] if c in chars_map else c for c in string)

	@staticmethod
	def disable_stdio():
		CommonVars.original_sys_stdin = sys.stdin
		CommonVars.original_sys_stdout = sys.stdout
		CommonVars.original_sys_stderr = sys.stderr
		sys.stdin = open(os.devnull, 'w')
		sys.stdout = open(os.devnull, 'w')
		sys.stderr = open(os.devnull, 'w')

	@staticmethod
	def enable_stdio():
		sys.stdin = CommonVars.original_sys_stdin
		sys.stdout = CommonVars.original_sys_stdout
		sys.stderr = CommonVars.original_sys_stderr
		CommonVars.original_sys_stdin = None
		CommonVars.original_sys_stdout = None
		CommonVars.original_sys_stderr = None

	@staticmethod
	def extract_filename_from_url(url):
		return basename(url)

	@staticmethod
	def class_for_name(module_name, class_name):
		# load the module, will raise ImportError if module cannot be loaded
		m = importlib.import_module(module_name)
		# get the class, will raise AttributeError if class cannot be found
		c = getattr(m, class_name)
		return c
