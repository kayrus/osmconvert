#
# spec file for package osmconvert
#

Name:           osmconvert
Version:        0.7U
Release:        1%{?dist}
Summary:        Convert OpenStreetMap data between different formats
License:        AGPL
Group:          Applications/GIS
Url:            http://wiki.openstreetmap.org/wiki/Osmconvert
BuildRequires:	zlib-devel
Source:         https://raw.githubusercontent.com/kayrus/osmconvert/master/osmconvert.c
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
This program reads different file formats of the OpenStreetMap project and converts the data to the selected output file format. These formats can be read: .osm .osc .osc.gz .osh .o5m .o5c .pbf
These formats can be written: .osm (default) .osc .osh .o5m .o5c .pbf 

%prep
%setup -q -c -T
cp %SOURCE0 .

%build
%__cc $RPM_OPT_FLAGS -o osmconvert osmconvert.c -lz

%install
mkdir -p ${RPM_BUILD_ROOT}%_bindir/
install -m 0755 -D osmconvert ${RPM_BUILD_ROOT}%_bindir/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%attr(0755,root,root) %_bindir/osmconvert

%changelog
* Tue Apr  1 2014 <kay.diam@gmail.com>
- Update to 0.7U
- Changed osmconvert source
* Wed May 22 2013 kukuk@suse.de
- Update to 0.7Q
  - Add subtract option
* Sat Feb 16 2013 kukuk@suse.de
- Update to 0.7P
  - changed memory layout to fix buffer overflow
* Fri Jan 11 2013 kukuk@suse.de
- Update to 0.7N
  - new add-bbox-tags option
* Fri Dec 14 2012 kukuk@suse.de
- Update to 0.7L
  - osmosis compatibility code
* Wed Dec  5 2012 kukuk@suse.de
- Update to 0.7K
  - bug fixing (dec vs. hex)
* Tue Oct 16 2012 kukuk@suse.de
- Update to 0.7g
  - use stdout for help output
  - new options
* Sat Sep 15 2012 kukuk@suse.com
- Update to 0.7c (csv support)
* Mon Jul  2 2012 kukuk@suse.de
- Fix big in creating pbf files.
  (http://forum.openstreetmap.org/viewtopic.php?id=17194 comment#12)
* Wed Feb  1 2012 kukuk@suse.de
- Update to 0.5z (small bugfixes)
* Sun Jan  8 2012 kukuk@suse.com
- Initial version
