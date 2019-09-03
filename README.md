# CryptographyAssignment1
Polynomial Multiplication Algorithm

I'm sure that because this is in the $$Z_{256}$$ that we could use bit multiplication to do the same thing faster, I am just not sure how so I prefered to just put out something that worked.

Essentially what I would like to do, but have no idea on how is convert both of the polynomials into a big number in binary, I would store each number in its bit form then separated by 8 0's (to both separate the coordinates and ensure that later I can take everything mod 256) then I would just bitwise multiply both of these numbers and then take every other set of 8 bits to be the new polynomial.

I have no clue how to do this though, but if it was possible / worked it would be significantly better than what I have written.

Untitled is just a jupyter notebook that runs the code, to check it.
