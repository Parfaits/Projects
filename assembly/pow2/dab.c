#include <stdio.h>

int pow2(int n);

int main(int argc, char const *argv[])
{
	int n = 9;
	for (int i = 0; i <= n; ++i)
	{
		printf("%d ", pow2(i));
	}
	puts("\n");
	return 0;
}