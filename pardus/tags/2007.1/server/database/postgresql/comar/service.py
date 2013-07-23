serviceType="server"
serviceDesc = _({"en": "PostgreSQL Database Server",
                 "tr": "PostgreSQL Veritabanı Sunucusu"})
serviceConf = "postgresql"

from comar.service import *

def check_postgresql():
    if not os.path.exists(config.get("PGDATA", "/var/lib/postgresql/data")):
        fail("PostgreSQL is not installed")

def start():
    check_postgresql()
    ret = os.system("su - %s -c \"/usr/bin/pg_ctl start \
                     -D '%s' -s -l '%s' -o '%s'\"" % (config.get("PGUSER", "postgres"),
                                                      config.get("PGDATA", "/var/lib/postgresql/data"),
                                                      config.get("PGLOG", "/var/lib/postgresql/data/postgresql.log"),
                                                      config.get("PGOPTS", "")))
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = os.system("su - %s -c \"/usr/bin/pg_ctl stop \
                     -D '%s' -s -m fast\"" % (config.get("PGUSER", "postgres"),
                                              config.get("PGDATA", "/var/lib/postgresql/data")))
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def reload():
    os.system("su - %s -c \"/usr/bin/pg_ctl reload \
               -D '%s' -s\"" % (config.get("PGUSER", "postgres"),
                                config.get("PGDATA", "/var/lib/postgresql/data")))

def status():
    pid = "%s/postmaster.pid" % config.get("PGDATA", "/var/lib/postgresql/data")
    return checkDaemon(pid)
