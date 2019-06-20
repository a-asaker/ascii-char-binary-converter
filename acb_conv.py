#!/usr/bin/env python3

from sys import argv

def ascToChar():
	print("\t+----------------+---------------+----------------------+")
	print("\t| \tAscii \t | \tChar \t |\t  Binary\t|")
	print("\t+----------------+---------------+----------------------+")
	for asc in argv[2:]:
		try:
			asc=int(asc)
			print("\t| \t {} \t | \t {} \t |\t  {}\t|".format(asc,chr(asc),bin(asc)[2:]))
		except Exception as e:
			print("\t| \t {} \t |\t{} \t |\t  {}\t|".format(asc,"Invalid Ascii",""))
	print("\t+----------------+---------------+----------------------+")

def binToChar():
	print("\t+-----------------------+----------------+---------------+")
	print("\t|\t Binary \t|\tChar\t |\tAscii\t |")
	print("\t+-----------------------+----------------+---------------+")
	for bina in argv[2:]:
		try:
			inte=int(bina,2)
			print("\t|\t {} \t|\t {}\t |\t {}\t |".format(bina,chr(inte),inte))
		except Exception as e:
			print("\t|\t {} \t=>\t{}\t |\t {}\t |".format(bina,"Invalid Binary",""))
	print("\t+-----------------------+----------------+---------------+")

def charToAsc():
	print("\t+----------------+---------------+----------------------+")
	print("\t| \tChar \t | \tAscii \t |\t  Binary\t|")
	print("\t+----------------+---------------+----------------------+")
	for char in argv[2:]:
		try:
			try:
				char=str(char)
				print("\t| \t {} \t | \t {} \t |\t  {} \t|".format(char,ord(char),bin(ord(char))[2:]))
			except:
				print("\t| \t {} \t | \t {} \t |\t  {} \t|".format(char),"Invalid Character","")
		except:
			pass
	print("\t+----------------+---------------+----------------------+")


def usage():
	print(""" [#] ASCII-Character-Binary Converter By A_Asaker.
 [-] Usage : ./acb_conv.py [option] [data]
 [*] Options : 
 	 -a : Converts ASCII To Char And Binary,
		  Data Should Be Integers.
	 -c : Converts Char To ASCII,Binary.
		  Data Should Be Characters.
	 -b : Converts Binary To Char And ASCII,
		  Data Should Be binary.
 [~] Examples :
 	      ~ ./acb_conv.py -a 67 34 546
  	    ~ ./acb_conv.py -c a 3 $
	      ~ ./acb_conv.py -a 234 52 
	      ~ ./acb_conv.py -b 110100 1001000 101101""")
	exit(0)

def main():
	if (len(argv)==1):
		usage()
	if argv[1]=="-c":
		charToAsc()
	elif argv[1]=="-a":
		ascToChar()
	elif argv[1]=="-b":
		binToChar()		
	else:
		usage()

if __name__ == '__main__':
	main()
