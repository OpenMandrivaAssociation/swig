%bcond_with guile
%bcond_with mono
%bcond_with ocaml

Summary:	Simplified Wrapper and Interface Generator (SWIG)
Name:		swig
Version:	3.0.2
Release:	2
Epoch:		1
License:	BSD
Group:		Development/Other
Url:		http://www.swig.org/
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1000:	%{name}.rpmlintrc
Patch0:		swig-3.0.0-pylib.patch
BuildRequires:	bison
BuildRequires:	imake
BuildRequires:	libtool
%if %{with mono}
BuildRequires:	mono
BuildRequires:	pkgconfig(mono)
%endif
%if %{with ocaml}
BuildRequires:	ocaml
%endif
BuildRequires:	boost-devel
BuildRequires:	libstdc++-devel
BuildRequires:	lua-devel
BuildRequires:	perl-devel
BuildRequires:	php-devel
BuildRequires:	ruby-devel
BuildRequires:	tcl-devel
%if %{with guile}
BuildRequires:	pkgconfig(guile-2.0)
%endif
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(python)
Obsoletes:	swig-devel < 2.0.7

%description
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

%files
%doc ANNOUNCE INSTALL CHANGES CHANGES.current LICENSE README TODO
%{_bindir}/swig
%{_bindir}/ccache-swig
%{_datadir}/swig
%{_mandir}/man1/*1*

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation and examples for %{name}
Group:		Development/C
Requires:	%{name} = %{EVRD}

%description doc
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

Install the %{name}-doc package if you want to look at example and 
documentation.

%files doc
%doc Examples Doc/Manual

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1 -b .pylib~

%build
./autogen.sh
%configure2_5x --with-python3=%{_bindir}/python
%make

%install
%makeinstall_std

