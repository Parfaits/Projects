	.globl avg
	# Description: Take the average of an array
	# di <- A[]
	# si <- n
avg:
	xorl %eax, %eax
	xorl %edx, %edx
	xorl %ecx, %ecx

loop:
	cmpl %ecx, %esi						
	jle endloop							# while  i = 0 to n-1
	addl (%edi, %ecx, 4), %eax			# eax <- eax + A[i]
	incl %ecx							# i++
	jmp loop
endloop:
	idivl %esi							# eax <- dividend, esi <- divisor. eax <- result of division; remainder in edx
	ret
