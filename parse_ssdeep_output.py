from decimal import *

# Purpose: read in SSDEEP output and print findings.
# Author: Tanner Glantz

def main():
	file = open("ssdeep_comparison", "r")
	# read past first line of output
	file.readline()	
	filea_data = file.readline()
	fileb_data = file.readline()
	file.close()
	totalCount = 0
	similarities = 0
	index = 0
	max_len = len(filea_data)
	while index < max_len:
			totalCount +=1
			if filea_data[index] == "," or fileb_data[index] == ",":
				index = max_len
				totalCount -=1
				break
			elif filea_data[index] == fileb_data[index]:
				similarities +=1
				index +=1
			else:
				index+=1
				continue
	print("------------------")
	print("Stats from ssdeep:")
	print("------------------")
	print("Total Count: " + str(totalCount))
	print("Similarities: " + str(similarities))
	ratio = (Decimal(similarities)/Decimal(totalCount) * 100)
	print ("Hash similarity detected: " + str(ratio)[:5] + "%")

	outputFile = open("ssdeep_stats", "w")
	outputFile.write("count:"+str(totalCount)+",ratio:"+str(ratio)[:5]+"\n")
	outputFile.close()
if __name__ == "__main__":
	main()

