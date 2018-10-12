class GuestBook:

	def __init__(self):
		self.guests = list()

	def add(self, name):
		self.guests.append({"Guest_name": name})

	def remove(self, name):
		for guest in self.guests:
			if guest.get("Guest_name") == name:
				self.guests.remove(guest)

	def write_file(self):
		import json
		with open("./book.json", 'a') as file:
			json_data = {"Guests": self.guests}
			file.write(json.dumps(json_data, ensure_ascii=False, indent=4))

if __name__ == "__main__":
	guestBook = GuestBook()
	guestBook.add("Kunica")
	guestBook.add("User1")
	guestBook.add("User2")

	guestBook.remove("User1")
	guestBook.write_file()

	print(guestBook.guests)
