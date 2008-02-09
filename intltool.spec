Summary:	Scripts and assorted auto* magic for i18nalizing various kinds of data files
Name:		intltool
Version: 0.37.0
Release: %mkrel 2
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
License:	GPL
URL: 		http://www.gnome.org/
Group:		Development/GNOME and GTK+
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	perl-XML-Parser
Requires:	perl gettext patch
BuildRequires:	perl-XML-Parser
Obsoletes:	xml-i18n-tools
Provides:	xml-i18n-tools = %{version}-%{release}
BuildArch:	noarch

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
rm -rf $RPM_BUILD_ROOT

%{makeinstall_std}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/aclocal/*
%{_mandir}/man8/*


