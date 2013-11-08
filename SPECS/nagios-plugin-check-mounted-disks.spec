Name:	nagios-plugin-check-mounted-disks		
Version:	1
Release:	3%{?dist}
Summary:	nagios check for mounted disks
Group:		Application
License:	Nagios Enterprises
URL:		www.nagios.org
Source0:	check_mounted_disks.tar
Patch0:		check_mounted_disks_uuid.patch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


%description
The check mounted disks Nagios plugin looks at the mounted partitions and compares them to what's in /etc/fstab

%prep
%setup -c -n %{name}-%{version}-%{release}.x86_64/usr/lib64/nagios/plugins/
%patch -p 1 -P 0


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
/usr/lib64/nagios/plugins/check_mounted_disks.pl



%changelog
* Fri Sep 14 2012 David Gurtner <david.gurtner@id.unibe.ch> - 3
- Added a patch to properly read UUIDs from /etc/fstab

* Mon Aug 20 2012 Nina Mujkanovic <nina.mujkanovic@id.unibe.ch> - 2
- Changed file permission to executable

* Thu Aug 09 2012 Nina Mujkanovic <nina.mujkanovic@id.unibe.ch> - 1
- Finished initial implementation

* Fri Aug 03 2012 Nina Mujkanovic <nina.mujkanovic@id.unibe.ch> - 1
- initial implementation

