from comar.service import *

serviceType = "script"
serviceDesc = _({"en": "KExec Tools",
                 "tr": "KExec Araçları"})
serviceConf = "kexec"

def start():
    kname = config.get("KNAME", "bzImage")
    bootpath = config.get("BOOTPATH", "/boot")
    bootmount = config.get("BOOTMOUNT", "0")
    rootpart = config.get("ROOTPART", [i.split(" ")[0] for i in open("/etc/mtab") if i.split(" ")[1] == "/"][0])
    kparam = config.get("KPARAM", "")
    initrdopt = config.get("INITRDOPT", "")

    if kname != "-":
        mnt = len([i.split(" ")[1] for i in open("/etc/mtab") if i.split(" ")[1] == bootpath])
        if bootmount == "1" and not mnt:
            mnt = run("/bin/mount %s" % bootpath)

        run("/usr/sbin/kexec -l %s/%s --append=\"root=%s %s\" %s" % (bootpath, kname, rootpart, kparam, initrdopt))

        if bootmount == "1" and not mnt:
            run("/bin/umount %s" % bootpath)

    else:
        run("/usr/sbin/kexec -u")
