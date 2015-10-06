Summary:	TCP Packet Sniffer
Name:		justniffer
Version:	0.5.12
Release:	0.1
Source0:	http://downloads.sourceforge.net/justniffer/%{name}_%{version}.tar.gz
# Source0-md5:	4321e69e77f21b335c9f1da228b70450
Source1:	http://github.com/tsuna/boost.m4/raw/master/build-aux/boost.m4
# Source1-md5:	ea467ff0c8d8f740e8feadc7e7a3c6fb
License:	GPL v3
Group:		Networking/Utilities
URL:		http://justniffer.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	glib2-devel
BuildRequires:	libpcap-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
justniffer is a tcp packet sniffer. It captures reassembles and
reorders TCP packets, performs IP packet defragmentation and displays
the tcp flow and trace timings. It is useful for logging network
traffic in a 'standard' (web server like) or in a customized way. It
can log http response time, useful for tracking network services
performances (e.g. web server, application server, etc.) .

Main differences from other sniffers:
- it captures tcp/ip traffic and handle all tcp/ip stuff (reordering,
  retrasmissions, defragmentation). The tcp stream adjustment is very
  reliabe since is performed using linux kernel code included in a
  slightly modified version of the nids library
- it reports timing informations. So it can be useful for tracking
  network system performances: for example http response time,
  connection time, etc.
- it can generate logs in a highly customizable way. For example can
  mimic the apache access_log

%prep
%setup -q
cp -p %{SOURCE1} m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_bindir}/justniffer
%attr(755,root,root) %{_bindir}/justniffer-grab-http-traffic
%dir %{_datadir}/justniffer
%dir %{_datadir}/justniffer/scripts
%attr(755,root,root) %{_datadir}/justniffer/scripts/*
%{_mandir}/man8/justniffer.8*
