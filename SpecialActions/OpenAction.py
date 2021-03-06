import webbrowser

from SpecialActions.OpenCopyBaseAction import OpenCopyBaseAction


class OpenAction(OpenCopyBaseAction):
	type = "Open"
	method_to_use = webbrowser.open_new_tab

	@classmethod
	def handle(cls, input_string):
		super().handle(input_string)

	@classmethod
	def set_action_idx_pointer(cls, level):
		return super().set_action_idx_pointer(level)

	@classmethod
	def handle_multiple_links(cls, selected_links):
		for link in selected_links:
			cls.method_to_use(link.url)
