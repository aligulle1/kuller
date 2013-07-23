#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# wine-update-menus.py:   This script converts windows link files to desktop files which
#                         is compliant to XDG menu standards.
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Fatih Aşıcı <fatih.asici [at] gmail.com>

import os
import codecs
import xml.dom.minidom as mdom

user_name = os.environ["USER"]
user_home = os.environ["HOME"]

profiles = ["All Users", user_name]
profiles_dir = os.path.join(user_home, ".wine/drive_c/windows/profiles/")
desktop_dir = os.path.join(user_home, "Desktop")
localmenu_dir = os.path.join(user_home, ".local/share/applications/wine")
icon_dir = os.path.join(user_home, ".icons")
xml_file = os.path.join(user_home, ".config/menus/applications-merged/wine-programs.menu")

desktop_file_template = """[Desktop Entry]
Name=%s
Comment=%s
Type=Application
Categories=Application;%s;
StartupNotify=false
Exec=%s
Icon=%s
"""

wine_menu_name = "Wine Windows Emulator"

desktop_links = []

def myhash(str):
    return hex(hash(str))[2:]

class Shortcut:
    def __init__(self, lnk_path, mode = "desktop"):
        self.mode = mode
        self.lnk_full_path = os.path.abspath(lnk_path)
        dirs = self.lnk_full_path[len(profiles_dir):].split("/")
        self.profile = dirs[0]
        self.group_dirs = "/".join(dirs[2:-1])
        self.file_name = dirs[-1]
        self.link_name = os.path.splitext(self.file_name)[0]
        self.icon_file = os.path.join(user_home, ".icons", self.link_name + ".xpm")
        if not os.path.exists(self.icon_file):
            self.icon_file = "exec_wine"
        self.lnkinfo = get_lnk_info(self.lnk_full_path)
        if mode == "desktop":
            self.category = "Wine-Shortcut"
        else:
            self.category = "Wine-" + myhash(self.group_dirs)
        cmd = self.get_local_path().replace("\\", "\\\\")
        p1 = cmd.split(" ")[0]
        if not (p1.endswith(".exe") or p1.endswith(".EXE")):
            cmd = '"' + cmd + '"'
        if self.get_work_dir():
            self.command = 'wine-start -D "%s" %s' % (winepath2unix(self.get_work_dir()),
                                                        cmd)
        else:
            self.command = 'wine-start %s' % cmd

    def get_local_path(self):
        if self.lnkinfo.has_key("LocalPath"):
            return self.lnkinfo["LocalPath"]
        else:
            return ""

    def get_work_dir(self):
        if self.lnkinfo.has_key("Working directory"):
            return self.lnkinfo["Working directory"]
        else:
            return ""

    def get_description(self):
        if self.lnkinfo.has_key("Description"):
            return self.lnkinfo["Description"]
        else:
            return ""

    def desktop_entry(self):
        return desktop_file_template % (self.link_name,
                                        self.get_description(),
                                        self.category,
                                        self.command,
                                        self.icon_file)

    def write_desktop_file(self):
        global desktop_links
	
        if self.mode == "desktop":
            target = desktop_dir
            desktop_links.append(self.link_name + ".desktop")
        else:
            target = os.path.join(localmenu_dir, self.group_dirs)

        if not os.path.exists(target):
            os.makedirs(target)
        desktop_file = open(os.path.join(target, self.link_name + ".desktop"), "w")
        desktop_file.write(self.desktop_entry())
        desktop_file.close()

def winepath2unix(wpath):
    winepath = os.popen('winepath -u "%s" | head -n 1' % wpath.replace("\\", "\\\\"))
    unixpath = winepath.read().rstrip("\n")
    winepath.close()
    return unixpath

def path2grp(path):
    return path.split("/")

def grp2path(group):
    return "/".join(group)

def get_lnk_info(lnkfile):
    link_info = os.popen('lnkinfo "' + lnkfile + '"')
    lines = link_info.readlines()
    link_info.close()
    lst = []
    for line in lines:
        item = line.strip("\n").split("=")
        if len(item) == 2:
            lst.append(item)
    return dict(lst)

def add_links(mode, group_dir, lnks):
    for lnk in lnks:
        if lnk.endswith(".lnk"):
            sc = Shortcut(os.path.join(group_dir, lnk), mode)
            sc.write_desktop_file()

