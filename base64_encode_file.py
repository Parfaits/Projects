import base64

def encode_File_Base64(fileName):
	data = ""
	with open(fileName, "rb") as file:
		data = base64.b64encode(file.read())
	return data

def file_Output(data):
	newFile = open("b64Data.txt", 'wb')
	newFile.write(data)
	newFile.close()

def main():
	d = encode_File_Base64("2ltbyy.jpg")
	file_Output(d)
	print(d)

if __name__ == '__main__':
	main()