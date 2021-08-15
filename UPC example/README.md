# tutoring
 
INSTRUCTIONS (READ BEFORE STARTING): A Universal Product Code or UPC is the most widely used type of barcode in the Anglosphere. It consists of 12 digits, including a check digit at the end. Check digits are used to check for errors in the UPC.

You will write a program which calculates the check digit of a user-input 11 digit UPC code. It is calculated as follows:

Pad the given number with leading zeroes so that it is 11 digits. For example, 12345 becomes 00000012345.
Enqueue these digits into a Queue of Integers.
Dequeue each digit one at a time in a loop:
On odd-numbered iterations, add this value to A.
On even-numbered iterations, add this value to B.
     4)     Calculate M = 3*A + B modulo 10.
     5)    If M is 0, then the check digit is also 0. Otherwise, the check digit is exactly 10 - M.

X = 12345

-loop 11 - 5 = 6 times, and enqueue 0 into the queue that many times
-enqueue each digit in the correct order into the queue
    -use Integer.parseInt(num.substring(i, i+1)) to get each digit in a loop
-the queue should be equal to [0,0,0,0,0,0,1,2,3,4,5]
-loop 11 times, polling each digit from the queue and adding the digits to either A or B

A = 0 + 0 + 0 + 1 + 3 + 5 = 9
B = 0 + 0 + 0 + 2 + 4 = 6

M = (3*9 + 6)%10 = 33%10 = 3

Check digit = 10 - 3 = 7

EXAMPLES: 
    getCheckDigit(12345) = 7
    getCheckDigit(8675309) = 8
    getCheckDigit(99999999999) = 3