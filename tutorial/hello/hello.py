from bcc import BPF

b = BPF(src_file='mybpf.c')

b.attach_kprobe(event=b.get_syscall_fnname("connect"), fn_name="hello")

b.trace_print()
