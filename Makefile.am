## Process this file with automake to produce Makefile.in.

dist_doc_DATA = \
  src/doc/pcre.txt \
  src/doc/pcre-config.txt \
  src/doc/pcregrep.txt \
  src/doc/pcretest.txt \
  AUTHORS \
  COPYING \
  ChangeLog \
  LICENCE \
  NEWS \
  README

dist_html_DATA = \
  src/doc/html/index.html \
  src/doc/html/pcre.html \
  src/doc/html/pcre-config.html \
  src/doc/html/pcre_compile.html \
  src/doc/html/pcre_compile2.html \
  src/doc/html/pcre_config.html \
  src/doc/html/pcre_copy_named_substring.html \
  src/doc/html/pcre_copy_substring.html \
  src/doc/html/pcre_dfa_exec.html \
  src/doc/html/pcre_exec.html \
  src/doc/html/pcre_free_substring.html \
  src/doc/html/pcre_free_substring_list.html \
  src/doc/html/pcre_fullinfo.html \
  src/doc/html/pcre_get_named_substring.html \
  src/doc/html/pcre_get_stringnumber.html \
  src/doc/html/pcre_get_stringtable_entries.html \
  src/doc/html/pcre_get_substring.html \
  src/doc/html/pcre_get_substring_list.html \
  src/doc/html/pcre_info.html \
  src/doc/html/pcre_maketables.html \
  src/doc/html/pcre_refcount.html \
  src/doc/html/pcre_study.html \
  src/doc/html/pcre_version.html \
  src/doc/html/pcreapi.html \
  src/doc/html/pcrebuild.html \
  src/doc/html/pcrecallout.html \
  src/doc/html/pcrecompat.html \
  src/doc/html/pcregrep.html \
  src/doc/html/pcrematching.html \
  src/doc/html/pcrepartial.html \
  src/doc/html/pcrepattern.html \
  src/doc/html/pcreperform.html \
  src/doc/html/pcreposix.html \
  src/doc/html/pcreprecompile.html \
  src/doc/html/pcresample.html \
  src/doc/html/pcrestack.html \
  src/doc/html/pcresyntax.html \
  src/doc/html/pcretest.html

pcrecpp_html = src/doc/html/pcrecpp.html
dist_noinst_DATA = $(pcrecpp_html)

if WITH_PCRE_CPP
html_DATA = $(pcrecpp_html)
endif

# The Libtool libraries to install.  We'll add to this later.
lib_LTLIBRARIES =

# Unit tests you want to run when people type 'make check'.
# TESTS is for binary unit tests, check_SCRIPTS for script-based tests
TESTS =
check_SCRIPTS =
dist_noinst_SCRIPTS =

# Some of the binaries we make are to be installed, and others are
# (non-user-visible) helper programs needed to build libpcre.
bin_PROGRAMS =
noinst_PROGRAMS =

# Additional files to delete on 'make clean' and 'make maintainer-clean'.
CLEANFILES =
MAINTAINERCLEANFILES =

# Additional files to bundle with the distribution, over and above what
# the Autotools include by default.
EXTRA_DIST =

# These files contain maintenance information
EXTRA_DIST += \
  src/doc/perltest.txt \
  NON-UNIX-USE \
  HACKING

# These files are used in the preparation of a release
EXTRA_DIST += \
  PrepareRelease \
  CleanTxt \
  Detrail \
  src/132html \
  src/doc/index.html.src

# These files are to do with building for Virtual Pascal
EXTRA_DIST += \
  makevp.bat \
  makevp_c.txt \
  makevp_l.txt \
  pcregexp.pas

# These files are usable versions of pcre.h and config.h that are distributed
# for the benefit of people who are building PCRE manually, without the
# Autotools support.
EXTRA_DIST += \
  pcre.h.generic \
  config.h.generic

pcre.h.generic: configure.ac
	rm -f $@
	cp -p pcre.h $@

MAINTAINERCLEANFILES += pcre.h.generic

# These are the header files we'll install. We do not distribute pcre.h because
# it is generated from pcre.h.in.
nodist_include_HEADERS = \
   pcre.h
include_HEADERS = \
  src/pcreposix.h

# These additional headers will be be installed if C++ support is enabled. We
# do not distribute pcrecpparg.h or pcre_stringpiece.h, as these are generated
# from corresponding .h.in files (which we do distribute).
if WITH_PCRE_CPP
nodist_include_HEADERS += \
  pcrecpparg.h \
  pcre_stringpiece.h
include_HEADERS += \
  src/pcrecpp.h \
  src/pcre_scanner.h
endif # WITH_PCRE_CPP

bin_SCRIPTS = pcre-config

## ---------------------------------------------------------------
## The dftables program is used to rebuild character tables before compiling
## PCRE, if --enable-rebuild-chartables is specified. It is not a user-visible
## program. The default (when --enable-rebuild-chartables is not specified) is
## to copy a distributed set of tables that are defined for ASCII code. In this
## case, dftables is not needed.

