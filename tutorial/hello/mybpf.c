int hello(void *ctx) {

    bpf_trace_printk("connected!\\n");

    return 0;
}