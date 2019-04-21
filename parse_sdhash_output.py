import csv

# Purpose: read in SSDEEP output and print findings.
# Author: Tanner Glantz

def main():
	print("------------------")
	print("Stats from sdhash:")
	print("------------------")
	file = open("sdhash_results", "r")
	results = csv.reader(file, delimiter='|')
	outputFile = open("sdhash_stats", "w")
	for row in results:
		outputFile.write("score:"+str(row[2])+"\n")
		print ("Score: " + str(row[2]) +" [Range: -1 to 100]")
	outputFile.close()
if __name__ == "__main__":
	main()