def remove_empty_dirs(arg, gdir, fnames):
    if os.path.samefile(gdir, localmenu_dir):
        return
    if len(fnames) == 0:
        os.removedirs(gdir)

def clean_up(skip, gdir, fnames):
    group_dirs = gdir[skip+1:]
    for file in fnames:
        if file.endswith(".desktop"):
            remove = 1
            for prf in profiles:
                if os.path.exists(os.path.join(profiles_dir, prf, "Start Menu", group_dirs, os.path.splitext(file)[0] + ".lnk")):
                    remove = 0
            if remove:
                os.remove(os.path.join(gdir, file))

def appendTree(doc, parentNode, directory, group_dirs):
    for item in os.listdir(directory):
        fpath = os.path.join(directory, item)
        if os.path.isdir(fpath):
            group_dirs2 = os.path.join(group_dirs, item)
            menu = xml_add_group(doc, parentNode, item, group_dirs2)
            appendTree(doc, menu, fpath, group_dirs2)

def xml_add_group(doc, parentNode, name, group_dirs):
    menu = parentNode.appendChild(doc.createElement("Menu"))
    menu_name = menu.appendChild(doc.createElement("Name"))
    menu_name.appendChild(doc.createTextNode(name))

    category = "Wine-" + myhash(group_dirs)
    menu_include = menu.appendChild(doc.createElement("Include"))
    menu_include_category = menu_include.appendChild(doc.createElement("Category"))
    menu_include_category.appendChild(doc.createTextNode(category))
    return menu

def write_xml_file():
    impl = mdom.getDOMImplementation()
    doc = impl.createDocument(None, "Menu", None)
    root = doc.documentElement

    p = root.appendChild(doc.createElement("Menu"))
    p_name = p.appendChild(doc.createElement("Name"))
    p_name.appendChild(doc.createTextNode("Utilities"))

    w = p.appendChild(doc.createElement("Menu"))
    w_name = w.appendChild(doc.createElement("Name"))
    w_name.appendChild(doc.createTextNode(wine_menu_name))
    category = "Wine-" + myhash("")
    w_include = w.appendChild(doc.createElement("Include"))
    w_include_category = w_include.appendChild(doc.createElement("Category"))
    w_include_category.appendChild(doc.createTextNode(category))

    appendTree(doc, w, localmenu_dir, "")

    layout = w.appendChild(doc.createElement("Layout"))
    merge = layout.appendChild(doc.createElement("Merge"))
    merge.setAttribute("type", "menus")
    access_menu = layout.appendChild(doc.createElement("Menuname"))
    access_menu.appendChild(doc.createTextNode("Tools"))
    merge = layout.appendChild(doc.createElement("Merge"))
    merge.setAttribute("type", "files")

    cfg_dir = os.path.split(xml_file)[0]
    if not os.path.exists(cfg_dir):
        os.makedirs(cfg_dir)
    f = codecs.open(xml_file, "w", "utf-8")
    f.write(doc.toxml())
    f.close()
    #print doc.toprettyxml()

def main():
    global desktop_links

    # Make shortcuts
    for profile in profiles:
        top = os.path.join(profiles_dir, profile, "Desktop")
        os.path.walk(top, add_links, "desktop")
    for profile in profiles:
        top = os.path.join(profiles_dir, profile, "Start Menu")
        os.path.walk(top, add_links, "menu")

    # Some clean up
    df = os.path.join(desktop_dir, ".wine-shortcuts")
    try:
        files = open(df).readlines()
    except IOError:
        files = []

    for file in files:
        file = file.strip("\n")
        remove = True
        for prf in profiles:
            if os.path.exists(os.path.join(profiles_dir, prf, "Desktop", os.path.splitext(file)[0] + ".lnk")):
                remove = False
        dfile = os.path.join(desktop_dir, file)
        if remove and os.path.exists(dfile):
            os.remove(dfile)

    skip = len(localmenu_dir)
    os.path.walk(localmenu_dir, clean_up, skip)
    os.path.walk(localmenu_dir, remove_empty_dirs, None)

    scfile = open(df, "w")
    for link in desktop_links:
        scfile.write(link + "\n")
    scfile.close()

    if not os.path.exists(localmenu_dir):
        os.makedirs(localmenu_dir)

    write_xml_file()
    return

if __name__ == "__main__":
    main()
