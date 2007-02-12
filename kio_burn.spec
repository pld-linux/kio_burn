%define		_name	burn

Summary:	CD-Burning kioslave
Summary(pl.UTF-8):   Wypalanie CD za pośrednictwem kioslave
Name:		kio_burn
Version:	0.8
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www-users.york.ac.uk/~jrht100/burn/%{_name}-%{version}.tar.bz2
# Source0-md5:	28ee1c4e2c78c8bd71809ca5d1d30472
URL:		http://www-users.york.ac.uk/~jrht100/burn/
BuildRequires:	k3b-devel
BuildRequires:	kdebase-devel >= 3.3.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	taglib-devel
Requires:	cdrecord
Requires:	mkisofs
Requires:	konqueror
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Burn is a package to let you burn CD or DVDs using Konqueror.
Actually, you could in theory use it from any KDE program capable of
opening and saving via KDE's ioslave system. However, Konqueror is
probably the easiest way to burn discs.

%description -l pl.UTF-8
Burn to pakiet umożliwiający wypalanie płyt CD i DVD przy użyciu
Konquerora. Właściwie teoretycznie można go używać z dowolnego
programu KDE potrafiącego otwierać i zapisywać poprzez system KDE
ioslave. Jednak Konqueror jest prawdopodobnie najłatwiejszy w użyciu
do wypalania płytek.

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

%find_lang burn --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f burn.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/apps/konqsidebartng/*/burnsidebar.desktop
%{_datadir}/services/burn.protocol
