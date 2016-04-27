from person import Person


class Kenyan(Person):
	corrupt = False   #default, corrupt until probed

	def probe(self, corrupt):
		self.corrupt = corrupt

	def is_corrupt(self):
		if self.corrupt == True:
			return "Yes, corrupt"
		else:
			return "No, is clean"

		
