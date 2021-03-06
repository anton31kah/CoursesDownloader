import re
import lxml.html

from CoursesClient.CoursesClient import CoursesClient
from CoursesModels.Header import Header
from CoursesModels.Links.FileLink import FileLink
from CoursesModels.Links.FolderLink import FolderLink
from CoursesModels.Section import Section
from Common.CommonVars import CommonVars


def find_id_from_ancestors(html_element):
	anchor_id = html_element.attrib.get('id')
	while not anchor_id:
		html_element = html_element.getparent()
		anchor_id = html_element.attrib.get('id')

	return anchor_id


def extract_sections_for_course(course_link):
	CoursesClient()
	course_page = CoursesClient.session.get(course_link, allow_redirects=True)
	CommonVars.sesskey = re.findall("(?<=sesskey=).{10}", course_page.text)[0]
	course_page_html = lxml.html.fromstring(course_page.text)
	headers_links = course_page_html.xpath(CommonVars.xpath_filter_a_h1_to_h6_with_folders)

	CommonVars.sections = []
	current_section = Section()
	CommonVars.sections.append(current_section)

	for header_link in headers_links:
		if header_link.tag.startswith("h"):
			header_name = next(header_link.itertext())
			header_tag = header_link.tag
			header_id = find_id_from_ancestors(header_link)
			current_section = Section(Header(header_name, header_tag, header_id))
			CommonVars.sections.append(current_section)
		elif 'resource' in header_link.attrib['href']:  # header_link.tag.startswith("a")
			current_section.links.append(FileLink(next(header_link.itertext()), header_link.attrib['href']))
		elif 'folder' in header_link.attrib['href']:  # header_link.tag.startswith("a")
			current_section.links.append(FolderLink(next(header_link.itertext()), header_link.attrib['href']))

	CommonVars.sections = [section for section in CommonVars.sections if section.links]

	return CommonVars.sections
