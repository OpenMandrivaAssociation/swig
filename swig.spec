%define with_guile 0
%{?_with_ruby: %{expand: %%global with_ruby 1}}

%define with_ocaml 0
%{?_with_ocaml: %{expand: %%global with_ocaml 1}}

%define with_mono 0
%{?_with_mono: %{expand: %%global with_mono 1}}

Name:		swig
Version:	2.0.8
Release:	2
Epoch:		1
Summary:	Simplified Wrapper and Interface Generator (SWIG)
License:	BSD-like
Group:		Development/Other
URL:		http://www.swig.org/
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		swig-2.0.7-pylib.patch
Patch1:		swig203-rh706140.patch
Patch2:		swig204-rh752054.patch
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
BuildRequires:	autoconf automake libtool
Obsoletes:	swig-devel < 2.0.7

%description
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.


%package	doc
Summary:	Documentation and examples for %{name}
Group:		Development/C
Requires:	%{name} = %{EVRD}

%description	doc
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

Install the %{name}-doc package if you want to look at example and 
documentation.

%prep
%setup -q
%patch0 -p1 -b .pylib
%patch1 -p1
%patch2 -p1

%build
./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc ANNOUNCE INSTALL CHANGES CHANGES.current LICENSE README TODO
%{_bindir}/swig
%{_bindir}/ccache-swig
%{_datadir}/swig
%{_mandir}/man1/*1*

%files doc
%doc Examples Doc/Manual


%changelog
* Wed Feb 08 2012 Oden Eriksson <oeriksson@mandriva.com> 1:2.0.4-4
+ Revision: 771783
- rebuilt against libpcre.so.1 (second try)
- rebuilt against new pcre
- various cleanups

* Mon Jan 16 2012 Andrey Bondrov <abondrov@mandriva.org> 1:2.0.4-2
+ Revision: 761663
- Drop BuildRoot and no longer needed scriptlets, fix build conditions

* Fri Oct 14 2011 Leonardo Coelho <leonardoc@mandriva.org> 1:2.0.4-1
+ Revision: 704711
- bump new version

* Tue May 03 2011 Funda Wang <fwang@mandriva.org> 1:2.0.3-1
+ Revision: 663706
- new version 2.0.3

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.3.40-4mdv2011.0
+ Revision: 627727
- bump release
- don't force the usage of automake1.7

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.3.40-3mdv2011.0
+ Revision: 607760
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.3.40-2mdv2010.1
+ Revision: 520237
- rebuilt for 2010.1

* Sat Sep 26 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.3.40-1mdv2010.0
+ Revision: 449494
- update to new version 1.3.40

* Fri Aug 07 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.3.39-1mdv2010.0
+ Revision: 411506
- Update to new version 1.3.39
- Remove patch integrated upstream

* Wed Mar 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.3.38-2mdv2009.1
+ Revision: 357221
- handle co option gracefully (patch stolen from fedora)
- spec cleanup

* Sun Feb 22 2009 Emmanuel Andry <eandry@mandriva.org> 1:1.3.38-1mdv2009.1
+ Revision: 343927
- New version 1.3.38
- drop P1, no more needed
- update files list

* Wed Dec 24 2008 Funda Wang <fwang@mandriva.org> 1:1.3.36-3mdv2009.1
+ Revision: 318392
- more patch
- fix code template

* Sat Dec 06 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.3.36-2mdv2009.1
+ Revision: 311086
- buildrequires lua-devel not liblua-devel (breaks on x86-64)
- rebuild for new tcl

* Tue Aug 26 2008 Funda Wang <fwang@mandriva.org> 1:1.3.36-1mdv2009.0
+ Revision: 276099
- New version 1.3.36

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1:1.3.35-3mdv2009.0
+ Revision: 265744
- rebuild early 2009.0 package (before pixel changes)

* Wed Jun 11 2008 Helio Chissini de Castro <helio@mandriva.com> 1:1.3.35-2mdv2009.0
+ Revision: 218193
- Added switchs for mono, ocaml and guile bindings with swig. Mono and guile fails with tests
- Obsoleted wrong devel package. Swig must be the only package

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Apr 21 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:1.3.35-1mdv2009.0
+ Revision: 196249
- update to 1.3.35
- drop P1 & P2 (fixed upstream)

* Fri Jan 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.3.33-1mdv2008.1
+ Revision: 154641
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.3.31-3mdv2008.0
+ Revision: 55912
- rule out some perl provides

* Thu May 03 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:1.3.31-2mdv2008.0
+ Revision: 22054
- build with java/gcj support


* Tue Nov 28 2006 David Walluck <walluck@mandriva.org> 1.3.31-1mdv2007.0
+ Revision: 87757
- 1.3.31
- Import swig

* Thu Apr 20 2006 Jerome Martin <jmartin@mandriva.org> 1:1.3.27-3mdk
- Fixed BuildRequires for 2006.0

* Sun Apr 09 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 1:1.3.27-2mdk
- drop BuildRequires: mono - in contrib

* Thu Apr 06 2006 Helio Chissini de Castro <helio@mandriva.com> 1:1.3.27-1mdk
- Revert to 1.3.27 release. No project is ready to compile against new swig. 
Subversion bindings not compile against 1.3.28 or 1.3.29 yet.

* Sun Apr 02 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.29-1mdk
- 1.3.29
- fix deps

* Mon Mar 27 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.27-3mdk
- make it backportable

* Tue Jan 24 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.3.27-2mdk
- remove kaffe-devel from buildrequires as it's not need nor in main anymore..
- %%mkrel

* Tue Oct 18 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.3.27-1mdk
- 1.3.27

* Thu Oct 06 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.3.25-1mdk
- 1.3.25
- Fix Group

* Tue Jul 19 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.3.24-2mdk
- Rebuild

* Fri Dec 24 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.3.24-1mdk
- 1.3.24
- do libtoolize again
- drop P0 (fixed upstream)
- libraries are no more
- pick up python libdir correctly (P1 from fedora)

* Mon Dec 20 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.3.21-6mdk
- Rebuild for new perl

* Tue Jun 08 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.3.21-5mdk 
- rebuilt with gcc v3.4.x
- use macros

* Fri Apr 16 2004 Michael Scherer <misc@mandrake.org> 1.3.21-4mdk 
- moved .so to -devel, to remove useless dependencies
- split docs from main package

* Thu Jan 15 2004 Ben Reser <ben@reser.org> 1.3.21-3mdk
- Patch to fix python support on amd64.

* Wed Jan 14 2004 Ben Reser <ben@reser.org> 1.3.21-2mdk
- devel package should require the same version-release of the main
  package.

* Wed Jan 14 2004 Ben Reser <ben@reser.org> 1.3.21-1mdk
- 1.3.21
- Remove the symlink that was causing it to ship the currently installed
  binary on the build host.  The 1.3.20 version actually had the 1.3.19
  binary in it.  And as such produced code that wouldn't build against
  the headers.
- Drop the symlink to the binary in the doc dir.
- Ship CHANGES.current, ANNOUNCE, FUTURE, NEW and TODO in the doc dir.

* Sat Jan 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.3.20-1mdk
- 1.3.20

