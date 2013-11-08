# Don't try fancy stuff like debuginfo, which is useless on binary-only
# packages. Don't strip binary too
# Be sure buildpolicy set to do nothing
%define         __spec_install_post %{nil}
%define         debug_package %{nil}
%define         __os_install_post %{_dbpath}/brp-compress

Name:		NAMD-ibverbs
Version:	2.9	
Release:	3
Summary:	scientific app for simulation of biomolecular systems
Group:		Application/Scientific 
License:	University of Illinois
URL:		http://www.ks.uiuc.edu/Research/namd/2.9/ug/
Source0:	/gpfs/software/packages/NAMD/NAMD_%{version}_Linux-x86_64-ibverbs.tar.gz
#Source1:	/gpfs/software/packages/NAMD/NAMD_modulefile

%description
A parallel molecular dynamics code designed for high-performance simulation of large biomolecular systems.

%prep
%setup -c -n %{name}-%{version}-%{release}.x86_64

#%build
# Nothing to compile as it's already a binary package

%install
export MODULE_FILE=/etc/modulefiles/NAMD/%{version}-ibverbs
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/modulefiles/NAMD
mkdir -p %{buildroot}/opt
cp -r ./ %{buildroot}/opt
#mv %{buildroot}/opt/NAMD_modulefile.tmpl $MODULE_FILE

cat <<"EOD" > %{buildroot}/$MODULE_FILE
#%Module1.0#####################################################################
##
## {{name}} modulefile
##

set ModulesVersion      "{{version}}"

proc ModulesHelp { } {
  global version prefix

  puts stderr "\t{{name}}-{{version}}"
  puts stderr "\n\tThis adds $prefix to several of the"
  puts stderr "\tenvironment variables."
  puts stderr "\n\tVersion $version\n"
}

module-whatis   "Loads {{name}}-{{version}}"

conflict        {{conflict}}

# for Tcl script use only
set             prefix          {{destination}}

prepend-path    PATH            ${prefix}
prepend-path    LIBRARY_PATH    ${prefix}/lib
prepend-path    LD_LIBRARY_PATH ${prefix}/lib
EOD

export DESTINATION="\/opt\/NAMD_%{version}_Linux-x86_64-ibverbs"
sed -i -e "s/{{name}}/%{name}/g" -e "s/{{version}}/%{version}/g" \
       -e "s/{{destination}}/${DESTINATION}/g" -e "s/{{conflict}}/NAMD/g" %{buildroot}/$MODULE_FILE

%clean
rm -rf %{_builddir}/%{name}-%{version}-%{release}.x86_64
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
/etc/modulefiles/NAMD/%{version}-ibverbs
/opt/NAMD_%{version}_Linux-x86_64-ibverbs

%changelog
* Fri Nov 08 2013 Michael Rolli <michael.rolli@id.unibe.ch> - 2.9-4
- Added the environment modulefile to the build process

* Tue Nov 05 2013 Michael Rolli <michael.rolli@id.unibe.ch> - 2.9-3
- Rebuild for testing

* Thu Aug 02 2012 David Gurtner <david.gurtner@id.unibe.ch> - 2.9-2
- initial implementation finished

* Thu Jul 26 2012 Nina Mujkanovic <nina.mujkanovic@id.unib.ch> - 2.9-1
- initial implementation

