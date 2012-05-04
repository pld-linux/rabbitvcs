Summary:	RabbitVCS - extension for Nautilus which integrates subversion and git functionality into the GNOME Nautilus file manager
Name:		rabbitvcs
Version:	0.15.0.5
Release:	0.1
License:	GPL v2
Group:		X11/Libraries
Source0:	http://rabbitvcs.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	9bf0548557cc803ad2d88f747da1af8a
URL:		http://rabbitvcs.org/
#BuildRequires:	eel-devel >= 2.0
BuildRequires:	nautilus-devel
BuildRequires:	neon-devel
BuildRequires:	python-devel
BuildRequires:	subversion-devel
Requires:	meld
Requires:	nautilus-python >= 0.5.0
Requires:	python-pygtk-gtk >= 2.12.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RabbitVCS is a set of graphical tools written to provide simple and
straightforward access to the version control systems you use.
Currently, it is integrated into the Nautilus and Thunar file
managers, the Gedit text editor, and supports Subversion and Git, with
a goal to incorporate other version control systems as well as other
file managers.

It is primarily inspired by TortoiseSVN.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

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
