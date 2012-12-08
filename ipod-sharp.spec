%define name ipod-sharp
%define version 0.8.5
%define release %mkrel 5
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
Source0: http://download.banshee-project.org/%name/%version/%{name}-%{version}.tar.bz2
License: LGPL
Group: System/Libraries
Url: http://banshee-project.org/index.php/Ipod-sharp
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: mono-tools
BuildRequires: gtk-sharp2-devel
BuildRequires: ndesk-dbus-glib-devel
BuildRequires: podsleuth-devel
BuildArch: noarch
Requires: podsleuth

%description
ipod-sharp is a library that allows manipulation of the iTunesDB used
in Apple iPod devices.  Currently it supports adding/removing songs
and manipulating playlists.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
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

%files devel
%defattr(-,root,root)
%pkgconfigdir/*

%files doc
%defattr(-,root,root)
%monoprefix/monodoc/sources/*




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.5-3mdv2011.0
+ Revision: 665518
- mass rebuild

  + Matthew Dawkins <mattydaw@mandriva.org>
    - corrected build requires for pkgs that have had their pkconfig split out to separate devel pkgs

* Mon Aug 09 2010 Götz Waschk <waschk@mandriva.org> 0.8.5-2mdv2011.0
+ Revision: 567901
- split out devel package

* Mon Nov 23 2009 Götz Waschk <waschk@mandriva.org> 0.8.5-1mdv2010.1
+ Revision: 469291
- update to new version 0.8.5

* Thu Oct 15 2009 Götz Waschk <waschk@mandriva.org> 0.8.3-1mdv2010.0
+ Revision: 457511
- new version 0.8.3

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.8.2-2mdv2010.0
+ Revision: 425372
- rebuild

* Wed Jan 21 2009 Götz Waschk <waschk@mandriva.org> 0.8.2-1mdv2009.1
+ Revision: 332155
- update to new version 0.8.2

* Tue Sep 23 2008 Götz Waschk <waschk@mandriva.org> 0.8.1-1mdv2009.0
+ Revision: 287515
- new version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.8.0-2mdv2009.0
+ Revision: 221637
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 21 2007 Götz Waschk <waschk@mandriva.org> 0.8.0-1mdv2008.1
+ Revision: 136202
- new version
- drop dependancy on libipoddevice
- depend on podsleuth

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 05 2007 Götz Waschk <waschk@mandriva.org> 0.6.4-1mdv2008.1
+ Revision: 105996
- new version
- filter out new automatic mono deps

* Sat May 26 2007 Götz Waschk <waschk@mandriva.org> 0.6.3-2mdv2008.0
+ Revision: 31563
- add missing dll map


* Tue Apr 03 2007 Götz Waschk <waschk@mandriva.org> 0.6.3-1mdv2007.1
+ Revision: 150278
- new version
- bump deps
- fix installation

* Sat Oct 14 2006 Götz Waschk <waschk@mandriva.org> 0.6.2-1mdv2007.1
+ Revision: 64499
- Import ipod-sharp

* Sat Oct 14 2006 Götz Waschk <waschk@mandriva.org> 0.6.2-1mdv2007.1
- split monodoc docs to separate package
- bump deps
- new version

* Thu Sep 14 2006 Götz Waschk <waschk@mandriva.org> 0.6.1-1mdv2007.0
- New version 0.6.1

* Mon Jul 24 2006 Götz Waschk <waschk@mandriva.org> 0.6.0-0.62857.2mdv2007.0
- rebuild for new mono

* Mon Jul 24 2006 Götz Waschk <waschk@mandriva.org> 0.6.0-0.62857.1mdv2007.0
- bump deps
- svn snapshot

* Wed Jul 19 2006 Götz Waschk <waschk@mandriva.org> 0.5.16-2mdv2007.0
- fix postun script

* Wed Jun 07 2006 Götz Waschk <waschk@mandriva.org> 0.5.16-1mdk
- New release 0.5.16

* Tue Feb 14 2006 Götz Waschk <waschk@mandriva.org> 0.5.15-1mdk
- New release 0.5.15

* Wed Dec 07 2005 Götz Waschk <waschk@mandriva.org> 0.5.12-1mdk
- New release 0.5.12

* Fri Nov 25 2005 Götz Waschk <waschk@mandriva.org> 0.5.11.1-1mdk
- New release 0.5.11.1

* Fri Nov 18 2005 Götz Waschk <waschk@mandriva.org> 0.5.11-1mdk
- build fix
- New release 0.5.11

* Thu Nov 10 2005 Götz Waschk <waschk@mandriva.org> 0.5.10-1mdk
- New release 0.5.10

* Mon Nov 07 2005 Götz Waschk <waschk@mandriva.org> 0.5.9-1mdk
- release version

* Mon Oct 31 2005 Götz Waschk <waschk@mandriva.org> 0.5.9-0.52406.1mdk
- new version

* Fri Oct 28 2005 Götz Waschk <waschk@mandriva.org> 0.5.8-0.52263.3mdk
- add dllmap

* Fri Oct 28 2005 Götz Waschk <waschk@mandriva.org> 0.5.8-0.52263.2mdk
- generate monodoc index

* Fri Oct 28 2005 Götz Waschk <waschk@mandriva.org> 0.5.8-0.52263.1mdk
- initial package

