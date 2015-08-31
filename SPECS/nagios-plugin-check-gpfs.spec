Name:	nagios-plugin-check-gpfs
Version:	1.0.1-1
Release:	1%{?dist}
Summary:	check gpfs mount
Group:		Application
License:	GNU
URL:		exchange.nagios.org
Source0:	check_gpfs.tar
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Simple bash script for GPFS Filesystem (Global Parallel FS) checks. It will check status, inodes, mount and fill level of the fill system. 

%prep
%setup -c -n %{name}-%{version}-%{release}.x86_64/usr/lib64/nagios/plugins/

#%build 
# Nothing to compile

%install
rm -rf %{buildroot}
mkdir %{buildroot}
cp -r ../../../../usr/ %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(755,root,root,-)
/usr/lib64/nagios/plugins/check_gpfs

%changelog
* Mon Aug 31 2015 Rolli, Michael (ID) <michael.rolli@id.unibe.ch> - 1.0.1
- Removed debug output from task fill

* Fri Jun 13 2014 Nina Mujkanovic <nina.mujkanovic@id.unibe.ch> - 1.0
- Initial implementation
