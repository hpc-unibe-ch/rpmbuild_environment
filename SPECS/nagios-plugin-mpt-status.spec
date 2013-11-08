Name:	nagios-plugin-mpt-state		
Version:	1
Release:	2%{?dist}
Summary:	nagios 
Group:		Application
License:	Nagios Enterprises
URL:		www.nagios.org
Source0:	mpt-status.tar
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


%description
The check mounted disks Nagios plugin looks at the mounted partitions and compares them to what's in /etc/fstab

%prep
%setup -c -n %{name}-%{version}-%{release}.x86_64/usr/lib64/nagios/plugins/

#%build
# Nothing to compile

%install
rm -rf %{buildroot}
mkdir %{buildroot}
cp -r ../../../../usr %{buildroot}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/usr/lib64/nagios/plugins/mpt-state


%changelog
* Fri Aug 24 2012 Nina Mujkanovic <nina.mujkanovic@id.unibe.ch> - 2
- Removed mptctl.rules from rpm

* Fri Aug 10 2012 Nina Mujkanovic <nina.mujkanovic@id.unibe.ch> - 1
- Finished initial implementation

* Thu Aug 09 2012 Nina Mujkanovic <nina.mujkanovic@id.unibe.ch> - 1
- initial implementation

