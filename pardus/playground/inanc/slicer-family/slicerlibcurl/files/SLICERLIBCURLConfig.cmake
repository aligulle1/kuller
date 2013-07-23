#-----------------------------------------------------------------------------
#
# SLICERLIBCURLConfig.cmake - CMake configuration file for external projects.
#
# This file is configured by SLICERLIBCURL and used by the UseSLICERLIBCURL.cmake 
# module to load SLICERLIBCURL's settings for an external project.

SET(SLICERLIBCURL_SOURCE_DIR "/var/pisi/slicerlibcurl-7.12.1-1/work/cmcurl-r117")
SET(SLICERLIBCURL_BINARY_DIR "/var/pisi/slicerlibcurl-7.12.1-1/work/cmcurl-r117")

# The SLICERLIBCURL version number.
SET(SLICERLIBCURL_VERSION "7.12.1")

# The libraries.
SET(SLICERLIBCURL_LIBRARIES "slicerlibcurl;dl;z")

# The configuration options.
SET(SLICERLIBCURL_BUILD_SHARED_LIBS "")

# The "use" file.
SET(SLICERLIBCURL_USE_FILE "/usr/lib/slicerlibcurl-7.12.1/UseSLICERLIBCURL.cmake")

# The library directories.
SET(SLICERLIBCURL_LIBRARY_DIRS "/usr/lib/slicerlibcurl-7.12.1")

# The runtime directories.
# Note that if SLICERLIBCURL_CONFIGURATION_TYPES is set (see below) then
# these directories will be the parent directories under which there will
# be a directory of runtime binaries for each configuration type.
SET(SLICERLIBCURL_RUNTIME_DIRS "/usr/lib/slicerlibcurl-7.12.1")

# The include directories.
SET(SLICERLIBCURL_INCLUDE_DIRS "/usr/include/slicerlibcurl")

# An install tree always provides one build configuration.
# A build tree may provide either one or multiple build
# configurations depending on the CMake generator used. Since
# this project can be used either from a build tree or an install tree it
# is useful for outside projects to know the configurations available.
# If this SLICERLIBCURLConfig.cmake is in an install tree
# SLICERLIBCURL_CONFIGURATION_TYPES will be empty and SLICERLIBCURL_BUILD_TYPE
# will be set to the value of CMAKE_BUILD_TYPE used to build
# SLICERLIBCURL. If SLICERLIBCURLConfig.cmake is in a build tree
# then SLICERLIBCURL_CONFIGURATION_TYPES and SLICERLIBCURL_BUILD_TYPE will
# have values matching CMAKE_CONFIGURATION_TYPES and CMAKE_BUILD_TYPE
# for that build tree (only one will ever be set).

SET(SLICERLIBCURL_CONFIGURATION_TYPES )

SET(SLICERLIBCURL_BUILD_TYPE )
