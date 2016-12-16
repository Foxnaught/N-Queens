#include <stdio.h>
#include <time.h>

//Global variable that holds the number of permutations
int permCount = 0;
int listLen = 0;

//Recursive function that takes an array of row values representing where a queen has been placed
//-1 represents a column with no queen
//My original attempt at the nqueens problem, falls short because it uses an array of ints when 3 ints can be used instead
void getPerms(int* excludeList, unsigned int row)
{
	unsigned int i = listLen;
	int newExclude[listLen];
	//Optimized for loop, order of index doesn't matter
	for(;i--;)
	{
		if(excludeList[i] == -1)
		{
			unsigned int t = listLen;
			_Bool found = 0;
			//Optimized for loop, order of index doesn't matter
			for(;t--;)
			{
				if(excludeList[t] != -1)
				{
					//If the column difference equals the row difference then it is diagonal.
					if(i - t == row - excludeList[t] || i - t == -row + excludeList[t])
					{
						found = 1;
						break;
					}
				}
			}

			//There was a conflicting diagonal
			if(!found)
			{
				if(row == listLen - 1)
				{
					permCount++;
				}
				else
				{
					//Copy into newExclude and change a column, pass that to the recursive function
					memcpy(newExclude, excludeList, listLen * sizeof(int));
					newExclude[i] = row;
					getPerms(newExclude, row+1);
				}
			}
		}
	}
}

int main()
{
	int i;
	printf("NxN value: ");
	scanf("%i", &listLen);

	int excludeList[listLen];
	for(i=0;i<listLen;i++)
	{
		excludeList[i] = -1;
	}

	time_t start, end;
	time(&start);

	getPerms(excludeList, 0);


	time(&end);
	printf("Seconds: %f\n", (float) (end - start));
	printf("%i\n", permCount);

	return 0;
}