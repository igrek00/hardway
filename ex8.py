# -*- coding: utf-8 -*-
formatter = "%s, %s, %s, %s"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
		"I had this thing.",
		"That u could type up right.",
		"But it didn't sing.",
		"So I said goodnight."
		)
