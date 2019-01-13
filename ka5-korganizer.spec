%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		korganizer
Summary:	korganizer
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	18167b026f936b62113ac467d294edfd
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
BuildRequires:	ka5-kcalcore-devel >= %{kdeappsver}
BuildRequires:	ka5-kcalutils-devel >= %{kdeappsver}
BuildRequires:	ka5-kcontacts-devel
BuildRequires:	ka5-kdepim-apps-libs-devel >= %{kdeappsver}
BuildRequires:	ka5-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	ka5-kldap-devel >= %{kdeappsver}
BuildRequires:	ka5-kmailtransport-devel >= %{kdeappsver}
BuildRequires:	ka5-kmime-devel >= %{kdeappsver}
BuildRequires:	ka5-kontactinterface-devel >= %{kdeappsver}
BuildRequires:	ka5-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka5-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.51.0
BuildRequires:	kf5-extra-cmake-modules >= 5.51.0
BuildRequires:	kf5-kcmutils-devel >= 5.51.0
BuildRequires:	kf5-kcodecs-devel >= 5.51.0
BuildRequires:	kf5-kcompletion-devel >= 5.51.0
BuildRequires:	kf5-kconfig-devel >= 5.51.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.51.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.51.0
BuildRequires:	kf5-kcrash-devel >= 5.51.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.51.0
BuildRequires:	kf5-kdoctools-devel >= 5.51.0
BuildRequires:	kf5-kholidays-devel >= 5.51.0
BuildRequires:	kf5-kiconthemes-devel >= 5.51.0
BuildRequires:	kf5-kitemviews-devel >= 5.51.0
BuildRequires:	kf5-kjobwidgets-devel >= 5.51.0
BuildRequires:	kf5-knewstuff-devel >= 5.51.0
BuildRequires:	kf5-knotifications-devel >= 5.51.0
BuildRequires:	kf5-kparts-devel >= 5.51.0
BuildRequires:	kf5-kservice-devel >= 5.51.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.51.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.51.0
BuildRequires:	kf5-kxmlgui-devel >= 5.51.0
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

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

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
/etc/xdg/autostart/org.kde.korgac.desktop
/etc/xdg/korganizer.categories
/etc/xdg/korganizer.knsrc
/etc/xdg/korganizer.renamecategories
%attr(755,root,root) %{_bindir}/korgac
%attr(755,root,root) %{_bindir}/korganizer
%attr(755,root,root) %{_libdir}/libkorganizer_core.so
%attr(755,root,root) %ghost %{_libdir}/libkorganizer_core.so.5
%attr(755,root,root) %{_libdir}/libkorganizer_core.so.5.*.*
%attr(755,root,root) %{_libdir}/libkorganizer_interfaces.so
%attr(755,root,root) %ghost %{_libdir}/libkorganizer_interfaces.so.5
%attr(755,root,root) %{_libdir}/libkorganizer_interfaces.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libkorganizerprivate.so.5
%attr(755,root,root) %{_libdir}/libkorganizerprivate.so.5.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_apptsummary.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_korganizer.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_sdsummary.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_todosummary.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kontact_journalplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kontact_korganizerplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kontact_specialdatesplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kontact_todoplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/korganizerpart.so
%{_desktopdir}/korganizer-import.desktop
%{_desktopdir}/org.kde.korganizer.desktop
%{_datadir}/config.kcfg/korganizer.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.Korganizer.Calendar.xml
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.KOrgac.xml
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
%{_iconsdir}/oxygen/16x16/actions/smallclock.png
%{_iconsdir}/oxygen/16x16/actions/upindicator.png
%{_iconsdir}/oxygen/22x22/actions/checkmark.png
%attr(755,root,root) %{_datadir}/kconf_update/korganizer-15.08-kickoff.sh
%{_datadir}/kconf_update/korganizer.upd
%{_datadir}/kontact/ksettingsdialog
%{_datadir}/korgac
%{_datadir}/korganizer
%{_datadir}/kservices5/kcmapptsummary.desktop
%{_datadir}/kservices5/kcmsdsummary.desktop
%{_datadir}/kservices5/kcmtodosummary.desktop
%{_datadir}/kservices5/kontact/journalplugin.desktop
%{_datadir}/kservices5/kontact/korganizerplugin.desktop
%{_datadir}/kservices5/kontact/specialdatesplugin.desktop
%{_datadir}/kservices5/kontact/todoplugin.desktop
%{_datadir}/kservices5/korganizer_configcolorsandfonts.desktop
%{_datadir}/kservices5/korganizer_configdesignerfields.desktop
%{_datadir}/kservices5/korganizer_configfreebusy.desktop
%{_datadir}/kservices5/korganizer_configgroupscheduling.desktop
%{_datadir}/kservices5/korganizer_configmain.desktop
%{_datadir}/kservices5/korganizer_configplugins.desktop
%{_datadir}/kservices5/korganizer_configtime.desktop
%{_datadir}/kservices5/korganizer_configviews.desktop
%{_datadir}/kservices5/korganizer_part.desktop
%{_datadir}/kservices5/webcal.protocol
%{_datadir}/kservicetypes5/dbuscalendar.desktop
%{_datadir}/metainfo/org.kde.korganizer.appdata.xml
