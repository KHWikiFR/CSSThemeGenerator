import json
import sys
import codecs
def generate_css(theme):
	output = u'''/* {full_name} */

.{name} th {{
	background-color:{title} !important;
	color: {title_font};
}}

.{name} .titrePalette .titreContent a {{
    color: {title_font};
}}

.{name} .collapseButtonLink {{
	color: {title_font} !important;
}}

.{name} th:not(.titrePalette),
.{name} .group {{
	background-color:{head}!important;
	color: {head_font};
}}

.{name} th:not(.titrePalette),
.{name} .group a{{
	color: {head_font};
}}

.{name} tr {{
	background-color:{row};
}}

.{name} tr:nth-child(odd) .liste {{
	background-color:{row_alt};
}}

'''.format(name=theme.get("Name"), full_name=theme.get("FullName"), title=theme.get("Title"), title_font=theme.get("TitleFont"), head=theme.get("Head"), head_font=theme.get("HeadFont"), row=theme.get("Row"), row_alt=theme.get("RowAlt") )
	return output
	#.group for the sale of compatibility with infoboxes, to remove eventually

if __name__ == '__main__':
	with codecs.open("KHWikiFRCSSThemes.json",encoding="utf-8") as themes_file:
		themes = json.loads(themes_file.read())
	output_builder = ''.join([generate_css(theme) for theme in themes])
	with codecs.open("KHWikiFRCSSThemes.css","w",encoding="utf-8") as output_file:
		output_file.write(output_builder)


