Summary:	Scripts and assorted auto* magic for i18nalizing various kinds of data files
Name:		intltool
Version:	0.50.2
Release:	2
Group:		Development/GNOME and GTK+
License:	GPLv2+
URL: 		http://www.gnome.org/
Source0:	http://edge.launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	perl-XML-Parser, diffutils
Requires:	perl-XML-Parser
Requires:	perl gettext-devel patch
%rename		xml-i18n-tools

%description
The intltool collection can be used to:

Extract translatable strings from various source files, including
.xml.in, .glade, .desktop.in, .server.in, .oaf.in.

Collect the extracted strings together with messages from traditional
source files (such as .c, .h) into pot files.

Merge back the translations from .po files into .xml, .desktop and
.oaf files during software build time.

%prep
%setup -q

%build
%configure2_5x
%make

%check
make check

%install
%makeinstall_std

%files
%doc AUTHORS COPYING README
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/aclocal/*
%{_mandir}/man8/*



%changelog
* Mon Apr 23 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.50.2-2
+ Revision: 793041
- rebuild
- cleaned up spec

* Mon Feb 27 2012 Götz Waschk <waschk@mandriva.org> 0.50.2-1
+ Revision: 781015
- new version 0.50.2

* Tue Feb 07 2012 Götz Waschk <waschk@mandriva.org> 0.50.1-1
+ Revision: 771570
- update to new version 0.50.1

* Mon Oct 10 2011 Götz Waschk <waschk@mandriva.org> 0.50.0-1
+ Revision: 704080
- update to new version 0.50.0

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.41.1-3
+ Revision: 665513
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.41.1-2mdv2011.0
+ Revision: 605976
- rebuild

* Mon Apr 19 2010 Götz Waschk <waschk@mandriva.org> 0.41.1-1mdv2010.1
+ Revision: 536621
- update to new version 0.41.1

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 0.41.0-1mdv2010.1
+ Revision: 489635
- new version
- new source URL
- update file list

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.40.6-2mdv2010.0
+ Revision: 425346
- rebuild

* Sat Mar 14 2009 Götz Waschk <waschk@mandriva.org> 0.40.6-1mdv2009.1
+ Revision: 355122
- update to new version 0.40.6

* Sat Oct 11 2008 Götz Waschk <waschk@mandriva.org> 0.40.5-1mdv2009.1
+ Revision: 291924
- new version

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 0.40.4-2mdv2009.0
+ Revision: 286469
- depend on gettext-devel (bug #44052)

* Fri Sep 19 2008 Götz Waschk <waschk@mandriva.org> 0.40.4-1mdv2009.0
+ Revision: 285998
- new version

* Sun Jul 27 2008 Funda Wang <fwang@mandriva.org> 0.40.3-1mdv2009.0
+ Revision: 250359
- New version 0.40.3

* Tue Jul 22 2008 Götz Waschk <waschk@mandriva.org> 0.40.1-1mdv2009.0
+ Revision: 239984
- new version
- update license

* Wed Jun 04 2008 Funda Wang <fwang@mandriva.org> 0.40.0-1mdv2009.0
+ Revision: 214940
- New version 0.40.0

* Mon Feb 25 2008 Götz Waschk <waschk@mandriva.org> 0.37.1-1mdv2008.1
+ Revision: 174581
- new version

* Sat Feb 09 2008 Funda Wang <fwang@mandriva.org> 0.37.0-2mdv2008.1
+ Revision: 164592
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 17 2007 Götz Waschk <waschk@mandriva.org> 0.37.0-1mdv2008.1
+ Revision: 121637
- new version

* Mon Dec 10 2007 Götz Waschk <waschk@mandriva.org> 0.36.3-1mdv2008.1
+ Revision: 116875
- new version

* Thu Nov 15 2007 Frederic Crozat <fcrozat@mandriva.com> 0.36.2-2mdv2008.1
+ Revision: 108907
- Remove old workaround for intlool-update, no longer needed

* Sun Sep 16 2007 Götz Waschk <waschk@mandriva.org> 0.36.2-1mdv2008.0
+ Revision: 88428
- new version

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 0.36.1-1mdv2008.0
+ Revision: 63175
- new version

* Fri Aug 03 2007 Götz Waschk <waschk@mandriva.org> 0.36.0-1mdv2008.0
+ Revision: 58451
- new version

* Mon Jun 04 2007 Jérôme Soyer <saispo@mandriva.org> 0.35.5-2mdv2008.0
+ Revision: 35209
- Fix intltool-extract invocation path


* Fri Feb 23 2007 Götz Waschk <waschk@mandriva.org> 0.35.5-1mdv2007.0
+ Revision: 125185
- new version

* Tue Jan 09 2007 Götz Waschk <waschk@mandriva.org> 0.35.4-1mdv2007.1
+ Revision: 106544
- new version

* Sat Jan 06 2007 Götz Waschk <waschk@mandriva.org> 0.35.3-1mdv2007.1
+ Revision: 104751
- new version
- enable checks

* Wed Dec 20 2006 Götz Waschk <waschk@mandriva.org> 0.35.2-1mdv2007.1
+ Revision: 100860
- new version

* Thu Dec 07 2006 Götz Waschk <waschk@mandriva.org> 0.35.1-1mdv2007.1
+ Revision: 91922
- Import intltool

* Thu Dec 07 2006 G�tz Waschk <waschk@mandriva.org> 0.35.1-1mdv2007.1
- drop patch
- New version 0.35.1

* Sat Jul 08 2006 Frederic Crozat <fcrozat@mandriva.com> 0.35.0-2mdv2007.0
- Patch0 (CVS): add support for quoted strings (Mdv bug #23280)

* Tue May 16 2006 Götz Waschk <waschk@mandriva.org> 0.35.0-1mdk
- New release 0.35.0

* Wed Feb 22 2006 Frederic Crozat <fcrozat@mandriva.com> 0.34.2-2mdk
- Fix build

* Mon Feb 06 2006 G�tz Waschk <waschk@mandriva.org> 0.34.2-1mdk
- bump automake dep
- New release 0.34.2
- use mkrel

* Wed Aug 03 2005 G�tz Waschk <waschk@mandriva.org> 0.34.1-1mdk
- New release 0.34.1

* Wed Jul 27 2005 G�tz Waschk <waschk@mandriva.org> 0.34-1mdk
- New release 0.34

* Mon Jan 24 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.33-1mdk
- New release 0.33

* Wed Nov 10 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.32.1-1mdk
- New release 0.32.1

* Tue Oct 19 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.31.3-1mdk
- New release 0.31.3

* Tue Aug 24 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.31.2-1mdk
- New release 0.31.2

* Thu Jul 29 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.31.1-1mdk
- New release 0.31.1

* Wed Jun 30 2004 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 0.31-2mdk
- fix buildrequires

* Sun Jun 27 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.31-1mdk
- fix build
- New release 0.31

* Sat Apr 03 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.30-1mdk
- Release 0.30
- remove patch0 (merged upstream)

