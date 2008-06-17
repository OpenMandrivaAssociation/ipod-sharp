%define name ipod-sharp
%define version 0.8.0
%define release %mkrel 2
%if %mdkversion >= 200600
%define pkgconfigdir %_datadir/pkgconfig
%else
%define pkgconfigdir %_libdir/pkgconfig
%endif
%define monoprefix %_prefix/lib
Summary: Library to control the Ipod database
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.snorp.net/files/ipod-sharp/%name-%version.tar.gz
#Source0: http://banshee-project.org/files/ipod-sharp/%{name}-%{version}.tar.bz2
#Source0: http://banshee-project.org/files/ipod-sharp/%{name}-%{svn}.tar.bz2
License: LGPL
Group: System/Libraries
Url: http://banshee-project.org/index.php/Ipod-sharp
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: mono-tools
BuildRequires: gtk-sharp2
BuildRequires: ndesk-dbus-glib
BuildRequires: podsleuth
BuildArch: noarch
Requires: podsleuth

%description
ipod-sharp is a library that allows manipulation of the iTunesDB used
in Apple iPod devices.  Currently it supports adding/removing songs
and manipulating playlists.

%package doc
Summary: Development documentation for %name
Group: Development/Other
Requires(post): mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9

%description doc
This package contains the API documentation for the %name in
Monodoc format.


%prep
%setup -q 
#-n %name
#./autogen.sh

%build
./configure --prefix=%_prefix --libdir=%_libdir
#gw parallel build is broken
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std pkgconfigdir=%pkgconfigdir docdir=%monoprefix/monodoc/sources/
%clean
rm -rf $RPM_BUILD_ROOT

%post doc
%_bindir/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi

%files
%defattr(-,root,root)
%doc README AUTHORS NEWS
%dir %monoprefix/ipod-sharp/
%monoprefix/ipod-sharp/*.mdb
%monoprefix/ipod-sharp/ipod-sharp.dll
%monoprefix/ipod-sharp/ipod-sharp-ui.dll
%monoprefix/ipod-sharp/ipod-sharp-firmware.dll
%pkgconfigdir/*

%files doc
%defattr(-,root,root)
%monoprefix/monodoc/sources/*


