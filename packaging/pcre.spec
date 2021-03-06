%define keepstatic 1

Name: pcre
Version: 7.6
Release: 1
Summary: Perl-compatible regular expression library - Tools
URL: http://www.pcre.org/
Source: http://downloads.sourceforge.net/project/pcre/pcre/%{version}/%{name}-%{version}.tar.bz2
License: BSD
Group: System/Libraries
BuildRequires: autoconf, automake, libtool

%description
Tools and Utilities coming with %{name}


%package -n lib%{name}
Summary: Perl-compatible regular expression library
Group: System/Libraries

%description -n lib%{name}
Perl-compatible regular expression library.
PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h.


%package -n lib%{name}-devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
Development files (Headers, libraries for dynamic linking, etc) for %{name}.

%package -n lib%{name}-static
Summary: Static library for %{name}
Group: Development/Libraries
Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-static
Static library for %{name}.

%prep
%setup -q

%build

./autogen.sh --prefix=%{_prefix}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

rm -rf $RPM_BUILD_ROOT/usr/share/man
rm -rf $RPM_BUILD_ROOT/usr/share/doc

%post -n lib%{name} -p /sbin/ldconfig

%postun -n lib%{name} -p /sbin/ldconfig


%files
%{_bindir}/pcregrep
%{_bindir}/pcretest

%files -n lib%{name}
%{_libdir}/*.so.*

%files -n lib%{name}-devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*.h
%{_bindir}/pcre-config

%files -n lib%{name}-static
%{_libdir}/*.a
