addi x1, x0, 1
add x2, x1, x1
beq x1, x2, 200
jal x1, 200
sw x2, 0(x1)