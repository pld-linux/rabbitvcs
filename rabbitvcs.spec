Summary:	RabbitVCS - extension for Nautilus which integrates subversion and git functionality into the GNOME Nautilus file manager
Name:		rabbitvcs
Version:	0.15.0.5
Release:	0.2
License:	GPL v2
Group:		X11/Libraries
Source0:	http://rabbitvcs.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	9bf0548557cc803ad2d88f747da1af8a
URL:		http://rabbitvcs.org/
BuildRequires:	python-devel
BuildRequires:	subversion-devel
Requires:	meld >= 1.1.2
Requires:	python-configobj >= 4.4.0
Requires:	python-dbus >= 0.80
Requires:	python-pygobject >= 2.14.1
Requires:	python-pygtk-gtk >= 2.12.1
Requires:	python-simplejson
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RabbitVCS is a set of graphical tools written to provide simple and
straightforward access to the version control systems you use.
Currently, it is integrated into the Nautilus and Thunar file
managers, the Gedit text editor, and supports Subversion and Git, with
a goal to incorporate other version control systems as well as other
file managers.

It is primarily inspired by TortoiseSVN.

%package -n nautilus-%{name}
Summary:	Nautilus extention for RabbitVCS
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 3.0
Requires:	nautilus-python >= 0.5.0
Suggests:	python-gnome-extras-gtkspell

%description -n nautilus-%{name}
Graphical frontend as Nautilus plugin

%package -n gedit-plugin-%{name}
Summary:	Gedit plugin for RabbitVCS
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gedit-plugins
Suggests:	python-gnome-extras-gtkspell

%description -n gedit-plugin-%{name}
Gedit plugin for RabbitVCS

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_datadir}/nautilus-python/extensions/
install clients/nautilus-3.0/RabbitVCS.py $RPM_BUILD_ROOT/%{_datadir}/nautilus-python/extensions/

install -d $RPM_BUILD_ROOT/%{_libdir}/gedit/plugins/
install clients/gedit/{%{name}-plugin.py,%{name}.gedit-plugin} $RPM_BUILD_ROOT/%{_libdir}/gedit/plugins/

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS README
%{_iconsdir}/hicolor/scalable/actions/%{name}-*.svg
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_iconsdir}/hicolor/scalable/apps/%{name}-small.svg
%{_iconsdir}/hicolor/scalable/emblems/emblem-%{name}-*.svg
%{_datadir}/%{name}
%{py_sitescriptdir}/%{name}-%{version}*.egg-info
%{py_sitescriptdir}/%{name}

%files -n nautilus-%{name}
%defattr(644,root,root,755)
%{_datadir}/nautilus-python/extensions/*.py

%files -n gedit-plugin-%{name}
%defattr(644,root,root,755)
%{_libdir}/gedit/plugins/%{name}-plugin.py
%{_libdir}/gedit/plugins/%{name}.gedit-plugin
