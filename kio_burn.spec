#
# Conditional build:
%bcond_without	k3b		# without k3b to detect devices
#
%define		_name	burn
#
Summary:	CD-Burning kioslave
Summary(pl):	Wypalanie CD za po¶rednictwem kioslave
Name:		kio_burn
Version:	0.7
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www-users.york.ac.uk/~jrht100/burn/%{_name}-%{version}.tar.bz2
# Source0-md5:	20223fbcfc9ab67767c0ad55359d1f75
URL:		http://www-users.york.ac.uk/~jrht100/burn/
BuildRequires:	audiofile-devel
%{?with_k3b:BuildRequires:	k3b-devel}
BuildRequires:	kdelibs-devel >= 3.3.2
BuildRequires:	kdemultimedia-akode
BuildRequires:	kdemultimedia-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	taglib-devel
Requires:	cdrtools
Requires:	cdrtools-mkisofs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Burn is a package to let you burn CD or DVDs using Konqueror.
Actually, you could in theory use it from any KDE program capable of
opening and saving via KDE's ioslave system. However, Konqueror is
probably the easiest way to burn discs.

%description -l pl
Burn to pakiet umo¿liwiaj±cy wypalanie p³yt CD i DVD przy u¿yciu
Konquerora. W³a¶ciwie teoretycznie mo¿na go u¿ywaæ z dowolnego
programu KDE potrafi±cego otwieraæ i zapisywaæ poprzez system KDE
ioslave. Jednak Konqueror jest prawdopodobnie naj³atwiejszy w u¿yciu
do wypalania p³ytek.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/kde3/kio_burn.so
%{_libdir}/kde3/kio_burn.la
%{_datadir}/services/burn.protocol
%{_datadir}/apps/kio_burn
%{_datadir}/apps/konqueror/kpartplugins/kio_burn.rc
%{_datadir}/apps/konqsidebartng/virtual_folders/services/burn.desktop
