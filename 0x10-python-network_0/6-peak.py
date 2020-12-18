#!/usr/bin/python3
# find_peak list unsorted integers
def find_peak(list_of_integers):
	num = 0
	for i, j in enumerate(list_of_integers):
		if i + 1 != len(list_of_integers) and i >= 1:
			if i == 1:
				num = len(list_of_integers) -1
			elif list_of_integers[i] > list_of_integers[i-1] and list_of_integers[i] > list_of_integers[i+1]:
				num = list_of_integers[i]
	if num == 0:
		num = None
	return num