if WITH_REBUILD_CHARTABLES

noinst_PROGRAMS += dftables
dftables_SOURCES = dftables.c

pcre_chartables.c: dftables$(EXEEXT)
	./dftables$(EXEEXT) $@
else

pcre_chartables.c: $(srcdir)/pcre_chartables.c.dist
	rm -f $@
	$(LN_S) $(srcdir)/pcre_chartables.c.dist $@

endif # WITH_REBUILD_CHARTABLES


## The main pcre library
lib_LTLIBRARIES += libpcre.la
libpcre_la_SOURCES = \
  src/pcre_compile.c \
  src/pcre_config.c \
  src/pcre_dfa_exec.c \
  src/pcre_exec.c \
  src/pcre_fullinfo.c \
  src/pcre_get.c \
  src/pcre_globals.c \
  src/pcre_info.c \
  src/pcre_internal.h \
  src/pcre_maketables.c \
  src/pcre_newline.c \
  src/pcre_ord2utf8.c \
  src/pcre_refcount.c \
  src/pcre_study.c \
  src/pcre_tables.c \
  src/pcre_try_flipped.c \
  src/pcre_ucp_searchfuncs.c \
  src/pcre_valid_utf8.c \
  src/pcre_version.c \
  src/pcre_xclass.c \
  src/ucp.h \
  src/ucpinternal.h \
  src/ucptable.h

## This file is generated as part of the building process, so don't distribute.
nodist_libpcre_la_SOURCES = \
  pcre_chartables.c

# The pcre_printint.src file is #included by some source files, so it must be
# distributed. The pcre_chartables.c.dist file is the default version of
# pcre_chartables.c, used unless --enable-rebuild-chartables is specified.
EXTRA_DIST += pcre_printint.src pcre_chartables.c.dist

libpcre_la_LDFLAGS = $(EXTRA_LIBPCRE_LDFLAGS)

CLEANFILES += pcre_chartables.c

## A version of the main pcre library that has a posix re API.
lib_LTLIBRARIES += libpcreposix.la
libpcreposix_la_SOURCES = \
  src/pcreposix.c
libpcreposix_la_LDFLAGS = $(EXTRA_LIBPCREPOSIX_LDFLAGS)
libpcreposix_la_LIBADD = libpcre.la

## There's a C++ library as well.
if WITH_PCRE_CPP

lib_LTLIBRARIES += libpcrecpp.la
libpcrecpp_la_SOURCES = \
  src/pcrecpp_internal.h \
  src/pcrecpp.cc \
  src/pcre_scanner.cc \
  src/pcre_stringpiece.cc
libpcrecpp_la_LDFLAGS = $(EXTRA_LIBPCRECPP_LDFLAGS)
libpcrecpp_la_LIBADD = libpcre.la

TESTS += pcrecpp_unittest
noinst_PROGRAMS += pcrecpp_unittest
pcrecpp_unittest_SOURCES = src/pcrecpp_unittest.cc
pcrecpp_unittest_LDADD = libpcrecpp.la libpcre.la

TESTS += pcre_scanner_unittest
noinst_PROGRAMS += pcre_scanner_unittest
pcre_scanner_unittest_SOURCES = src/pcre_scanner_unittest.cc
pcre_scanner_unittest_LDADD = libpcrecpp.la libpcre.la

TESTS += pcre_stringpiece_unittest
noinst_PROGRAMS += pcre_stringpiece_unittest
pcre_stringpiece_unittest_SOURCES = src/pcre_stringpiece_unittest.cc
pcre_stringpiece_unittest_LDADD = libpcrecpp.la libpcre.la

endif # WITH_PCRE_CPP

## The main unit tests

# Each unit test is a binary plus a script that runs that binary in various
# ways. We install these test binaries in case folks find it helpful.

TESTS += RunTest
dist_noinst_SCRIPTS += RunTest
EXTRA_DIST += RunTest.bat
bin_PROGRAMS += pcretest
pcretest_SOURCES = src/pcretest.c
pcretest_LDADD = libpcreposix.la libpcre.la

TESTS += RunGrepTest
dist_noinst_SCRIPTS += RunGrepTest
bin_PROGRAMS += pcregrep
pcregrep_SOURCES = src/pcregrep.c
pcregrep_LDADD = libpcreposix.la libpcre.la

