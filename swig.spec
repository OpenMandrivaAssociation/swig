%bcond_without guile
%bcond_without mono
%bcond_without ocaml
%bcond_without php
%bcond_without ruby
%bcond_without java
%bcond_without golang
%bcond_without lua

Summary:	Simplified Wrapper and Interface Generator (SWIG)
Name:		swig
Version:	4.1.0
Release:	2
Epoch:		1
License:	BSD
Group:		Development/Other
Url:		http://www.swig.org/
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1000:	%{name}.rpmlintrc
Patch0:		swig-4.1.0-fix-push-pop-mismatch.patch
BuildRequires:	bison
BuildRequires:	imake
BuildRequires:	libtool
BuildRequires:	pkgconfig(libpcre2-posix)
%if %{with mono}
BuildRequires:	mono
BuildRequires:	pkgconfig(mono)
%endif
%if %{with ocaml}
BuildRequires:	ocaml
%endif
%if %{with golang}
BuildRequires:	golang
%endif
BuildRequires:	boost-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl-devel
%if %{with php}
BuildRequires:	php-cli
BuildRequires:	php-devel
%endif
%if %{with ruby}
BuildRequires:	ruby-devel
%endif
BuildRequires:	tcl-devel
%if %{with guile}
BuildRequires:	pkgconfig(guile-2.2)
%endif
%if %{with java}
BuildRequires:	jre-current
BuildRequires:	jdk-current
%endif
BuildRequires:	pkgconfig(libpcre)
%if %{with lua}
BuildRequires:	pkgconfig(lua)
%endif
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
%autosetup -p1

%build
./autogen.sh
%if %{with java}
. %{_sysconfdir}/profile.d/90java.sh
%endif
%configure \
	--with-boost \
	--with-tcl=%{_bindir}/tcl \
	--with-python=%{_bindir}/python2 \
	--with-2to3=%{_bindir}/2to3 \
	--with-python3=%{_bindir}/python \
	--with-perl5=%{_bindir}/perl \
%if %{with java}
	--with-java=$JAVA_HOME/bin/java \
	--with-javac=$JAVA_HOME/bin/javac \
%endif
%if %{with guile}
	--with-guile=%{_bindir}/guile \
%endif
%if %{with ocaml}
	--with-ocamlc=%{_bindir}/ocamlc \
%endif
%if %{with mono}
	--with-cil-interpreter=%{_bindir}/mono \
%endif
%if %{with lua}
	--with-lua=%{_bindir}/lua \
%endif
%if %{with golang}
	--with-go=%{_bindir}/go
%endif

%make_build

%install
%make_install
