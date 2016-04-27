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

		
k = Kenyan("Miguna", 50)

k.probe(True)
print "Is {}, corrupt? {}".format(k.name, k.is_corrupt())

print k.say_Hello()

print "-----"
print k.say_Hello() + " and " + k.is_corrupt()