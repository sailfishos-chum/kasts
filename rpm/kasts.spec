Name:           kasts
Version:        23.04.2
Release:        1%{?dist}
License:        GPLv2 and GPLv2+ and GPLv3+ and BSD and LGPLv3+
Summary:        A mobile podcast application
Url:            https://apps.kde.org/%{name}
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz
Patch0:         0001-qtrunner-desktop.patch
Source1:        kasts-86.png
Source2:        kasts-108.png
Source3:        kasts-128.png
Source4:        kasts-256.png

BuildRequires:  desktop-file-utils
BuildRequires:  cmake
BuildRequires:  opt-extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  taglib-devel
BuildRequires:  opt-qt5-qtbase-devel
BuildRequires:  qt5keychain-devel
BuildRequires:  opt-qt5-qtmultimedia-devel
BuildRequires:  opt-qt5-qtquickcontrols2-devel
BuildRequires:  opt-qt5-qtsvg-devel
BuildRequires:  opt-kf5-kconfig-devel
BuildRequires:  opt-kf5-kcoreaddons-devel
BuildRequires:  opt-kf5-ki18n-devel
BuildRequires:  opt-kf5-kirigami2-devel
BuildRequires:  opt-kf5-kirigami-addons
BuildRequires:  opt-kf5-syndication-devel
BuildRequires:  opt-kf5-threadweaver-devel
BuildRequires:  opt-kf5-rpm-macros
BuildRequires:  opt-kf5-kcodecs-devel

Requires:       opt-kf5-kirigami2
Requires:       opt-kf5-kirigami-addons
Requires:       opt-kf5-threadweaver
Requires:       opt-kf5-syndication
Requires:       qt5keychain

%global __requires_exclude ^[libKMediaSession|libKastsSolidExtras].*$
%{?opt_kf5_default_filter}

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../ \
		-DKDE_INSTALL_BINDIR:PATH=/usr/bin \
		-DCMAKE_INSTALL_PREFIX:PATH=/usr/
%make_build
popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

# copy icons
install -p -m644 -D %{SOURCE1} \
	%{buildroot}/%{_datadir}/icons/hicolor/86x86/apps/%{name}.png
install -p -m644 -D %{SOURCE2} \
	%{buildroot}/%{_datadir}/icons/hicolor/108x108/apps/%{name}.png
install -p -m644 -D %{SOURCE3} \
	%{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -p -m644 -D %{SOURCE4} \
	%{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/%{name}.png


%files
%{_bindir}/%{name}
%{_datadir}/locale/
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/icons/hicolor/scalable/actions/media-playback-cloud.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}*.svg
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_opt_kf5_libdir}/libKastsSolidExtras.so
%{_opt_kf5_libdir}/libKMediaSession.so
%{_opt_kf5_libdir}/qt5/qml/org/kde/kmediasession/libkmediasession-qmlplugin.so
%{_opt_kf5_libdir}/qt5/qml/org/kde/kmediasession/qmldir
%{_opt_kf5_metainfodir}/org.kde.%{name}.appdata.xml
%{_opt_kf5_qmldir}/org/kde/%{name}/solidextras/libkasts-solidextrasqmlplugin.so
%{_opt_kf5_qmldir}/org/kde/%{name}/solidextras/qmldir
%license LICENSES/*
