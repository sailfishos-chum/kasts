Name:           kasts
Version:        25.08.2
Release:        1%{?dist}
License:        GPLv2 and GPLv2+ and GPLv3+ and BSD and LGPLv3+
Summary:        A mobile podcast application
Url:            https://apps.kde.org/%{name}
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz
Patch0:         0001-qtrunner-desktop.patch
Patch1:         0002-add-sailfishos.patch
Source1:        kasts-86.png
Source2:        kasts-108.png
Source3:        kasts-128.png
Source4:        kasts-256.png

BuildRequires:  desktop-file-utils
BuildRequires:  cmake
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  taglib-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtkeychain-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kirigami-devel
BuildRequires:  kf6-kirigami-addons-devel
BuildRequires:  kf6-syndication-devel
BuildRequires:  kf6-threadweaver-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-kcodecs-devel
BuildRequires:  kf6-kcolorscheme-devel
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kf6-kwindowsystem-devel
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  kf6-breeze-icons-devel

Requires:       kf6-kirigami
Requires:       kf6-kirigami-addons
Requires:       kf6-threadweaver
Requires:       kf6-syndication
Requires:       kf6-kiconthemes
Requires:		kf6-kdbusaddons
Requires:		kf6-kwindowsystem
Requires:       qt6-qtkeychain
Requires:       qt-runner-qt6
Requires:	  	kf6-breeze-icons

%global __requires_exclude ^[libKMediaSession|libKastsSolidExtras].*$

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build

%cmake_kf6 -DSAILFISHOS=1
%cmake_build

%install
%cmake_install

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
%{_libdir}/libKMediaSession.so
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_qmldir}/org/kde/kmediasession/kde-qmlmodule.version
%{_kf6_qmldir}/org/kde/kmediasession/kmediasessionqmlplugin.qmltypes
%{_kf6_qmldir}/org/kde/kmediasession/libkmediasessionqmlplugin.so
%{_kf6_qmldir}/org/kde/kmediasession/qmldir
%license LICENSES/*
