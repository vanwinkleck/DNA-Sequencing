sequence = input('Enter a DNA sequence: ') ##Ask the user to enter their DNA Sequence
pattern = input('Enter the pattern: ') ##Ask the user for the pattern

reversePattern = pattern[::-1] ##Reverses the pattern in order to search for it backwards later down the line

patternOnePos = sequence.find(pattern) ##These two lines find where the pattern exists within the sequence
patternReversePos = sequence.find(reversePattern, patternOnePos + len(reversePattern))

x = sequence[0:patternOnePos+len(pattern)] ##Contains the begining of the sequence to the end of the first pattern
y = sequence[patternOnePos + len(pattern) : patternReversePos] ##Contains the sequence that lies inbetween two patterns
z = sequence[patternReversePos:] ##Contains the sequence from the end of the second pattern to the end of the sequence
ry = y[::-1] ##Reverses the Y variable explained above
print('Mutated DNA sequence: '+x+ry+z) ##Assembles and prints the new mutated dna sequence 
