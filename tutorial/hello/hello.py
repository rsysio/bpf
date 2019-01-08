from bcc import BPF

prog = '''
int hello(void *ctx) {
    bpf_trace_printk("connected!\\n");
    return 0;
}
'''
b = BPF(text=prog)

b.attach_kprobe(event=b.get_syscall_fnname("connect"), fn_name="hello")

b.trace_print()
