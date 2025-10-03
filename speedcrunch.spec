Summary:	SpeedCrunch is a fast, high precision and powerful desktop calculator
Summary(hu.UTF-8):	SpeedCrunch egy gyors, nagy pontosságú és hatékony desktop-számológép
Name:		speedcrunch
Version:	0.12.0
Release:	1
License:	GPL v2
Group:		Applications/Math
Source0:	https://bitbucket.org/heldercorreia/speedcrunch/get/release-%{version}.tar.bz2?/%{name}-%{version}.tar.bz2
# Source0-md5:	f294f00d9ab8153ad4f2bebaaa93176c
URL:		http://www.speedcrunch.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Help-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.4.4
BuildRequires:	qt5-build
BuildRequires:	qt5-linguist
BuildRequires:	qt5-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SpeedCrunch is a fast, high precision and powerful desktop calculator.

%description -l hu.UTF-8
SpeedCrunch egy gyors, nagy pontosságú és hatékony desktop-számológép.

%prep
%setup -q -n heldercorreia-%{name}-ea93b21f9498

%build
mkdir -p build
cd build
%cmake ../src
sed -i "s@%{_prefix}/local@$RPM_BUILD_ROOT%{_prefix}@g" cmake_install.cmake
%{__make}
cd ../src/resources/locale
lrelease-qt5 *.ts

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/locale
cp -a src/resources/locale/*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/

for locale in ca_ES cs_CZ de_DE es_ES et_EE eu_ES fi_FI fr_FR he_IL hu_HU id_ID \
	it_IT ja_JP ko_KR lv_LV nb_NO nl_NL pl_PL pt_PT ro_RO ru_RU sv_SE tr_TR uz_Latn_UZ; do
	short=$(echo $locale | sed 's/_.*//')
	%{__mv} $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/{$locale,$short}.qm
done


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# imho the pdf-format is enough, odt is not necessary
%doc README.md
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale
%lang(ar) %{_datadir}/speedcrunch/locale/ar.qm
%lang(ca) %{_datadir}/%{name}/locale/ca.qm
%lang(cs) %{_datadir}/%{name}/locale/cs.qm
%lang(da) %{_datadir}/speedcrunch/locale/da.qm
%lang(de) %{_datadir}/%{name}/locale/de.qm
%lang(el) %{_datadir}/speedcrunch/locale/el.qm
%lang(en_GB) %{_datadir}/speedcrunch/locale/en_GB.qm
%lang(en_US) %{_datadir}/speedcrunch/locale/en_US.qm
%lang(es) %{_datadir}/%{name}/locale/es.qm
%lang(es_AR) %{_datadir}/%{name}/locale/es_AR.qm
%lang(et) %{_datadir}/speedcrunch/locale/et.qm
%lang(eu) %{_datadir}/%{name}/locale/eu.qm
%lang(fi) %{_datadir}/%{name}/locale/fi.qm
%lang(fr) %{_datadir}/%{name}/locale/fr.qm
%lang(he) %{_datadir}/%{name}/locale/he.qm
%lang(hu) %{_datadir}/speedcrunch/locale/hu.qm
%lang(id) %{_datadir}/%{name}/locale/id.qm
%lang(it) %{_datadir}/%{name}/locale/it.qm
%lang(ja) %{_datadir}/speedcrunch/locale/ja.qm
%lang(ko) %{_datadir}/speedcrunch/locale/ko.qm
%lang(lt) %{_datadir}/speedcrunch/locale/lt.qm
%lang(lv) %{_datadir}/speedcrunch/locale/lv.qm
%lang(nb) %{_datadir}/%{name}/locale/nb.qm
%lang(nl) %{_datadir}/%{name}/locale/nl.qm
%lang(pl) %{_datadir}/%{name}/locale/pl.qm
%lang(pt) %{_datadir}/%{name}/locale/pt.qm
%lang(pt_BR) %{_datadir}/%{name}/locale/pt_BR.qm
%lang(ro) %{_datadir}/%{name}/locale/ro.qm
%lang(ru) %{_datadir}/%{name}/locale/ru.qm
%lang(sk) %{_datadir}/speedcrunch/locale/sk.qm
%lang(sv) %{_datadir}/%{name}/locale/sv.qm
%lang(tr) %{_datadir}/%{name}/locale/tr.qm
%lang(uz) %{_datadir}/speedcrunch/locale/uz.qm
%lang(vi) %{_datadir}/speedcrunch/locale/vi.qm
%lang(zh_CN) %{_datadir}/%{name}/locale/zh_CN.qm
%{_datadir}/appdata/speedcrunch.appdata.xml
