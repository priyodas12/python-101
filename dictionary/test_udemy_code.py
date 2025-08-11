islands = {
	'Wano': ['Road Poneglyph', 'Historical Poneglyph'],
	'Zou': ['Road Poneglyph'],
	'Alabasta': ['Historical Poneglyph']
}


def collect_poneglyph_types(island_test):
	for island in island_test.keys():
		values=island_test.get(island)
		comma_seperated_values=','.join(values)

		print(f"On {island}, the crew collected the following Poneglyphs: {comma_seperated_values}.")

	total_poneglyph = set()
	for island in island_test.keys():
		list_poneglyph = island_test.get(island)
		for l in list_poneglyph:
			total_poneglyph.add(l)

	print(f"Total unique Poneglyph types collected: {len(total_poneglyph)}")
	return total_poneglyph


collect_poneglyph_types(islands)

#Error details
#'On Island1, the crew collected the following Poneglyphs: Type1, Type2.'
#not found in 'On Island1,the crew collected the following Poneglyphs: Type1,Type2.
# \nOn Island2,the crew collected the following Poneglyphs: Type2,Type3.\n
# On Island3,the crew collected the following Poneglyphs: Type1,Type3.\nTotal unique Poneglyph types collected: 3\n' :
# Incorrect Poneglyphs collected on Island1