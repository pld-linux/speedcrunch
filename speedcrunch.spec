Summary:	SpeedCrunch is a fast, high precision and powerful desktop calculator
Summary(hu.UTF-8):	SpeedCrunch egy gyors, nagy pontosságú és hatékony desktop-számológép.
Name:		speedcrunch
Version:	0.10.1
Release:	1
License:	GPL v2
Group:		Applications/Math
Source0:	http://speedcrunch.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	344ee1303b05502d28c58a2fff1ca6b2
URL:		http://www.speedcrunch.org
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	cmake >=2.4.4
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SpeedCrunch is a fast, high precision and powerful desktop calculator

%description -l hu.UTF-8
SpeedCrunch egy gyors, nagy pontosságú és hatékony desktop-számológép.

%prep
%setup -q

%build
mkdir build
cd build
cmake ../src
sed -i "s@%{_prefix}/local@$RPM_BUILD_ROOT%{_prefix}@g" cmake_install.cmake
%{__make}
cd ../src/i18n
lrelease-qt4 *.ts

%install
rm -rf $RPM_BUILD_ROOT
cd build
%{__make} install
# imho this is useless
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/books

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# imho the pdf-format is enough, odt is not necessary
%doc ChangeLog ChangeLog.floatnum HACKING.txt INSTALL.txt PACKAGERS README TRANSLATORS doc/speedcrunch-manual.pdf doc/logic-unit.pdf
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale
%{_pixmapsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop
%attr(755,root,root) %{_bindir}/%{name}
%lang(ca) %{_datadir}/%{name}/locale/ca.qm
%lang(cs) %{_datadir}/%{name}/locale/cs.qm
%lang(de) %{_datadir}/%{name}/locale/de.qm
%lang(es_AR) %{_datadir}/%{name}/locale/es_AR.qm
%lang(es) %{_datadir}/%{name}/locale/es.qm
%lang(eu) %{_datadir}/%{name}/locale/eu.qm
%lang(fi) %{_datadir}/%{name}/locale/fi.qm
%lang(fr) %{_datadir}/%{name}/locale/fr.qm
%lang(he) %{_datadir}/%{name}/locale/he.qm
%lang(id) %{_datadir}/%{name}/locale/id.qm
%lang(it) %{_datadir}/%{name}/locale/it.qm
%lang(nb) %{_datadir}/%{name}/locale/nb.qm
%lang(nl) %{_datadir}/%{name}/locale/nl.qm
%lang(pl) %{_datadir}/%{name}/locale/pl.qm
%lang(pt_BR) %{_datadir}/%{name}/locale/pt_BR.qm
%lang(pt) %{_datadir}/%{name}/locale/pt.qm
%lang(ro) %{_datadir}/%{name}/locale/ro.qm
%lang(ru) %{_datadir}/%{name}/locale/ru.qm
%lang(sv) %{_datadir}/%{name}/locale/sv.qm
%lang(tr) %{_datadir}/%{name}/locale/tr.qm
%lang(zh_CN) %{_datadir}/%{name}/locale/zh_CN.qm
