import json
import sys
import codecs
def generate_css(theme):
	output = u'''/* {full_name} */

aside.portable-infobox.pi-theme-{name},
.StatBox.{name}{{
    border-color: {title};
}}
 
table.navbox.{name} th.titrePalette,
.pi-theme-{name} .pi-item.pi-title,
.StatBox.{name} th.SectionHeader,
table.Donnees.{name} tr:first-child th {{
	background-color:{title};
	color: {title_font};
}}

table.navbox.{name} th.titrePalette .titreContent a,
table.navbox.{name} a.mw-collapsible-text,
.StatBox.{name} a.mw-collapsible-text,
table.Donnees.{name} tr:first-child th a {{
	color: {title_font};
}}

table.navbox.{name} th,
.{name} .group,
.pi-theme-{name} .pi-item,
.pi-europa.pi-theme-{name} .pi-data-label,
.StatBox.{name} tr.LabelRow,
.StatBox.{name} tr.MixedRow th.Label,
table.Donnees.{name} tr:not(:first-child) th,
table.Donnees.{name} tr:not(:first-child) td.group {{
	background-color:{head};
	color: {head_font};
}}

table.navbox.{name} th a,
.{name} .group a,
.pi-theme-{name} .pi-item > .pi-data-value a,
.StatBox.{name} tr.LabelRow a,
.StatBox.{name} tr.MixedRow th.Label a,
table.Donnees.{name} tr:not(:first-child) th a,
table.Donnees.{name} tr:not(:first-child) td.group a{{
	color: {head_font_link};
}}

table.navbox.{name} tr td,
table.Donnees.{name}.altColor tr:nth-child(even) td,
table.Donnees.{name} td {{
	background-color:{row};
}}

table.navbox.{name} td .subTitle {{
	border-color:{head};
}}

table.navbox.{name} tr:nth-child(odd) td,
.StatBox.{name} tr.DataRow,
.StatBox.{name} tr.MixedRow td.Data,
.pi-theme-{name} .pi-horizontal-group-item:nth-child(even),
.pi-theme-{name} .pi-horizontal-group-item:nth-child(odd),
.pi-theme-{name}.pi-europa .pi-smart-data-label:nth-child(even),
.pi-theme-{name}.pi-europa .pi-smart-data-value:nth-child(even),
.pi-theme-{name}.pi-europa .pi-smart-data-label:nth-child(odd),
.pi-theme-{name}.pi-europa .pi-smart-data-value:nth-child(odd),
.pi-theme-{name} .pi-collapse .pi-item.pi-data,
table.Donnees.{name}.altColor tr:nth-child(odd) td,
table.Donnees.{name} td.altColor {{
	background-color:{row_alt};
	color:{row_alt_font};
}}

table.navbox.{name} tr:nth-child(odd) td a,
.StatBox.{name} tr.DataRow a,
.StatBox.{name} tr.MixedRow td.Data a,
.pi-theme-{name} .pi-horizontal-group-item:nth-child(even) a,
.pi-theme-{name} .pi-horizontal-group-item:nth-child(odd) a,
.pi-theme-{name}.pi-europa .pi-smart-data-label:nth-child(even) a,
.pi-theme-{name}.pi-europa .pi-smart-data-value:nth-child(even) a,
.pi-theme-{name}.pi-europa .pi-smart-data-label:nth-child(odd) a,
.pi-theme-{name}.pi-europa .pi-smart-data-value:nth-child(odd) a,
.pi-theme-{name} .pi-collapse .pi-item.pi-data a,
table.Donnees.{name}.altColor tr:nth-child(odd) td a,
table.Donnees.{name} td.altColor a{{
	color:{row_alt_link_font};
}}

.pi-theme-{name} .pi-group .pi-group + .pi-group.pi-border-color {{
	border-top-color: {title};
}}

.StatTabber.{name} ul.tabbernav li a,
.StatTabber.{name} ul.tabbernav li a:hover,
.StatTabber.{name} ul.tabbernav li a:visited,
.StatTabber.{name} ul.tabbernav li a:link,
ul.SousPages.{name} li a {{
    color:{head};
}}
 
.StatTabber.{name} ul.tabbernav li.tabberactive a,
.StatTabber.{name} ul.tabbernav li.tabberactive a:hover,
ul.SousPages.{name} li.PageActuelle {{
    background-color: {row_alt};
    border-bottom-color:{row_alt};
    color:{row_alt_font};
}}

ul.SousPages.{name} li.PageActuelle {{
    background-color: {row_alt};
    border-bottom-color:{row_alt};
	}}

ul.SousPages.{name} li.PageActuelle a {{
    color:{row_alt_font};
}}



'''.format(name=theme.get("Name"), full_name=theme.get("FullName"), title=theme.get("Title"), title_font=theme.get("TitleFont"), head=theme.get("Head"), head_font=theme.get("HeadFont"), head_font_link=theme.get("HeadFontLink"), row=theme.get("Row"), row_alt=theme.get("RowAlt"), row_alt_font=theme.get("RowAltFont"), row_alt_link_font = theme.get("RowAltLinkFont") )
	return output
	#.group for the sale of compatibility with infoboxes, to remove eventually

if __name__ == '__main__':
	with codecs.open("KHWikiFRCSSThemes.json",encoding="utf-8") as themes_file:
		themes = json.loads(themes_file.read())
	output_builder = ''.join([generate_css(theme) for theme in themes])
	with codecs.open("KHWikiFRCSSThemes.css","w",encoding="utf-8") as output_file:
		output_file.write(output_builder)
		