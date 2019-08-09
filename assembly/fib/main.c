#include <stdio.h>

int fib1(int n);

int fib2(int n){
	if (n <= 1) 
      return n; 
   return fib2(n-1) + fib2(n-2);
}

int main(int argc, char const *argv[])
{
	int n = 9;
	puts("C fib sequence:\n");
	for (int i = 0; i <= n; ++i)
	{
		printf("%d ", fib2(i));
	}
	putchar('\n');
	puts("asm fib sequence:\n");
	for (int i = 0; i <= n; ++i)
	{
		printf("%d ", fib1(i));
	}
	putchar('\n');
	return 0;
}
