sequence = input('Enter a DNA sequence: ')
pattern = input('Enter the pattern: ')

reversePattern = pattern[::-1]

patternOnePos = sequence.find(pattern)
patternReversePos = sequence.find(reversePattern, patternOnePos + len(reversePattern))

x = sequence[0:patternOnePos+len(pattern)]
y = sequence[patternOnePos + len(pattern) : patternReversePos]
z = sequence[patternReversePos:]
ry = y[::-1]
print('Mutated DNA sequence: '+x+ry+z)
