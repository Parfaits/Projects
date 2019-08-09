all: swag


swag: swag.o avg.o
	gcc -o swag avg.o swag.o

swag.o: swag.s
	gcc -c swag.s

avg.o: avg.s
	gcc -g -c avg.s

swag.s: swag.c
	gcc -O2 -S swag.c

clean:	
	rm -f swag *.o swag.s