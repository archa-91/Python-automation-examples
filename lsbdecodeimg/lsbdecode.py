from PIL import *
import Image

def Bintoascii(decmsg):
	x=''
	for i in range(len(decmsg)/8):
		x = x+(chr(int(''.join(decmsg[i*8:(i+1)*8]),2)))

	return x

def decodeLSB(encdata):
	value = str(bin(encdata))[-1]
	return value


def decode(img):
	pixels, mode = list(img.getdata()), img.mode
	header, trailer = 2*"11001100",2*"0101010100000000"
	trailer = list(trailer)
#	print trailer	
	databin = []  
	for i in range(len(pixels)):
		newPixel = list(pixels[i])
		#print newPixel[0]
		databin.append(decodeLSB(newPixel[i%len(mode)]))
		if databin[-32:] == trailer:
			return databin[16:-32:]

if __name__ == "__main__":
	img = Image.open("Secret.png")
	decmsg = decode(img)
	msg = Bintoascii(decmsg)
	print msg
