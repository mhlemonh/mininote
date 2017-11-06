import os
import re
import time

def read_note():
	current_dir = os.getcwd()
	note_pages=[]
	with open(current_dir+"/note.txt", "r") as note:
		time_stamp_re = re.compile("@ [\d]{2}\/[\d]{2} [\d:]{5} --")
		for line in note:
			result = time_stamp_re.search(line)
			if result:
				try:
					note_pages.append(context)
				except UnboundLocalError:
					pass
				context = line
			else:
				context += line
		else:
			try:
				note_pages.append(context)
			except UnboundLocalError:
				pass

	for note in reversed(note_pages):
		print note,

	return note_pages

def write_note(note, time_stamp):
	add_time_stamp = True
	while True:
		line = raw_input("")
		if line == "q":
			break
		else:
			if add_time_stamp:
				note.write(time_stamp+'\n')
				add_time_stamp = False
			note.write(line+'\n\n')

def current_time():
	return time.strftime("@ %m/%d %H:%M --")

def main():
	current_dir = os.getcwd()
	last_notes = read_note()
	time_stamp = current_time()
	print time_stamp
	with open(current_dir+"/note.txt", "w+") as note:
		write_note(note, time_stamp)
		for last_note in last_notes:
			note.write(last_note)

if __name__ == '__main__':
	main()