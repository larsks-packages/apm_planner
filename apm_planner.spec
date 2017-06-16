%global debug_package %{nil}
%global commit0 38c5f5e28b087c8161d64f556172dd12e2ee6cc9
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: apm_planner
Version: 2.0.25
Release: 2%{?dist}.git%{shortcommit0}
Summary: ArduPilot and PX4 compatible ground station application
License: GPLv3+
URL: https://github.com/ArduPilot/apm_planner
Source0: https://github.com/ArduPilot/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{shortcommit0}.tar.gz

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qtwebkit-devel
BuildRequires: qt5-qtserialport-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtquick1-devel
BuildRequires: pyserial
BuildRequires: python-pexpect
BuildRequires: SDL-devel
BuildRequires: libsndfile-devel
BuildRequires: flite-devel
BuildRequires: openssl-devel
BuildRequires: libudev-devel
BuildRequires: SDL2-devel
BuildRequires: gcc-c++

Requires: pyserial
Requires: python-pexpect
Requires: flite

%description
APM Planner is an open-source ground station application for MAVlink based
autopilots including APM and PX4/Pixhawk.

%prep
%setup -q -n %{name}-%{commit0}

sed -i '/FLITE_AUDIO_ENABLED/ d' apm_planner.pro

%build
qmake-qt5 apm_planner.pro
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
make install INSTALL_ROOT=$RPM_BUILD_ROOT/usr

mkdir -p $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT/usr/bin/sik_uploader \
	$RPM_BUILD_ROOT%{_datadir}/sik_uploader

mv $RPM_BUILD_ROOT%{_datadir}/sik_uploader/sik_uploader.py \
	$RPM_BUILD_ROOT/usr/bin/sik_uploader

%files
%defattr(-, root, root)
%doc README.md license.txt

%{_bindir}/apmplanner2
%attr(0755, root, root) %{_bindir}/sik_uploader
%{_datadir}/APMPlanner2
%{_datadir}/sik_uploader
%{_datadir}/applications/apmplanner2.desktop
%{_datadir}/menu/apmplanner2

%changelog
* Thu Feb 04 2016 Lars Kellogg-Stedman <lars@redhat.com> - 0.21
- updated to 0.21-1fcbf09
