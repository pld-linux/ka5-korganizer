#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.12.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		korganizer
Summary:	korganizer
Name:		ka5-%{kaname}
Version:	22.12.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	eb0a91f66efc3dc9d9a05344608809dc
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5UiTools-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-calendar-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-mime-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-notes-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-search-devel >= %{kdeappsver}
BuildRequires:	ka5-calendarsupport-devel >= %{kdeappsver}
BuildRequires:	ka5-eventviews-devel >= %{kdeappsver}
BuildRequires:	ka5-incidenceeditor-devel >= %{kdeappsver}
BuildRequires:	ka5-kcalutils-devel >= %{kdeappsver}
BuildRequires:	ka5-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	ka5-kldap-devel >= %{kdeappsver}
BuildRequires:	ka5-kmailtransport-devel >= %{kdeappsver}
BuildRequires:	ka5-kmime-devel >= %{kdeappsver}
BuildRequires:	ka5-kontactinterface-devel >= %{kdeappsver}
BuildRequires:	ka5-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka5-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kcodecs-devel >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kholidays-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kitemviews-devel >= %{kframever}
BuildRequires:	kf5-kjobwidgets-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-kservice-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	phonon-qt5-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KOrganizer is an easy to use personal information manager (PIM). You
can write journal entries, schedule appointments, events, and to-dos.
KOrganizer will remind you about pending tasks, and help you keep your
schedule.

%description -l pl.UTF-8
KOrganizer jest łatwym w użyciu programem do zarządzania
informacją osobistą (PIM). Możesz dodawać wpisy do dziennika,
planować spotkania, i listę zadań do zrobienia. KOrganizer
przypomni Ci o sprawach do załatwienia i pomoże Ci trzymać się
planu.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korganizer
%{_libdir}/libkorganizer_core.so
%ghost %{_libdir}/libkorganizer_core.so.5
%attr(755,root,root) %{_libdir}/libkorganizer_core.so.*.*.*
%ghost %{_libdir}/libkorganizer_interfaces.so.5
%attr(755,root,root) %{_libdir}/libkorganizer_interfaces.so.*.*.*
%ghost %{_libdir}/libkorganizerprivate.so.5
%attr(755,root,root) %{_libdir}/libkorganizerprivate.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/korganizerpart.so
%{_desktopdir}/korganizer-import.desktop
%{_desktopdir}/org.kde.korganizer.desktop
%{_datadir}/config.kcfg/korganizer.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.Korganizer.Calendar.xml
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.Korganizer.xml
%{_iconsdir}/hicolor/128x128/apps/korg-journal.png
%{_iconsdir}/hicolor/128x128/apps/korg-todo.png
%{_iconsdir}/hicolor/128x128/apps/korganizer.png
%{_iconsdir}/hicolor/128x128/apps/quickview.png
%{_iconsdir}/hicolor/16x16/apps/korg-journal.png
%{_iconsdir}/hicolor/16x16/apps/korg-todo.png
%{_iconsdir}/hicolor/16x16/apps/korganizer.png
%{_iconsdir}/hicolor/16x16/apps/quickview.png
%{_iconsdir}/hicolor/22x22/apps/korg-journal.png
%{_iconsdir}/hicolor/22x22/apps/korg-todo.png
%{_iconsdir}/hicolor/22x22/apps/korganizer.png
%{_iconsdir}/hicolor/22x22/apps/quickview.png
%{_iconsdir}/hicolor/256x256/apps/quickview.png
%{_iconsdir}/hicolor/32x32/apps/korg-journal.png
%{_iconsdir}/hicolor/32x32/apps/korg-todo.png
%{_iconsdir}/hicolor/32x32/apps/korganizer.png
%{_iconsdir}/hicolor/32x32/apps/quickview.png
%{_iconsdir}/hicolor/48x48/apps/korg-journal.png
%{_iconsdir}/hicolor/48x48/apps/korg-todo.png
%{_iconsdir}/hicolor/48x48/apps/korganizer.png
%{_iconsdir}/hicolor/48x48/apps/quickview.png
%{_iconsdir}/hicolor/64x64/apps/korg-journal.png
%{_iconsdir}/hicolor/64x64/apps/korg-todo.png
%{_iconsdir}/hicolor/64x64/apps/korganizer.png
%{_iconsdir}/hicolor/64x64/apps/quickview.png
%{_iconsdir}/hicolor/scalable/apps/korg-journal.svgz
%{_iconsdir}/hicolor/scalable/apps/korg-todo.svg
%{_iconsdir}/hicolor/scalable/apps/korganizer.svg
%{_iconsdir}/hicolor/scalable/apps/quickview.svgz
%{_datadir}/korganizer
%{_datadir}/metainfo/org.kde.korganizer.appdata.xml
%{_datadir}/knsrcfiles/korganizer.knsrc
%{_datadir}/qlogging-categories5/korganizer.categories
%{_datadir}/qlogging-categories5/korganizer.renamecategories
%{_desktopdir}/korganizer-view.desktop
%{_datadir}/dbus-1/services/org.kde.korganizer.service
%dir %{_libdir}/qt5/plugins/pim5/kcms/korganizer
%{_libdir}/qt5/plugins/pim5/kcms/korganizer/korganizer_configcolorsandfonts.so
%{_libdir}/qt5/plugins/pim5/kcms/korganizer/korganizer_configdesignerfields.so
%{_libdir}/qt5/plugins/pim5/kcms/korganizer/korganizer_configfreebusy.so
%{_libdir}/qt5/plugins/pim5/kcms/korganizer/korganizer_configgroupscheduling.so
%{_libdir}/qt5/plugins/pim5/kcms/korganizer/korganizer_configmain.so
%{_libdir}/qt5/plugins/pim5/kcms/korganizer/korganizer_configplugins.so
%{_libdir}/qt5/plugins/pim5/kcms/korganizer/korganizer_configtime.so
%{_libdir}/qt5/plugins/pim5/kcms/korganizer/korganizer_configviews.so
%{_libdir}/qt5/plugins/pim5/kcms/korganizer/korganizer_userfeedback.so
%{_libdir}/qt5/plugins/pim5/kcms/summary/kcmapptsummary.so
%{_libdir}/qt5/plugins/pim5/kcms/summary/kcmsdsummary.so
%{_libdir}/qt5/plugins/pim5/kcms/summary/kcmtodosummary.so
%{_libdir}/qt5/plugins/pim5/kontact/kontact_journalplugin.so
%{_libdir}/qt5/plugins/pim5/kontact/kontact_korganizerplugin.so
%{_libdir}/qt5/plugins/pim5/kontact/kontact_specialdatesplugin.so
%{_libdir}/qt5/plugins/pim5/kontact/kontact_todoplugin.so
