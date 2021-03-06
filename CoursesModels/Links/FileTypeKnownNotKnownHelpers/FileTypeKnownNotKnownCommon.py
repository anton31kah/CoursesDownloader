import os
import re
from pathlib import Path


class FileTypeKnownNotKnownCommon:
	valid_filename_regex = r"^[\w\-. ]+$"
	illegal_chars_regex = r"[^\w\-. ]"

	default_location = f"{Path.home()}\\Downloads\\"

	@classmethod
	def prepare_valid_file_path(cls, filename):
		filename = re.sub(cls.illegal_chars_regex, "_", filename)
		filename = cls.default_location + filename
		return filename

	@staticmethod
	def _handle_file_name_exists(filename, file_type):
		i = 1
		new_filename = filename
		while os.path.isfile(f"{new_filename}{file_type}"):
			new_filename = f"{filename}_{i}"
			i += 1

		return new_filename
