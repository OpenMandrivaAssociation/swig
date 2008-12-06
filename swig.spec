%define _provides_exceptions perl(Test::More)\\perl(Test::Builder)

%define with_guile 0
%{?_with_ruby: %{expand: %%global with_ruby 1}}

%define with_ocaml 0
%{?_with_ruby: %{expand: %%global with_ruby 1}}

%define with_mono 0
%{?_with_ruby: %{expand: %%global with_ruby 1}}

Name: swig
Version: 1.3.36
Release: %mkrel 2
Epoch: 1
Summary: Simplified Wrapper and Interface Generator (SWIG)
License: BSD-like
Group: Development/Other
URL: http://www.swig.org/
Source0: http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0: swig-1.3.23-pylib.patch
BuildRequires: bison
BuildRequires: imake
%if %{with_guile}
BuildRequires: guile-devel
%endif
%if %{with_ocaml}
BuildRequires: ocaml
%endif
BuildRequires: lua-devel
%if %{with_mono}
BuildRequires: mono
BuildRequires: mono-devel
%endif
BuildRequires: libstdc++-devel
BuildRequires: boost-devel
BuildRequires: perl-devel
BuildRequires: php-devel
BuildRequires: python-devel
BuildRequires: ruby-devel
BuildRequires: tcl-devel
BuildRequires: automake1.7
BuildRequires: autoconf2.5
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Obsoletes: swig-devel

%description
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.


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

%build
./autogen.sh

%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std 

mkdir -p %buildroot/%_docdir/swig %buildroot/%_libdir/swig
cp -a ANNOUNCE INSTALL CHANGES CHANGES.current \
	FUTURE LICENSE NEW README TODO  Doc/Devel Doc/Manual %buildroot/%_docdir/swig

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

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
