#include <stdio.h>
#include <time.h>
#include <math.h>

//My implementation of the bitfield approach to the n-queens problem
//The checker has 1's for all valid columns and is essentially what the down integer should eventually equal
unsigned int checker = 0;
//Number of solutions
unsigned int permCount = 0;
//The left int and right int are shifted before being passed to the next recursion level (row)
//The bits in each integer represent a space in the current row being attacked
//Each level of recursion represent the next row down the perspective of how it conceptually proceeds through the board is irrelevant (top to bottom or left to right)
void bitRecurse(unsigned int down, unsigned int left, unsigned int right)
{
	//All bits in available represent columns not currently being attacked on this row
	unsigned int available = ~(down | left | right) & checker;
	//This represents our current column being checked, it will be bitwise-or'd into the comparison ints when the next call is made
	unsigned int bit = 1;
	//Once all available bits have been turned off we have nothing left to check
	while(available)
	{
		//If our current bit matches an available bit then we can place it there
		if(available & bit)
		{
			//If placing this next queen fills all columns then we have finished, increment the count and exit the function
			if((down | bit) == checker)
			{
				permCount++;
				break;
			}
			else
			{
				//Add in the bit to the comparison ints, shift the resulting right and left ints because the next level of recursion will be one row down
				bitRecurse(down | bit, (left | bit) << 1, (right | bit) >> 1);
			}
			//Turn off the available bit that corresponds to the column we just checked
			available ^= bit;
		}
		//Go to the next column position
		bit = bit << 1;
	}
}

void main()
{
	unsigned int listLen;
	printf("NxN value: ");
	scanf("%i", &listLen);

	time_t start, end;
	time(&start);
	//Create an int with bits representing all available columns to filter out invalid columns and to validate the final solution
	checker = pow(2, listLen) - 1;
	bitRecurse(0, 0, 0);
	time(&end);
	printf("Seconds: %i\n", (int)(end - start));
	printf("Number of solutions: %i\n", permCount);
}