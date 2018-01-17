%define name ldaptool
%define version 0.1
%define unmangled_version 0.1
%define release 2

Summary: Tool for manipulating LDAP databases
Name: %{name}
Version: %{version}
Release: %{release}
Requires: python-ldap
Source0: %{name}-%{unmangled_version}.tar.gz
License: GNU General Public License (GPL)
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Philipp Bunge <buge@crimson.ch>
Url: http://www.ox9.org/projects/ldaptool/

%description
UNKNOWN

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Tue Oct 17 2017 Rolli, Michael (ID) <michael.rolli@id.unibe.ch> - 0.1-2
- Rebuild for CentOS 7

* Wed Nov 04 2015 Färber, Nico (ID) <nico.faerber@id.unibe.ch> - 0.1-1
- Redone for next CentOS reincarnation of UBELIX,
