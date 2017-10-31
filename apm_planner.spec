%global debug_package %{nil}
%global commit0 3f35d759afec76909da3def8c91f062e352c2489
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: apm_planner
Version: 2.0.25
Release: 3%{?dist}.git%{shortcommit0}
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

%if 0%{?fedora} < 26
BuildRequires: qt5-qtquick1-devel
%else
BuildRequires: qt5-qtquickcontrols2-devel
%endif
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

%files
%defattr(-, root, root)
%doc README.md license.txt

%{_bindir}/apmplanner2
%attr(0755, root, root) %{_bindir}/sik_uploader.py
%{_datadir}/APMPlanner2
%{_datadir}/sik_uploader
%{_datadir}/applications/apmplanner2.desktop

%changelog
* Mon Oct 30 2017 Lars Kellogg-Stedman <lars@redhat.com> - 3f35d75
- updated to 3f35d75
