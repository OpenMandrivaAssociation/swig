%define _provides_exceptions perl(Test::More)\\perl(Test::Builder)

Summary:        Simplified Wrapper and Interface Generator (SWIG)
Name:           swig
Version:        1.3.31
Release:        %mkrel 3
Epoch:          1
License:        BSD-like
Group:          Development/Other
URL:            http://www.swig.org/
Source0:        http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         swig-1.3.23-pylib.patch
BuildRequires:  bison
BuildRequires:  guile-devel
BuildRequires:  liblua-devel
#BuildRequires: libmono-devel
BuildRequires:  libstdc++-devel
#BuildRequires: mono
BuildRequires:  perl-devel
BuildRequires:  php
BuildRequires:  php-devel
BuildRequires:  python-devel
BuildRequires:  ruby-devel
BuildRequires:  tcl
BuildRequires:	java-gcj
%if %mdkversion >= 200610
BuildRequires:  tcl-devel
%endif
BuildRequires:  automake1.7
BuildRequires:  autoconf2.5

%description
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

%package        devel
Summary:        Header files and libraries for developing apps which will use %{name}
Group:          Development/C
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    devel
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

Install the %{name}-devel package if you want to develop applications that
will use the %{name} library.

%package        doc
Summary:        Documentation and examples for %{name}
Group:          Development/C
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    doc
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

Install the %{name}-doc package if you want to look at example and 
documentation.


%prep
%setup -q
%patch0 -p1 -b .pylib
WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force
mkdir -p Tools/config
aclocal-1.7 -I Tools/config
autoheader
automake-1.7 --add-missing --copy --force-missing
autoconf

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std install-lib install-main M4_INSTALL_DIR=%{buildroot}%{_datadir}/aclocal
install -m644 ./Source/DOH/doh.h -D %{buildroot}%{_includedir}/doh.h

# TODO: interpreters need to be fixed, etc.
%{_bindir}/find Examples -type f | %{_bindir}/xargs %{__perl} -pi -e 's/\r$//g'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc ANNOUNCE INSTALL CHANGES CHANGES.current FUTURE LICENSE NEW README TODO
%attr(0755,root,root) %{_bindir}/swig
%{_datadir}/swig

%files doc
%defattr(-,root,root,755)
%doc Examples Doc/Manual

%files devel
%defattr(0644,root,root,0755)
%doc LICENSE Doc/Devel
%{_includedir}/doh.h
