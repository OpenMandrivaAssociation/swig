%define _provides_exceptions perl(Test::\\(More\\|Builder\\))

%define with_guile 0
%{?_with_ruby: %{expand: %%global with_ruby 1}}

%define with_ocaml 0
%{?_with_ocaml: %{expand: %%global with_ocaml 1}}

%define with_mono 0
%{?_with_mono: %{expand: %%global with_mono 1}}

Name:		swig
Version:	2.0.4
Release:	%mkrel 2
Epoch:		1
Summary:	Simplified Wrapper and Interface Generator (SWIG)
License:	BSD-like
Group:		Development/Other
URL:		http://www.swig.org/
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		swig-1.3.23-pylib.patch
BuildRequires:	bison
BuildRequires:	imake
%if %{with_guile}
BuildRequires:	guile-devel
%endif
%if %{with_ocaml}
BuildRequires:	ocaml
%endif
BuildRequires:	lua-devel
%if %{with_mono}
BuildRequires:	mono
BuildRequires:	mono-devel
%endif
BuildRequires:	pcre-devel
BuildRequires:	libstdc++-devel
BuildRequires:	boost-devel
BuildRequires:	perl-devel
BuildRequires:	php-devel
BuildRequires:	python-devel
BuildRequires:	ruby-devel
BuildRequires:	tcl-devel
BuildRequires:	automake
BuildRequires:	autoconf2.5
Obsoletes:	swig-devel

%description
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.


%package	doc
Summary:	Documentation and examples for %{name}
Group:		Development/C
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	doc
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
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ANNOUNCE INSTALL CHANGES CHANGES.current LICENSE README TODO
%{_bindir}/swig
%{_bindir}/ccache-swig
%{_datadir}/swig
%{_mandir}/man1/*1*

%files doc
%defattr(-,root,root)
%doc Examples Doc/Manual
