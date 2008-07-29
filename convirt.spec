%define		xenversion	3.2

Summary:	A graphical Xen management tool
Summary(pl.UTF-8):	Graficzne narzędzie do zarządzania środowiskiem Xen
Name:		convirt
Version:	0.9
Release:	0.2
License:	LGPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/xenman/%{name}-%{version}.tar.gz
# Source0-md5:	5ad9e5ee1ecc5bbbe3db062edc04902e
URL:		http://xenman.sourceforge.net/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	python-paramiko
#Requires:	xen >= 3.0.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
ConVirt is a Xen management tool with a GTK+ based graphical interface
that allows for performing the standard set of domain operations
(start, stop, pause, kill, shutdown, reboot, snapshot, etc...). It
also attempts to simplify certain aspects such as the creation of
domains, as well as making the consoles available directly within the
tool's user interface.

%description -l pl.UTF-8
ConVirt to narzędzie do zarządzania środowiskiem Xen z opartym na GTK+
graficznym interfejsem pozwalającym na wykonywanie standardowego
zestawu operacji na domenach (uruchamianie, zatrzymywanie, pauzowanie,
zabijanie, wyłączanie, rebootowanie, snapshot itp.). Próbuje także
uprościć pewne aspekty, takie jak tworzenie domen, a także
udostępnianie konsoli bezpośrednio w interfejsie użytkownika.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{src,install/{client,common/scripts/xen-%{xenversion}}}
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_bindir},%{_localstatedir}/cache/%{name}}

#install -Dp $SOURCE2 %{buildroot}%{_sysconfdir}/%{name}.conf
cp -rf src $RPM_BUILD_ROOT%{_datadir}/%{name}
install install/client/ConVirt $RPM_BUILD_ROOT%{_datadir}/%{name}/install/client
install install/common/mk_image_store $RPM_BUILD_ROOT%{_datadir}/%{name}/install/common
install install/common/scripts/xen-%{xenversion}/configure-xend.sh $RPM_BUILD_ROOT%{_datadir}/%{name}/install/common/scripts/xen-%{xenversion}

cp -rf image_store $RPM_BUILD_ROOT%{_localstatedir}/cache/%{name}
cp -rf appliance_store $RPM_BUILD_ROOT%{_localstatedir}/cache/%{name}

ln -s %{_datadir}/%{name}/install/client/ConVirt $RPM_BUILD_ROOT%{_bindir}/%{name}
ln -s %{_datadir}/%{name}/install/common/mk_image_store $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
#%config %{_sysconfdir}/%{name}.conf
%config %{_localstatedir}/cache/%{name}/image_store/image_store.conf
%config %{_localstatedir}/cache/%{name}/appliance_store/catalog.conf
%dir %{_datadir}/%{name}/install
%dir %{_datadir}/%{name}/install/client
%attr(755,root,root) %{_datadir}/%{name}/install/client/ConVirt
%dir %{_datadir}/%{name}/install/common
%attr(755,root,root) %{_datadir}/%{name}/install/common/mk_image_store
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/mk_image_store
%dir %{_datadir}/%{name}/install/common/scripts/xen-%{xenversion}
%attr(755,root,root) %{_datadir}/%{name}/install/common/scripts/xen-%{xenversion}/configure-xend.sh
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/src
%dir %{_localstatedir}/cache/%{name}
%dir %{_localstatedir}/cache/%{name}/image_store
%dir %{_localstatedir}/cache/%{name}/appliance_store

#%dir %{_localstatedir}/cache/%{name}/image_store/CentOS_PV_Install
#%{_localstatedir}/cache/%{name}/image_store/CentOS_PV_Install/*
#%dir %{_localstatedir}/cache/%{name}/image_store/Windows_CD_Install
#%{_localstatedir}/cache/%{name}/image_store/Windows_CD_Install/*
#%dir %{_localstatedir}/cache/%{name}/image_store/Fedora_PV_Install
#%{_localstatedir}/cache/%{name}/image_store/Fedora_PV_Install/*
#%dir %{_localstatedir}/cache/%{name}/image_store/Linux_CD_Install
#%{_localstatedir}/cache/%{name}/image_store/Linux_CD_Install/*
#%dir %{_localstatedir}/cache/%{name}/image_store/_template_
#%{_localstatedir}/cache/%{name}/image_store/_template_/*
#dir %{_localstatedir}/cache/%{name}/image_store/common
#%{_localstatedir}/cache/%{name}/image_store/common/*
#dir %{_localstatedir}/cache/%{name}/image_store/example
#%{_localstatedir}/cache/%{name}/image_store/example/*
#dir %{_localstatedir}/cache/%{name}/appliance_store
