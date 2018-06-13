# This allows overriding of the release number
%{!?_rel:%{expand:%%global _rel 1}}

Name:      ubelix-common
Version:   8
Release:   %{_rel}%{dist}
Summary:   Install common packages needed on all UBELIX hosts.

Group:     System Environment/Base
BuildArch: noarch
Vendor:    IT Services Department, University of Bern
Packager:  grid-admin@id.unibe.ch
License:   Apache 2.0
URL:       https://ubelix.unibe.ch/

Requires:  bash-completion
Requires:  bind-utils
Requires:  dstat
Requires:  iotop
Requires:  kernel-devel
Requires:  net-tools
Requires:  openssl-devel
Requires:  psmisc
Requires:  vim
Requires:  wget


%description
This is a metapackage. It provides not a single file. It's mere
usefulness is to install "dependencies". This is used to install
many packages at once that are used on every (or some hosts).

%files



%package -n ubelix-submit
Summary:   Installation of packages UBELIX users need on submit nodes only.

#
# Only put stuff that is present in CentOS or EPEL
#
# Shells
Requires:   xorg-x11-xauth

%description -n ubelix-submit
Packages this package is depending are relevant for submit nodes only.
Those package were previously requested by UBELIX users to be present
on UBELIX or are needed for other functionality related to login nodes..

This is a metapackage. It provides not a single file. It's mere
usefulness is to install "dependencies". This is used to install
many packages at once that are used on every (or some hosts).

%files -n ubelix-submit





%package -n ubelix-userwishes
Summary:   Installation of packages UBELIX users requested to be present on submit/compute nodes.

#
# Only put stuff that is present in CentOS or EPEL
#
# Shells
Requires:   tcsh
Requires:   zsh
# Tools
Requires:   tmux
#Requires:  aspell aspell-en atlas atlas-devel
#Requires:  bzr git mercurial subversion
# Libraries
Requires:   libX11-devel
# Scientific software
#Requires:  boost boost-date-time boost-devel boost-filesystem boost-graph
#Requires:  boost-iostreams boost-math boost-program-options boost-python
#Requires:  boost-regex boost-serialization boost-signals boost-system
#Requires:  boost-system boost-test boost-thread boost-wave
# Python stuff
#Requires:  python-pip

%description -n ubelix-userwishes
Packages this package is depending are relevant for compute nodes and
submit nodes. Those package were previously requested by UBELIX user
to be present within UBELIX.

This is a metapackage. It provides not a single file. It's mere
usefulness is to install "dependencies". This is used to install
many packages at once that are used on every (or some hosts).

%files -n ubelix-userwishes



%changelog
* Wed Jun 13 2018 Michael Rolli <michael.rolli@id.unibe.ch> 8-1
- Add tmux to the list of userwishes

* Fri Jun 8 2018 Michael Rolli <michael.rolli@id.unibe.ch> 7-1
- New metapackage ubelix-submit for submit nodes

* Fri Jun 8 2018 Michael Rolli <michael.rolli@id.unibe.ch> 6-1
- Add mlocate to generell tools
- Add libX11-devel to the list of userwishes

* Tue Jun 5 2018 Michael Rolli <michael.rolli@id.unibe.ch> 5-1
- Add tcsh to the list of userwishes

* Tue Feb 27 2018 Michael Rolli <michael.rolli@id.unibe.ch> 4-1
- Add package net-tools to have netstat available everywhere

* Thu Jan 11 2018 Michael Rolli <michael.rolli@id.unibe.ch> 3-2
- Switch to noarch packages
- Added additional metadata

* Thu Jan 11 2018 Michael Rolli <michael.rolli@id.unibe.ch> 3-1
- Restart with only really necessary stuff
- [user]: zsh | Matthias Lüthi (LHEP)

* Thu Jun 15 2017 Michael Rolli <michael.rolli@id.unibe.ch> 2-1
- Initial RPM release

