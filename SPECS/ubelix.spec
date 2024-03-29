# This allows overriding of the release number
%{!?_rel:%{expand:%%global _rel 1}}

Name:      ubelix-common
Version:   44.1
Release:   %{_rel}%{dist}
Summary:   Install common packages needed on all UBELIX hosts.

Group:     System Environment/Base
BuildArch: noarch
Vendor:    IT Services Office, University of Bern
Packager:  hpc-admin.id@unibe.ch
License:   Apache 2.0
URL:       https://ubelix.unibe.ch/

Requires:  at
Requires:  bash-completion
Requires:  bind-utils
Requires:  blktrace
Requires:  dstat
Requires:  htop
Requires:  iotop
Requires:  kernel-devel
Requires:  lsof
Requires:  mailx
Requires:  net-tools
Requires:  openssl-devel
Requires:  psmisc
Requires:  redhat-lsb-core
Requires:  screen
Requires:  sysstat
Requires:  telnet
Requires:  time
Requires:  vim
Requires:  wget


%description
This is a metapackage. It provides not a single file. It's mere
usefulness is to install "dependencies". This is used to install
many packages at once that are used on every (or some hosts).

%files


%package -n ubelix-sedna
Summary:   Installation of packages UBELIX users need on sedna only.

#
# Only put stuff that is present in CentOS or EPEL
#
# Editors
Requires:   gedit nedit
# Libraries
# gtk-murrine-engine is a dependency of Adobe Reader 9.x
Requires:   gtk-murrine-engine
# Perl
Requires:   cpan perl-Digest-MD5 perl-Tk perl-libwww-perl
# Qt
Requires:   qt qt-devel
# Tools
Requires:   openssh-askpass
Requires:   cvs tkcvs
Requires:   firefox mc
Requires:   ncompress gv tcl tk xterm
Requires:   plplot plplot-devel plplot-fortran-devel
Requires:   ImageMagick

%description -n ubelix-sedna
Packages this package is depending are relevant for sedna only.
Those package were previously requested by AIUB users to be present
on sedna or are needed for other functionality related to login nodes..

This is a metapackage. It provides not a single file. It's mere
usefulness is to install "dependencies". This is used to install
many packages at once that are used on every (or some hosts).

%files -n ubelix-sedna






%package -n ubelix-submit
Summary:   Installation of packages UBELIX users need on submit nodes only.

#
# Only put stuff that is present in CentOS or EPEL
#
# Shells
Requires:   xorg-x11-xauth
# Tools
Requires:   cifs-utils samba-client
Requires:   aspell aspell-en
Requires:   evince
Requires:   openssh-askpass
Requires:   ftp lftp
Requires:   tmux

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
# Editors
Requires:   emacs emacs-git emacs-php-mode emacs-yaml-mode
# Tools
Requires:   openssh-askpass
#Requires:  aspell aspell-en atlas atlas-devel
Requires:   cvs bzr git mercurial subversion
Requires:   gdl
Requires:   gnuplot
Requires:   nano
Requires:   perf
Requires:   dos2unix
Requires:   pbzip2
Requires:   xpdf
# X Window Server related
Requires:   libX11-devel
Requires:   mesa-libGLU
Requires:   xorg-x11-xauth
Requires:   xterm
# The following libs are needed by Matlab
Requires:   libXScrnSaver libXtst
# Libraries
Requires:   glibc-static
Requires:   compat-libstdc++-33
Requires:   xalan-c xerces-c
Requires:   libpng12
# Perl
Requires:   cpan perl-Digest-MD5 perl-Tk perl-libwww-perl
# Python stuff
#Requires:  python-pip
Requires:   python-devel python-setuptools
Requires:   python34-devel python34-setuptools

%description -n ubelix-userwishes
Packages this package is depending are relevant for compute nodes and
submit nodes. Those package were previously requested by UBELIX user
to be present within UBELIX.

This is a metapackage. It provides not a single file. It's mere
usefulness is to install "dependencies". This is used to install
many packages at once that are used on every (or some hosts).

%files -n ubelix-userwishes



%changelog
* Mon Oct 10 2022 Michael Rolli <michael.rolli@unibe.ch> 44-1
- Add some perl deps to submits/computes to enable out of the box texlive installation

* Fri Aug 26 2022 Matthias Salzmann <matthias.salzmann@unibe.ch> 43-2
- Add openssh-askpass on computenodes this is needed for jupyter-compute

* Wed Aug 17 2022 Michael Rolli <michael.rolli@unibe.ch> 43-1
- Add openssh-askpass on login servers and sedna as this is needed for jupyter-compute

* Fri Mar 18 2022 Michael Rolli <michael.rolli@unibe.ch> 42-2
- Addtionally add aspell-en to the submit package

* Thu Mar 17 2022 Michael Rolli <michael.rolli@unibe.ch> 42-1
- Add aspell to the submit package

* Tue Jan 25 2022 Michael Rolli <michael.rolli@unibe.ch> 41-1
- Add evince to the submit packages

* Fri May 07 2021 Michael Rolli <michael.rolli@unibe.ch> 40-1
- Add libpng12 to userwishes as it is needed by STATA

* Thu May 06 2021 Michael Rolli <michael.rolli@unibe.ch> 39-1
- Add htop globally, requested by faerber
- Add pbzip2 to user wishes, useful in case of berardi

* Thu Jan 23 2020 Michael Rolli <michael.rolli@unibe.ch> 38-1
- Add compat-libstdc++-33 to the user wishes, req by ariza

