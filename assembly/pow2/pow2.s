	.globl pow2
	# Description: Calculate 2^n by recursion
	# di <- n
pow2:
    movl 	%edi, %eax    
    cmpl $0, %eax			# return 0
    jle end
 	
 	cmpl $1, %eax			# return 1
 	je end


 	pushq %rax				# save n
 	decl %eax				# n-1
 	movl %eax, %edi
 	call pow2

 	popq %rsi				# n
 	pushq %rax				# save pow2(n-1)
 	decl %esi				# n-1
 	movl %esi, %edi
 	call pow2

 	popq %rdx				# pow2(n-1)
 	addl %edx, %eax 		# pow2(n-1)+pow2(n-2)
end:
    ret
