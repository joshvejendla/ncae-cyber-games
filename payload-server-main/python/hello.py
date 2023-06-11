import pwd, os

print("Hello world!: %s" % pwd.getpwuid(os.getuid()).pw_name)