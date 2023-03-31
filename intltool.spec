Summary:	Scripts and assorted auto* magic for i18nalizing various kinds of data files
Name:		intltool
Version:	0.51.0
Release:	5
Group:		Development/GNOME and GTK+
License:	GPLv2+
Url:		http://www.gnome.org/
Source0:	http://edge.launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# Fix intltool-update to work with perl 5.26. Patch taken from
# Debian's intltool_0.51.0-4.debian.tar.xz
Patch1:		intltool-perl5.26-regex-fixes.patch
# https://bugs.launchpad.net/intltool/+bug/1505260
# https://bugzilla.redhat.com/show_bug.cgi?id=1249051
Patch2:		intltool-merge-Create-cache-file-atomically.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1318674
Patch3:		intltool_distcheck-fix.patch

BuildArch:	noarch
BuildRequires:	diffutils
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	gettext
Requires:	gettext-devel
Requires:	patch
Requires:	perl(XML::Parser)
Requires:	perl(Getopt::Long)
Requires:	automake

%description
The intltool collection can be used to:

Extract translatable strings from various source files, including
.xml.in, .glade, .desktop.in, .server.in, .oaf.in.

Collect the extracted strings together with messages from traditional
source files (such as .c, .h) into pot files.

Merge back the translations from .po files into .xml, .desktop and
.oaf files during software build time.

%prep
%autosetup -p1

%build
%configure
%make_build

%check
make check

%install
%make_install

%files
%doc AUTHORS README
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/aclocal/*
%{_mandir}/man8/*
