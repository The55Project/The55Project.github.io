#Name: Liang Dong
#Penn ID: 

#The START codon is ATG
#The STOP  codon is TAG, TAA, TGA
codonTable = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M','ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K','AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L','CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q','CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S','TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_','TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',}

#input = "ABCDEFGHIJKLMNOP"

#This function takes "ABCDEFGHIJKLMNOP" and turns it into
#              ["ABC","DEF","GHI","JKL","MNO"]

def stringToCodons(input):
  # write your function here
  result = []  
  iteriate = 0
  for x in input:
    stringStorage = input[iteriate]+input[iteriate+1]+input[iteriate+2]
    result.append(stringStorage)
    iteriate = iteriate + 3

    if (iteriate+2) >= len(input):
      break


  return result


def startCodonFinder():
  # write your function here


  return


def stopCodonFinder():
  # write your function here
  return


def codonsToAminoAcids():
  # write your function here
  return


def decideToTranslate():
  # write your function here
  return


def findLongestProtein():
  # write your function here
  return


def main():
  # write your function here
  stringToCodons("ABCDEFGHIJKLMNOP")

  return


#Don't change this!
if __name__ == "__main__":
    main()