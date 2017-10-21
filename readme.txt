Write
---

Add to ~/.bash_profile:  `alias journal="cd /path/to/journal && ./write_journal"`
Start a new terminal
Run `journal`
Enter your password
Write down some deep dark secrets
Save and quit your text editor
Enter your password again
All done.  Your files are stored in the encrypted directory.

Read
---

cd /path/to/journal

# Decrypt the encrypted files and save them in the decrypted dir
./read_journal

# Reencrypt the decrypted files and delete the decrypted dir
./lock

Misc
----

Inspired by this article:
http://www.spring.org.uk/2017/09/how-to-make-your-brain-think-faster-under-stress.php

MIT license
