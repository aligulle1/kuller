MCS=gmcs
BEAGLE_LIBDIR=/usr/lib/beagle

all:
	$(MCS) -target:library FilterPisi.cs -r:ICSharpCode.SharpZipLib -r:$(BEAGLE_LIBDIR)/BeagleDaemonPlugins.dll -r:$(BEAGLE_LIBDIR)/Beagle.dll -r:$(BEAGLE_LIBDIR)/Filters/Filters.dll -r:$(BEAGLE_LIBDIR)/Util.dll

clean:
	$(RM) FilterPisi.dll

install:
	install FilterPisi.dll $(BEAGLE_LIBDIR)/Filters/FilterPisi.dll

uninstall:
	$(RM) $(BEAGLE_LIBDIR)/Filters/FilterPisi.dll
