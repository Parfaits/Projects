all: dab

dab: dab.o pow2.o
	gcc -o dab pow2.o dab.o

dab.o: dab.s
	gcc -c dab.s

pow2.o: pow2.s
	gcc -g -c pow2.s

dab.s: dab.c
	gcc -O2 -S dab.c

clean:	
	rm -f dab *.o dab.s