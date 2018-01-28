import string

if __name__ == "__main__":
	bin_data = open("./reverse", 'rb').read()
	hex_data = bin_data.encode('hex')
	png_data = hex_data[::-1]
	pngbin = png_data.decode('hex')
	
	pngfile = open("q3.png",'wb')
	pngfile.write(pngbin)
	pngfile.close()
	#print png_data
	
