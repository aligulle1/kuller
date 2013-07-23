find -type f | xargs sed -i -e "s:/opt/kde3:/usr/kde/3.5:g" 
find -type f | xargs sed -i -e "s:/usr/lib/qt3:/usr/qt/3:g"
find -type f | xargs sed -i -e "s:/usr/X11R6:/usr:g"
echo "  /usr/lib/pardus/**.{py,pyc,pth,so} mr," >> abstractions/python
