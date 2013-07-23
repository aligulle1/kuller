import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("chmod 4755 /sbin/pam_timestamp_check")
    os.system("chmod 4755 /sbin/unix_chkpwd")
