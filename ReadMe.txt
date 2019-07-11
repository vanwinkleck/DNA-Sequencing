This was one of the projects I worked on with Ryan Szczepanski for a class taught by Jason Fritts in the spring semester of 2019. To run the program, open it in IDLE and use the "run the module" option. Feel free to use either one of the test DNA sequences in "test.txt" or to enter your own valid DNA sequence.
Because this project was originally hard for us to grasp, I am attaching below the original prompt for the project so you can understand what the goal of this assignment was:

DNA can be modeled as a string of characters using the alphabet A, C, G, and T. One form of DNA mutation occurs when a substring of the DNA is reversed during the replication process. Usually, such a reversal occurs between what are termed inverted pairs, where some substring is followed later by its reversal.As an example, consider the original DNA strand:CGATTGAACATGTAAGTCCAATT 
This example happens to have an inverted pair, with the original marker beingTGAAand its subsequentreversed pair being AAGT as shown below. 
CGATTGAACATGTAAGTCCAATT
It is possible that the entire slice of DNA delimited by those patterns could be inverted and reattached,since the bonds at each end will be locally the same. In that case, the resulting mutated DNA would appear as
CGATTGAATGTACAAGTCCAATT
In effect, the 13 character strand has been flipped, noting that the middle 5 characters TGTAC are effectivley reversed relative to the original strand.You are to design a program that works as follows. It should ask the user for an original DNA string aswell as the particular pattern that is inverted. It should then locate the leftmost occurrence of that pattern,and the next subsequent and disjoint occurrence of the inverted pattern. The output should be the mutatedDNA, with the segment including the inverted pair reversed. An example session might proceed as follows(where the user input is shown in bold):
Entera DNA sequence:CGATTGAACATGTAAGTCCATT
Enter the pattern:TGAA
Mutated DNA sequence:CGATTGAATGTACAAGTCCAATT

Specifications

For the sake of this assignment, you may assume that the user enters valid input, defined as follows.
•The designated pattern will appear at least once within the original DNA sequence
•The original DNA strand will contain at least one occurrence of the reversed pattern that occurs completely after the first occurrence of the forward pattern. 
(Although there may be additional occurrences of the reversed pattern elsewhere.)Your program is responsible for performing only the single mutation that occurs between the first occur-rence of the pattern, and the next subsequent occurrence of the reversed pattern (that which is completely disjoint from the forward pattern).


