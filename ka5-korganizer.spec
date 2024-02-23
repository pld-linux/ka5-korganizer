#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.01.95
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		korganizer
Summary:	korganizer
Name:		ka5-%{kaname}
Version:	24.01.95
Release:	0.1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/unstable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	83b3babac26994db9ee09bf2add5492e
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6UiTools-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
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
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcmutils-devel >= %{kframever}
BuildRequires:	kf6-kcodecs-devel >= %{kframever}
BuildRequires:	kf6-kcompletion-devel >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-kholidays-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-kitemviews-devel >= %{kframever}
BuildRequires:	kf6-kjobwidgets-devel >= %{kframever}
BuildRequires:	kf6-knewstuff-devel >= %{kframever}
BuildRequires:	kf6-knotifications-devel >= %{kframever}
BuildRequires:	kf6-kparts-devel >= %{kframever}
BuildRequires:	kf6-kservice-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	phonon-qt6-devel
BuildRequires:	qt6-build >= %{qtver}
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
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
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
%ghost %{_libdir}/libkorganizer_core.so.6
%attr(755,root,root) %{_libdir}/libkorganizer_core.so.*.*
%ghost %{_libdir}/libkorganizer_interfaces.so.6
%attr(755,root,root) %{_libdir}/libkorganizer_interfaces.so.*.*
%ghost %{_libdir}/libkorganizerprivate.so.6
%attr(755,root,root) %{_libdir}/libkorganizerprivate.so.*.*
%attr(755,root,root) %{_libdir}/qt6/plugins/korganizerpart.so
%{_desktopdir}/korganizer-import.desktop
%{_desktopdir}/org.kde.korganizer.desktop
%{_datadir}/config.kcfg/korganizer.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.Korganizer.Calendar.xml
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.Korganizer.xml
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg*
%{_datadir}/korganizer
%{_datadir}/metainfo/org.kde.korganizer.appdata.xml
%{_datadir}/knsrcfiles/korganizer.knsrc
%{_datadir}/qlogging-categories6/korganizer.categories
%{_datadir}/qlogging-categories6/korganizer.renamecategories
%{_desktopdir}/korganizer-view.desktop
%{_datadir}/dbus-1/services/org.kde.korganizer.service
%dir %{_libdir}/qt6/plugins/pim6/kcms/korganizer
%{_libdir}/qt6/plugins/pim6/kcms/korganizer/korganizer_configcolorsandfonts.so
%{_libdir}/qt6/plugins/pim6/kcms/korganizer/korganizer_configdesignerfields.so
%{_libdir}/qt6/plugins/pim6/kcms/korganizer/korganizer_configfreebusy.so
%{_libdir}/qt6/plugins/pim6/kcms/korganizer/korganizer_configgroupscheduling.so
%{_libdir}/qt6/plugins/pim6/kcms/korganizer/korganizer_configmain.so
%{_libdir}/qt6/plugins/pim6/kcms/korganizer/korganizer_configplugins.so
%{_libdir}/qt6/plugins/pim6/kcms/korganizer/korganizer_configtime.so
%{_libdir}/qt6/plugins/pim6/kcms/korganizer/korganizer_configviews.so
%{_libdir}/qt6/plugins/pim6/kcms/korganizer/korganizer_userfeedback.so
%{_libdir}/qt6/plugins/pim6/kcms/summary/kcmapptsummary.so
%{_libdir}/qt6/plugins/pim6/kcms/summary/kcmsdsummary.so
%{_libdir}/qt6/plugins/pim6/kcms/summary/kcmtodosummary.so
%{_libdir}/qt6/plugins/pim6/kontact/kontact_journalplugin.so
%{_libdir}/qt6/plugins/pim6/kontact/kontact_korganizerplugin.so
%{_libdir}/qt6/plugins/pim6/kontact/kontact_specialdatesplugin.so
%{_libdir}/qt6/plugins/pim6/kontact/kontact_todoplugin.so
