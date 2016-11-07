def readUser(uName=None, param="name"):

	users = []
	with open("mockDB.txt", "r") as fo:


		data = fo.read().split('\n')


		for idx, line in enumerate(data):
			if (data[idx] == uName) and (idx % 2 == 0):
				user = {
					param : data[idx],
					"password" : data[idx+1]
				}

				users.append(user)

	return users

def addUser(uName, password):

	if not uName:
		raise ValueError("dafaq, no username.")
	elif not password:
		raise ValueError("dafaq, no password.")

	with open("mockDB.txt", "r") as fo:
		data = fo.read()


	with open("mockDB.txt", "a") as fo:


		if not data:
			fo.write(uName + '\n' + password)
		else:
			fo.write('\n' + uName + "\n" + password)


	return True
