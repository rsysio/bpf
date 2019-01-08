from bcc import BPF

code = '''
int kprobe__sys_connect(void *ctx) {
    bpf_trace_printk("connected!\\n");
    return 0;
}
'''

BPF(text=code).trace_print()