EXTRA_DIST += \
  src/testdata/grepinput \
  src/testdata/grepinput8 \
  src/testdata/grepinputv \
  src/testdata/grepinputx \
  src/testdata/greplist \
  src/testdata/grepoutput \
  src/testdata/grepoutput8 \
  src/testdata/grepoutputN \
  src/testdata/testinput1 \
  src/testdata/testinput2 \
  src/testdata/testinput3 \
  src/testdata/testinput4 \
  src/testdata/testinput5 \
  src/testdata/testinput6 \
  src/testdata/testinput7 \
  src/testdata/testinput8 \
  src/testdata/testinput9 \
  src/testdata/testinput10 \
  src/testdata/testoutput1 \
  src/testdata/testoutput2 \
  src/testdata/testoutput3 \
  src/testdata/testoutput4 \
  src/testdata/testoutput5 \
  src/testdata/testoutput6 \
  src/testdata/testoutput7 \
  src/testdata/testoutput8 \
  src/testdata/testoutput9 \
  src/testdata/testoutput10 \
  src/testdata/wintestinput3 \
  src/testdata/wintestoutput3 \
  src/perltest.pl

CLEANFILES += \
	testsavedregex \
	teststderr \
	testtry \
        testNinput


# PCRE demonstration program. No longer built automatcally. The point is that
# the users should build it themselves. So just distribute the source.
# noinst_PROGRAMS += pcredemo
# pcredemo_SOURCES = pcredemo.c
# pcredemo_LDADD = libpcre.la

EXTRA_DIST += src/pcredemo.c


## Utility rules, documentation, etc.

# A compatibility line, the old build system worked with 'make test'
test: check ;


# A PCRE user submitted the following addition, saying that it "will allow
# anyone using the 'mingw32' compiler to simply type 'make pcre.dll' and get a
# nice DLL for Windows use". (It is used by the pcre.dll target.)
DLL_OBJS= src/pcre_compile.o src/pcre_config.o \
	src/pcre_dfa_exec.o src/pcre_exec.o src/pcre_fullinfo.o pcre_get.o \
	src/pcre_globals.o src/pcre_info.o src/pcre_maketables.o \
	src/pcre_newline.o src/pcre_ord2utf8.o src/pcre_refcount.o \
	src/pcre_study.o src/pcre_tables.o src/pcre_try_flipped.o \
	src/pcre_ucp_searchfuncs.o src/pcre_valid_utf8.o src/pcre_version.o \
	pcre_chartables.o \
	src/pcre_xclass.o

# A PCRE user submitted the following addition, saying that it "will allow
# anyone using the 'mingw32' compiler to simply type 'make pcre.dll' and get a
# nice DLL for Windows use".
pcre.dll: $(DLL_OBJS)
	$(CC) -shared -o pcre.dll -Wl,"--strip-all" -Wl,"--export-all-symbols" $(DLL_OBJS)


# We have .pc files for pkg-config users.
pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = libpcre.pc
if WITH_PCRE_CPP
pkgconfig_DATA += libpcrecpp.pc
endif

dist_man_MANS = \
  src/doc/pcre.3 \
  src/doc/pcre-config.1 \
  src/doc/pcre_compile.3 \
  src/doc/pcre_compile2.3 \
  src/doc/pcre_config.3 \
  src/doc/pcre_copy_named_substring.3 \
  src/doc/pcre_copy_substring.3 \
  src/doc/pcre_dfa_exec.3 \
  src/doc/pcre_exec.3 \
  src/doc/pcre_free_substring.3 \
  src/doc/pcre_free_substring_list.3 \
  src/doc/pcre_fullinfo.3 \
  src/doc/pcre_get_named_substring.3 \
  src/doc/pcre_get_stringnumber.3 \
  src/doc/pcre_get_stringtable_entries.3 \
  src/doc/pcre_get_substring.3 \
  src/doc/pcre_get_substring_list.3 \
  src/doc/pcre_info.3 \
  src/doc/pcre_maketables.3 \
  src/doc/pcre_refcount.3 \
  src/doc/pcre_study.3 \
  src/doc/pcre_version.3 \
  src/doc/pcreapi.3 \
  src/doc/pcrebuild.3 \
  src/doc/pcrecallout.3 \
  src/doc/pcrecompat.3 \
  src/doc/pcregrep.1 \
  src/doc/pcrematching.3 \
  src/doc/pcrepartial.3 \
  src/doc/pcrepattern.3 \
  src/doc/pcreperform.3 \
  src/doc/pcreposix.3 \
  src/doc/pcreprecompile.3 \
  src/doc/pcresample.3 \
  src/doc/pcrestack.3 \
  src/doc/pcresyntax.3 \
  src/doc/pcretest.1

pcrecpp_man = src/doc/pcrecpp.3
EXTRA_DIST += $(pcrecpp_man)

if WITH_PCRE_CPP
man_MANS = $(pcrecpp_man)
endif

## CMake support

EXTRA_DIST += \
  cmake/COPYING-CMAKE-SCRIPTS \
  cmake/FindPackageHandleStandardArgs.cmake \
  cmake/FindReadline.cmake \
  CMakeLists.txt \
  config-cmake.h.in

## end Makefile.am
