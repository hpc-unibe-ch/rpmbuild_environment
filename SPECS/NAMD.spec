Name:	NAMD	
Version:	2.9	
Release:	2
Summary:	scientific app for simulation of biomolecular systems
Group:		Application/Scientific 
License:	University of Illinois
URL:		http://www.ks.uiuc.edu/Research/namd/2.9/ug/
Source0:	NAMD_%{version}_Linux-x86_64-ibverbs.tar
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
A parallel molecular dynamics code designed for high-performance simulation of large biomolecular systems.

%prep
%setup -c -n %{name}-%{version}-%{release}.x86_64/opt/

#%build
# Nothing to compile

%install
rm -rf %{buildroot}
mkdir %{buildroot}
cp -r ../opt/ %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
/opt/NAMD_%{version}_Linux-x86_64-ibverbs

%changelog
* Thu Aug 02 2012 David Gurtner <david.gurtner@id.unibe.ch> - 2.9-2
- initial implementation finished

* Thu Jul 26 2012 Nina Mujkanovic <nina.mujkanovic@id.unib.ch> - 2.9-1
- initial implementation

