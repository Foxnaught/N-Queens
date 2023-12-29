#include <stdio.h>
#include <time.h>
#include <math.h>
int checker = 0;
int permCount = 0;
void bitRecurse(int down, int left, int right)
{
	int available = ~(down | left | right) & checker;
	int bit = 1;
	while(available)
	{
		if(available & bit)
		{
			if((down | bit) == checker)
			{
				permCount++;
				break;
			}
			else
			{
				bitRecurse(down | bit, (left | bit) << 1, (right | bit) >> 1);
			}
			available ^= bit;
		}
		bit = bit << 1;
	}
}

void main()
{
	int listLen;
	printf("NxN value: ");
	scanf("%i", &listLen);
	time_t start, end;
	time(&start);
	checker = pow(2, listLen) - 1;
	bitRecurse(0, 0, 0);
	time(&end);
	printf("Seconds: %d\n", (int)(end - start));
	printf("Number of solutions: %i\n", permCount);
}