* Tue May 28 2019 Michael Rolli <michael.rolli@unibe.ch> 37-1
- Add glibc-static to the user wishes, req by user

* Tue Mar 19 2019 Michael Rolli <michael.rolli@unibe.ch> 36-1
- Add mesa-libGLU to the userwishes; req by dm18i266

* Wed Jan 16 2019 Michael Rolli <michael.rolli@unibe.ch> 35-1
- Add CVS to the userwishes

* Tue Jan 15 2019 Michael Rolli <michael.rolli@unibe.ch> 34-1
- Move some packages from submit to userwishes

* Fri Dec 14 2018 Michael Rolli <michael.rolli@unibe.ch> 33-1
- Add another library for Matlab: libXtst

* Fri Dec 14 2018 Michael Rolli <michael.rolli@unibe.ch> 32-1
- Add libXScrnSaver to userwishes as it is needed by Matlab

* Fri Nov 30 2018 Michael Rolli <michael.rolli@unibe.ch> 31-1
- Add xterm and xorg-x11-xauth to the userwishes

* Thu Nov 29 2018 Michael Rolli <michael.rolli@unibe.ch> 30-1
- Add at, redhat-lsb-core, time to the list of common packages

* Wed Nov 28 2018 Michael Rolli <michael.rolli@unibe.ch> 29-1
- Add cifs-utils and samba-clientto submit

* Tue Oct 30 2018 Michael Rolli <michael.rolli@unibe.ch> 28-1
- Add lftp to submit

* Thu Oct 11 2018 Nico Färber <nico.faerber@unibe.ch> 27-1
- Add dos2unix to ubelix-userwishes

* Tue Sep 18 2018 Michael Rolli <michael.rolli@unibe.ch> 26-1
- Add xalan-c and xerces-c to ubelix-userwishes

* Thu Sep 13 2018 Michael Rolli <michael.rolli@unibe.ch> 25-1
- Fix python34-devel

* Thu Sep 13 2018 Michael Rolli <michael.rolli@unibe.ch> 24-1
- Add python-devl, python34-devel and python34-setuptools

* Tue Sep 11 2018 Michael Rolli <michael.rolli@unibe.ch> 23-1
- Add perf t ubelix-userwishes

* Tue Aug 28 2018 Michael Rolli <michael.rolli@unibe.ch> 22-1
- Add packages tkcvs, ncompress, perl-libwww-perl, perl-Tk (sedna)
- ADd plplot, plplot-devel, plplot-fortran-devel (sedna)
- Add ftp (submit)

* Tue Aug 28 2018 Michael Rolli <michael.rolli@unibe.ch> 21-1
- Add mailx to ubelix-common

* Tue Aug 28 2018 Michael Rolli <michael.rolli@unibe.ch> 20-1
- Move gdl to ubelix-userwishes

* Tue Aug 28 2018 Michael Rolli <michael.rolli@unibe.ch> 19-1
- Add cpan to ubelix-sedna

* Tue Aug 28 2018 Michael Rolli <michael.rolli@unibe.ch> 18-1
- Add GDL to ubelix-submit

* Tue Aug 28 2018 Michael Rolli <michael.rolli@unibe.ch> 17-1
- Remove Adobe Reader dependency; add xpdf instead

* Tue Aug 28 2018 Michael Rolli <michael.rolli@unibe.ch> 16-1
- Add missing cvs to ubelix-sedna

* Tue Aug 28 2018 Michael Rolli <michael.rolli@unibe.ch> 15-1
- ubelix-sedna with user wishes from AIUB

* Tue Aug 28 2018 Michael Rolli <michael.rolli@unibe.ch> 14-1
- Add Emacs (Ticket Andrea Binardi)

* Fri Jul 13 2018 Michael Rolli <michael.rolli@unibe.ch> 13-1
- More packages

* Fri Jul 13 2018 Michael Rolli <michael.rolli@unibe.ch> 12-1
- Add editor nano

* Fri Jul 13 2018 Michael Rolli <michael.rolli@unibe.ch> 11-1
- Added python-setuptools to userwishes and globally some
  debug tools.

* Thu Jul 5 2018 Michael Rolli <michael.rolli@unibe.ch> 10-1
- Add screen to common

* Wed Jun 13 2018 Michael Rolli <michael.rolli@unibe.ch> 9-1
- Move tmux to the list for submit nodes

* Wed Jun 13 2018 Michael Rolli <michael.rolli@unibe.ch> 8-1
- Add tmux to the list of userwishes

* Fri Jun 8 2018 Michael Rolli <michael.rolli@unibe.ch> 7-1
- New metapackage ubelix-submit for submit nodes

* Fri Jun 8 2018 Michael Rolli <michael.rolli@unibe.ch> 6-1
- Add mlocate to generell tools
- Add libX11-devel to the list of userwishes

* Tue Jun 5 2018 Michael Rolli <michael.rolli@unibe.ch> 5-1
- Add tcsh to the list of userwishes

* Tue Feb 27 2018 Michael Rolli <michael.rolli@unibe.ch> 4-1
- Add package net-tools to have netstat available everywhere

* Thu Jan 11 2018 Michael Rolli <michael.rolli@unibe.ch> 3-2
- Switch to noarch packages
- Added additional metadata

* Thu Jan 11 2018 Michael Rolli <michael.rolli@unibe.ch> 3-1
- Restart with only really necessary stuff
- [user]: zsh | Matthias Lüthi (LHEP)

* Thu Jun 15 2017 Michael Rolli <michael.rolli@unibe.ch> 2-1
- Initial RPM release

