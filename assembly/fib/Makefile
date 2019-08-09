all: main


main: main.o fib1.o
	gcc -o main fib1.o main.o

main.o:	main.s
	gcc -c main.s

fib1.o:	fib1.s
	gcc -g -c fib1.s

main.s:	main.c
	gcc -O2 -S main.c


clean:	
	rm -f main *.o main.s
