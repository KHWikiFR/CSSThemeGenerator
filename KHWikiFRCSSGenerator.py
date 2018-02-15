import json
import sys
import codecs
def generate_css(theme):
	output = u'''/* {full_name} */

aside.portable-infobox.pi-theme-{name} {{
    border-color: {title};
}}
 
table.navbox.{name} th,
.pi-theme-{name} .pi-item.pi-title {{
	background-color:{title} !important;
	color: {title_font};
}}

table.navbox.{name} .titrePalette .titreContent a {{
    color: {title_font};
}}

table.navbox.{name} .collapseButtonLink {{
	color: {title_font};
}}

table.navbox.{name} th:not(.titrePalette),
.{name} .group,
.pi-theme-{name} .pi-item {{
	background-color:{head};
	color: {head_font};
}}

table.navbox.{name} th:not(.titrePalette) a,
.{name} .group a{{
	color: {head_font};
}}

.pi-theme-{name} .pi-item a {{
	color: {head_font};
	font-weight: bold;
}}

table.navbox.{name} tr td {{
	background-color:{row};
}}

table.navbox.{name} tr:nth-child(odd) td {{
	background-color:{row_alt};
}}

.pi-theme-{name} .pi-horizontal-group-item:nth-child(even),
.pi-theme-{name} .pi-horizontal-group-item:nth-child(odd),
.pi-theme-{name} .pi-collapse .pi-item.pi-data {{
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


