Summary:	Scripts and assorted auto* magic for i18nalizing various kinds of data files
Name:		intltool
Version:	0.50.2
Release:	7
Group:		Development/GNOME and GTK+
License:	GPLv2+
Url:		http://www.gnome.org/
Source0:	http://edge.launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	diffutils
BuildRequires:	perl-XML-Parser
Requires:	gettext-devel
Requires:	patch
Requires:	perl-XML-Parser
Requires:	perl

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
%doc AUTHORS README
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/aclocal/*
%{_mandir}/man8/*

