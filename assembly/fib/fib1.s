	.globl fib1
	# Description: Calculate the nth fibonnaci sequence by recursion
	# di = n
fib1:
    movl 	%edi, %eax    	# eax <- n
    cmpl $0, %eax			# base case: F_0 = 0
    jle end
 	
 	cmpl $1, %eax			# base case: F_1 = 1
 	je end


 	pushq %rax				# save n
 	decl %eax				# n-1
 	movl %eax, %edi
 	call fib1 				# fib1(n-1)

 	popq %rsi				# rsi <- n
 	pushq %rax				# save fib1(n-1)
 	decl %esi
 	decl %esi				# n-2
 	movl %esi, %edi
 	call fib1 				# fib1(n-2)

 	popq %rdx				# rdx <- fib1(n-1)
 	addl %edx, %eax 		# eax <- fib1(n-1)+fib1(n-2)
end:
    ret
