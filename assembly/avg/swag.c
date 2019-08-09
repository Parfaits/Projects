#include <stdio.h>
#include <stdlib.h>

int avg(int *, int);

int main(int argc, char const *argv[])
{
	int* swag;
	int size, n, x;
	swag = (int *) malloc(5*sizeof(int));
	printf("Gibe me the numbers b0us:\n");
	size = 5;
	n = 0;
	while(scanf("%d", &swag[n]) != EOF){
		if (n >= size)
		{
			swag = (int *) realloc(swag, size*5*sizeof(int));
			size = size*5;
		}
		n++;
	}
	putchar('\n');
	x = avg(swag, n);
	printf("I got the monies b0us: %d\n", x);
	free(swag);
	return 0;
}