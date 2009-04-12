Summary:	NautilusSvn - extension for Nautilus which integrates a load of Subversion functionality into the GNOME Nautilus file manager
Name:		nautilussvn
Version:	0.12
Release:	0.1
License:	GPL v2
Group:		X11/Libraries
Source0:	http://nautilussvn.googlecode.com/files/%{name}_%{version}-beta1-2.tar.gz
# Source0-md5:	1cd6f9d28bfadfe9a6455a9b0a50c9ab
URL:		http://code.google.com/p/nautilussvn/
BuildRequires:	eel-devel >= 2.0
BuildRequires:	nautilus-devel
BuildRequires:	neon-devel
BuildRequires:	python-devel
BuildRequires:	subversion-devel
Requires:	meld
Requires:	nautilus-python >= 0.4.3
Requires:	python-pygtk >= 2.12.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NautilusSvn is a Python extension for Nautilus which integrates a load
of Subversion functionality into the GNOME Nautilus file manager,
basically as a clone of the TortoiseSVN project on Windows.
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
%doc AUTHORS CREDITS MAINTAINERS README THANKS
%attr(755,root,root) %{_bindir}/nautilussvn
%{_libdir}/nautilus/extensions-2.0/python/NautilusSvn.py
%{_iconsdir}/hicolor/scalable/actions/%{name}-*.svg
%{_iconsdir}/hicolor/scalable/apps/nautilussvn.svg
%{_iconsdir}/hicolor/scalable/emblems/emblem-%{name}-*.svg
%{_datadir}/%{name}
%{py_sitescriptdir}/%{name}-%{version}*.egg-info
%{py_sitescriptdir}/%{name}
