%global username sgeadmin
%global homedir %{_datadir}/gridengine
%global gecos Grid Engine
%global _hardened_build 1

# gridengine uses a versioned binary protocol to communicate between the master
# and the nodes that needs to be the same on all machines in a cluster.  This
# version is defined by GRM_GDI_VERSION in: libs/gdi/version.c 
# No updates should be pushed that bump this version in a stable release.

Name:    gridengine
Version: 2011.11p1
Release: 23%{?dist}
Summary: Grid Engine - Distributed Computing Management software

Group:   Applications/System
# Only the file %{_libexecdir}/gridengine/bin/*/qmake is
# under GPLv2+, which is not used or linked by other parts
# of gridengine.
# The file %{_libexecdir}/gridengine/bin/*/qtcsh is
# under BSD with advertising, 
# which is not used or linked by other parts of gridengine.
License: (BSD and LGPLv2+ and MIT and SISSL) and GPLv2+ and BSD with advertising
URL:     http://gridscheduler.sourceforge.net/
Source0: http://downloads.sourceforge.net/gridscheduler/GE%{version}/GE%{version}.tar.gz
Source1: gridengine-ppc.tar.gz
Source2: conf_defaults
Source3: sge.csh
Source4: sge.sh
%if 0%{?fedora} >= 15
Source5: sge_execd.service
Source6: sgemaster.service
Source13: sge_shadowd.service
%else
Source5: sge_execd
Source6: sgemaster
%endif
Source7: bootstrap
Source8: Licenses
Source9: gridengine.sysconfig
Source10: libcore.c
Source11: README
Source12: maketarball
# Make loadsensor reports fresh
Patch0: gridengine-loadsensor.patch
# Add LDFLAGS to LFLAGS used by aimk
Patch1: gridengine-ldflags.patch
# Fix format-security errors
# https://bugzilla.redhat.com/show_bug.cgi?id=1037103
Patch2: gridengine-format.patch
# Try to support arm architecture
Patch4: gridengine-arm.patch
# Don't need to make rc files in inst_common.sh
# Partially http://gridengine.sunsource.net/issues/show_bug.cgi?id=2780
Patch10: gridengine-rctemplates.patch
# Fixup sge_ca to use system openssl and java paths
Patch11: gridengine-6.2u2_1-sge_ca.patch
# Fixup jni paths
Patch12: gridengine-6.2-jni.patch
# Don't use rpaths
Patch13: gridengine-rpath.patch
# Fix issue with hostnames and localhost
Patch14: gridengine-6.2u5-gethostname.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch: ppc64

BuildRequires: /bin/csh, openssl-devel, db4-devel, ncurses-devel, pam-devel
BuildRequires: libXmu-devel, libXpm-devel
%if 0%{?rhel}
BuildRequires: openmotif-devel
%else
BuildRequires: lesstif-devel
%endif
BuildRequires: java-devel >= 1.6.0, javacc, ant-junit
%if 0%{?rhel}
BuildRequires: ant-nodeps
%endif
BuildRequires: elfutils-libelf-devel, net-tools
BuildRequires: groff
%if 0%{?fedora}
BuildRequires: hostname
%endif
BuildRequires: hwloc-devel
BuildRequires: jemalloc-devel
%if 0%{?fedora}
%if 0%{?fedora} >= 18
BuildRequires: systemd-units
%else
BuildRequires: systemd
%endif
%endif
Requires: binutils
Requires: ncurses
Requires(posttrans): /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives
Requires(pre): shadow-utils


%description
In a typical network that does not have distributed resource management
software, workstations and servers are used from 5% to 20% of the time.
Even technical servers are generally less than fully utilized. This
means that there are a lot of cycles that can be used productively if
only users know where they are, can capture them, and put them to work.

Grid Engine finds a pool of idle resources and harnesses it
productively, so an organization gets as much as five to ten times the
usable power out of systems on the network. That can increase utilization
to as much as 98%.

Grid Engine software aggregates available compute resources and
delivers compute power as a network service.

These are the local files shared by both the qmaster and execd
daemons. You must install this package in order to use any one of them.


%package devel
Summary: Gridengine development files
Group: Development/Libraries
License: BSD and LGPLv2+ and MIT and SISSL
Requires: %{name} = %{version}-%{release}

%description devel
gridengine development headers and libraries.


%package qmon
Summary: Gridengine qmon monitor
Group: Development/Libraries
License: BSD and LGPLv2+ and MIT and SISSL
Requires: %{name} = %{version}-%{release}
Requires: xorg-x11-fonts-ISO8859-1-100dpi xorg-x11-fonts-ISO8859-1-75dpi

%description qmon
The qmon graphical grid engine monitor


%package execd
Summary: Gridengine execd program
Group: Development/Libraries
License: BSD and LGPLv2+ and MIT and SISSL
Requires: %{name} = %{version}-%{release}
%if 0%{?fedora}
%if 0%{?fedora} >= 18
Requires(post): systemd
Requires(postun): systemd
Requires(preun): systemd
%else
Requires(post): systemd-units
Requires(post): systemd-sysv
Requires(postun): systemd-units
Requires(preun): systemd-units
%endif
%else
Requires(post): /sbin/chkconfig
Requires(postun): /sbin/service
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service
%endif
Requires(postun): %{name} = %{version}-%{release}
Requires(preun): %{name} = %{version}-%{release}

%description execd
Programs needed to run a grid engine execution host


%package qmaster
Summary: Gridengine qmaster programs
Group: Development/Libraries
License: BSD and LGPLv2+ and MIT and SISSL
Requires: %{name} = %{version}-%{release}
Requires: db4-utils
%if 0%{?fedora}
%if 0%{?fedora} >= 18
Requires(post): systemd
Requires(postun): systemd
Requires(preun): systemd
%else
Requires(post): systemd-units
Requires(post): systemd-sysv
Requires(postun): systemd-units
Requires(preun): systemd-units
%endif
%else
Requires(post): /sbin/chkconfig
Requires(postun): /sbin/service
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service
%endif
Requires(postun): %{name} = %{version}-%{release}
Requires(preun): %{name} = %{version}-%{release}

%description qmaster
Programs needed to run a grid engine qmaster or shadowd host


%prep
%setup -q -n GE%{version} -a 1
#Use system hwloc and jemalloc
rm -r source/3rdparty/hwloc
rm -r source/3rdparty/jemalloc
#Copy Licenses and README file into build directory
cp %SOURCE8 %SOURCE11 .
#Remove unneeded shbangs
sed -i -e '/^#! *\/bin\/sh/d' source/dist/util/install_modules/*.sh
%patch0 -p0 -b .loadsensor
%patch1 -p1 -b .ldflags
%patch2 -p1 -b .format
%patch4 -p1 -b .arm
%patch10 -p1 -b .rctemplates
%patch11 -p1 -b .sge_ca
%patch12 -p1 -b .jni
%patch13 -p1 -b .rpath
%patch14 -p1 -b .gethostname
sed -i.arch -e 's,/\$DSTARCH,,g' source/scripts/distinst
#Don't ship rctemplates
rm -rf source/dist/util/rctemplates
#Don't ship windows .bat scripts
find source -name \*.bat | xargs rm
#Fix permissions
chmod +x source/dist/util/dl?.*sh 
chmod -x source/dist/util/dl.*sh 
find source -name \*.c | xargs chmod -x
#Fix flags for qmake build
find source/3rdparty/qmake source/3rdparty/qtcsh -name Makefile | 
  xargs sed -i -e "/^CFLAGS *=/s:=:= $RPM_OPT_FLAGS:"
#dlopen the runtime libssl library
soname=$(objdump -p %{_libdir}/libssl.so | awk '/SONAME/ {print $2}')
sed -i -e s/libssl\.so/$soname/ source/libs/comm/cl_ssl_framework.c
#Fix xterm path
sed -i -e s,X11/xterm,xterm,g doc/htmlman/htmlman5/sge_conf.html \
                              doc/man/man5/sge_conf.5 \
                              source/dist/util/arch_variables \
                              source/libs/sgeobj/sge_conf.c


%build
export JAVA_HOME=%{java_home}
cd source
#Setup paths
cat > aimk.private <<EOF
set OPENSSL_HOME = /usr
set BERKELEYDB_HOME = /usr
%if 0%{?fedora} >= 18
set BDB_INCLUDE_SUBDIR = libdb4
set BDB_LIB_SUBDIR = ../%{_lib}/libdb4
%else
set BDB_INCLUDE_SUBDIR =
set BDB_LIB_SUBDIR = ../%{_lib}
%endif
set KRB_HOME = /usr
set MAN2HTMLPATH = /usr/bin
set GROFFPATH = /usr/bin
set SWIG = /usr/bin/swig
set PERL = /usr/bin/perl
set TCLSH = /usr/bin/tclsh
set JUNIT_JAR = /usr/share/java/junit.jar
set CORE_HOME = `pwd`
EOF
cat > build_private.properties <<EOF
javacc.home=%{_javadir}
default.sge.javac.source=1.5
default.sge.javac.target=1.5
libs.junit.classpath=%{_javadir}/junit.jar
izpack.lib=/usr/share/java/izpack
hadoop.javac.source=1.6
hadoop.javac.target=1.6
hadoop.home=/usr/share/java
EOF

#Build libcore.so
gcc $RPM_OPT_FLAGS -D_GNU_SOURCE -fPIC -c %SOURCE10 -o libcore.o
gcc $RPM_LD_FLAGS -shared -o libcore.so libcore.o -lpthread
export SGE_INPUT_CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="$RPM_LD_FLAGS"
touch aimk
./aimk -only-depend
scripts/zerodepend
./aimk -sys-hwloc -sys-jemalloc -sys-libssl depend
#TODO - Need IzPack for GUI Installer
./aimk -no-gui-inst -sys-hwloc -sys-jemalloc -sys-libssl
./aimk -man -sunman
#Not build by default - going to need hadoop
#ant herd


%install 
rm -rf $RPM_BUILD_ROOT

#Set the gridengine arch
gearch=`%{_builddir}/%{buildsubdir}/source/dist/util/arch`
# set up the target installation directory
export SGE_ROOT=$RPM_BUILD_ROOT%{_datadir}/gridengine
mkdir -p $SGE_ROOT
cd source
echo 'y'| scripts/distinst -nobdb -noopenssl -local -allall -noexit -mansrc sge ${gearch}

#Create default install configuration
cp dist/util/install_modules/inst_template.conf \
   $RPM_BUILD_ROOT%{_datadir}/gridengine/my_configuration.conf
cat %SOURCE2 | while read line
do
  key=${line/=*/}
  value=${line/*=/}
  sed -i -e "/^${key}=/s,=.*,=$value," $RPM_BUILD_ROOT%{_datadir}/gridengine/my_configuration.conf
done

install -p -m755 `scripts/compilearch -b`/qevent $RPM_BUILD_ROOT%{_datadir}/gridengine/bin

# man - do before the alternatives rename below
mkdir -p $RPM_BUILD_ROOT%{_mandir}
mv $RPM_BUILD_ROOT%{_datadir}/gridengine/man/man* $RPM_BUILD_ROOT%{_mandir}

# Move things to the right location, making links back
# bin
mv $RPM_BUILD_ROOT%{_datadir}/gridengine/bin $RPM_BUILD_ROOT%{_prefix}
rmdir $RPM_BUILD_ROOT%{_bindir}/${gearch}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gridengine/bin/${gearch}
# Rename common queuing binaries and manpages for use with alternatives
for bin in qalter qdel qhold qmake qrls qselect qstat qsub
do
    if [ -L $RPM_BUILD_ROOT%{_bindir}/$bin ]
    then
        target=`readlink $RPM_BUILD_ROOT%{_bindir}/$bin`
        rm $RPM_BUILD_ROOT%{_bindir}/$bin
        ln -s ${target}-ge $RPM_BUILD_ROOT%{_bindir}/${bin}-ge
    else
        mv $RPM_BUILD_ROOT%{_bindir}/$bin $RPM_BUILD_ROOT%{_bindir}/${bin}-ge
    fi
    mv $RPM_BUILD_ROOT%{_mandir}/man1/${bin}.1 $RPM_BUILD_ROOT%{_mandir}/man1/${bin}-ge.1
done
for bin in `find $RPM_BUILD_ROOT%{_bindir} -type f -o -type l`
do
    ln -s ../../../../bin/`basename $bin` \
          $RPM_BUILD_ROOT%{_datadir}/gridengine/bin/${gearch}/`basename $bin -ge`
done

# utilbin
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/gridengine/utilbin
mv $RPM_BUILD_ROOT%{_datadir}/gridengine/utilbin/* \
   $RPM_BUILD_ROOT%{_libexecdir}/gridengine/utilbin
ln -s ../../../libexec/gridengine/utilbin \
      $RPM_BUILD_ROOT%{_datadir}/gridengine/utilbin/${gearch}
# We also need some db utils
ln -s ../../../bin/db_dump ../../../bin/db_load \
      $RPM_BUILD_ROOT%{_datadir}/gridengine/utilbin/

# lib
mkdir -p $RPM_BUILD_ROOT%{_prefix}
mv $RPM_BUILD_ROOT%{_datadir}/gridengine/lib $RPM_BUILD_ROOT%{_libdir}
ln -s ../../%{_lib}/gridengine $RPM_BUILD_ROOT%{_datadir}/gridengine/lib
# libcore.so
install -p -m755 libcore.so $RPM_BUILD_ROOT%{_libdir}
# Move the JNI libraries
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
for jni in jgdi juti
do
  mv $RPM_BUILD_ROOT%{_libdir}/${jni}.jar $RPM_BUILD_ROOT%{_libdir}/lib${jni}.so \
     $RPM_BUILD_ROOT%{_libdir}/%{name}/
done
mkdir -p $RPM_BUILD_ROOT%{_javadir}
mv $RPM_BUILD_ROOT%{_libdir}/drmaa.jar $RPM_BUILD_ROOT%{_javadir}/drmaa.jar
mv $RPM_BUILD_ROOT%{_libdir}/JSV.jar $RPM_BUILD_ROOT%{_javadir}/JSV.jar

# include
mv $RPM_BUILD_ROOT%{_datadir}/gridengine/include $RPM_BUILD_ROOT%{_includedir}

# app-defaults
mkdir -p $RPM_BUILD_ROOT%{_datadir}/X11/app-defaults
mv $RPM_BUILD_ROOT%{_datadir}/gridengine/qmon/*.ad \
   $RPM_BUILD_ROOT%{_datadir}/X11/app-defaults

# The default cell directories
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gridengine/default/common

# The default qmaster, spool, and spooldb directories
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/spool/gridengine/default/qmaster
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/spool/gridengine/default/spool/{admin_hosts,cqueues,job_scripts,resource_quotas,zombies,calendars,exec_hosts,pe,submit_hosts,centry,hostgroups,projects,users,ckpt,jobs,qinstances,usersets}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/spool/gridengine/default/spooldb

# Bootstrap file
#cp %SOURCE7 $RPM_BUILD_ROOT%{_datadir}/gridengine/default/common/

# These files get created during user setup (install_qmaster)
for f in common/{act_qmaster,bootstrap,qtask,settings.csh,settings.sh,sge_aliases,sgeexecd,sgemaster,sge_request}
do
   touch $RPM_BUILD_ROOT%{_datadir}/gridengine/default/${f}
done
for f in qmaster/job_scripts spooldb/{__db.00{1,2,3,4,5,6},log.0000000001,sge,sge_job}
do
   touch $RPM_BUILD_ROOT%{_localstatedir}/spool/gridengine/default/${f}
done

# Environment (SGE_ROOT)
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/
install -p -m644 %SOURCE3 %SOURCE4 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/

# Startup scripts
%if 0%{?fedora} >= 15
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m755 %SOURCE5 %SOURCE6 %SOURCE13 $RPM_BUILD_ROOT%{_unitdir}
%else
mkdir -p $RPM_BUILD_ROOT%{_initrddir}
install -p -m755 %SOURCE5 %SOURCE6 $RPM_BUILD_ROOT%{_initrddir}
%endif
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -p -m644 %SOURCE9 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/gridengine

#sgeCA
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/sgeCA

# Don't package catman files
rm -rf $RPM_BUILD_ROOT%{_datadir}/gridengine/catman

# Rename some man pages to avoid conflicts
pushd $RPM_BUILD_ROOT%{_mandir}/man5
for f in *
do
   if [ ${f:0:4} != sge_ ]
   then
      mv $f sge_$f
   fi
done
popd

#Don't need these
rm -rf $RPM_BUILD_ROOT%{_datadir}/gridengine/3rd_party
rm -rf $RPM_BUILD_ROOT%{_datadir}/gridengine/dtrace

#Don't ship example binaries
rm -rf $RPM_BUILD_ROOT%{_datadir}/gridengine/examples/jobsbin
rm -rf $RPM_BUILD_ROOT%{_datadir}/gridengine/examples/worker.*

#Cleanup some patch backups that get shipped
rm $RPM_BUILD_ROOT%{_datadir}/gridengine/util/install_modules/inst_*.sh.*

#TODO - Ship the GUI installer
rm $RPM_BUILD_ROOT%{_datadir}/gridengine/start_gui_installer


%clean
rm -rf $RPM_BUILD_ROOT


%pre
getent group %{username} >/dev/null || groupadd -r %{username}
getent passwd %{username} >/dev/null || \
    useradd -r -g %{username} -d %{homedir} -s /sbin/nologin \
    -c '%{gecos}' %{username}
exit 0


%post -p /sbin/ldconfig

%posttrans
alternatives --install %{_bindir}/qsub qsub %{_bindir}/qsub-ge 10 \
        --slave %{_mandir}/man1/qsub.1.gz qsub-man \
                %{_mandir}/man1/qsub-ge.1.gz \
        --slave %{_bindir}/qalter qalter %{_bindir}/qalter-ge \
        --slave %{_mandir}/man1/qalter.1.gz qalter-man \
                %{_mandir}/man1/qalter-ge.1.gz \
        --slave %{_bindir}/qdel qdel %{_bindir}/qdel-ge \
        --slave %{_mandir}/man1/qdel.1.gz qdel-man \
                %{_mandir}/man1/qdel-ge.1.gz \
        --slave %{_bindir}/qhold qhold %{_bindir}/qhold-ge \
        --slave %{_mandir}/man1/qhold.1.gz qhold-man \
                %{_mandir}/man1/qhold-ge.1.gz \
        --slave %{_bindir}/qrls qrls %{_bindir}/qrls-ge \
        --slave %{_mandir}/man1/qrls.1.gz qrls-man \
                %{_mandir}/man1/qrls-ge.1.gz \
        --slave %{_bindir}/qselect qselect %{_bindir}/qselect-ge \
        --slave %{_mandir}/man1/qselect.1.gz qselect-man \
                %{_mandir}/man1/qselect-ge.1.gz \
        --slave %{_bindir}/qstat qstat %{_bindir}/qstat-ge \
        --slave %{_mandir}/man1/qstat.1.gz qstat-man \
                %{_mandir}/man1/qstat-ge.1.gz || :

%preun
if [ $1 -eq 0 ] ; then 
    alternatives --remove qsub %{_bindir}/qsub-ge || :
fi

%postun -p /sbin/ldconfig


%post execd
%if 0%{?fedora}
%if 0%{?fedora} >= 18
%systemd_post sge_execd.service
%else
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%endif
%else
/sbin/chkconfig --add sge_execd
%endif


%postun execd
%if 0%{?fedora}
%if 0%{?fedora} >= 18
%systemd_postun_with_restart sge_execd.service
%else
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart sge_execd.service >/dev/null 2>&1 || :
fi
%endif
%else
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /sbin/service sge_execd condrestart >/dev/null 2>&1 || :
fi
%endif

%preun execd
%if 0%{?fedora}
%if 0%{?fedora} >= 18
%systemd_preun sge_execd.service
%else
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable sge_execd.service > /dev/null 2>&1 || :
    /bin/systemctl stop sge_execd.service > /dev/null 2>&1 || :
fi
%endif
%else
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /sbin/service sge_execd stop
    /sbin/chkconfig --del sge_execd
fi
%endif

%if 0%{?fedora} >= 15
%triggerun -- gridengine-execd < 6.2u5p2-2
/usr/bin/systemd-sysv-convert --save sge_execd >/dev/null 2>&1 || :
/sbin/chkconfig --del sge_execd >/dev/null 2>&1 || :
/bin/systemctl try-restart sge_execd.service >/dev/null 2>&1 || :
%endif

%post qmaster
%if 0%{?fedora}
%if 0%{?fedora} >= 18
%systemd_post sgemaster.service
%systemd_post sge_shadowd.service
%else
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%endif
%else
/sbin/chkconfig --add sgemaster
%endif

%postun qmaster
%if 0%{?fedora}
%if 0%{?fedora} >= 18
%systemd_postun_with_restart sgemaster.service
%systemd_postun_with_restart sge_shadowd.service
%else
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart sgemaster.service >/dev/null 2>&1 || :
fi
%endif
%else
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /sbin/service sgemaster condrestart >/dev/null 2>&1 || :
fi
%endif

%preun qmaster
%if 0%{?fedora}
%if 0%{?fedora} >= 18
%systemd_preun sgemaster.service
%systemd_preun sge_shadowd.service
%else
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable sgemaster.service > /dev/null 2>&1 || :
    /bin/systemctl stop sgemaster.service > /dev/null 2>&1 || :
fi
%endif
%else
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /sbin/service sgemaster stop
    /sbin/chkconfig --del sgemaster
fi
%endif


%files
%doc Licenses README
%config(noreplace) %{_sysconfdir}/profile.d/sge.*
%config(noreplace) %{_sysconfdir}/sysconfig/gridengine
# Only the file %{_bindir}/qmake-ge is
# under GPLv2+
# Olny the file %{_bindir}/qtcsh is
# under BSD with advertising
%{_bindir}/*
%exclude %{_bindir}/qacct
%exclude %{_bindir}/qmon
%exclude %{_bindir}/sge_execd
%exclude %{_bindir}/sge_qmaster
%exclude %{_bindir}/sge_shadowd
%exclude %{_bindir}/sge_*shepherd
%{_libdir}/%{name}
%{_libdir}/libcore.so
%{_libdir}/libdrmaa.so*
%{_libdir}/libspoolb.so
%{_libdir}/libspoolc.so
%{_javadir}/drmaa.jar
%{_javadir}/JSV.jar
%{_libexecdir}/gridengine/
%attr(-,%username,%username) %dir %{_datadir}/gridengine
%{_datadir}/gridengine/bin
%exclude %{_datadir}/gridengine/bin/*/qacct
%exclude %{_datadir}/gridengine/bin/*/qmon
%exclude %{_datadir}/gridengine/bin/*/sge_execd
%exclude %{_datadir}/gridengine/bin/*/sge_qmaster
%exclude %{_datadir}/gridengine/bin/*/sge_shadowd
%exclude %{_datadir}/gridengine/bin/*/sge_*shepherd
%{_datadir}/gridengine/ckpt
%attr(-,%username,%username) %ghost %{_datadir}/gridengine/default
%{_datadir}/gridengine/doc
%{_datadir}/gridengine/hadoop
%{_datadir}/gridengine/inst_sge
%{_datadir}/gridengine/lib
%{_datadir}/gridengine/mpi
%{_datadir}/gridengine/my_configuration.conf
%dir %{_datadir}/gridengine/pvm
%{_datadir}/gridengine/pvm/*
%exclude %{_datadir}/gridengine/pvm/src
%{_datadir}/gridengine/util
%dir %{_datadir}/gridengine/utilbin
%{_datadir}/gridengine/utilbin/*
%exclude %{_datadir}/gridengine/utilbin/db_*
%{_mandir}/man1/*.1*
%exclude %{_mandir}/man1/qmon.1*
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*
%exclude %{_mandir}/man8/sge_qmaster.8*
%exclude %{_mandir}/man8/sge_shadowd.8*
%exclude %{_mandir}/man8/sge_execd.8*
%exclude %{_mandir}/man8/sge_*shepherd.8*
%attr(-,%username,%username) %dir %{_localstatedir}/spool/gridengine
%attr(-,%username,%username) %dir %{_localstatedir}/spool/gridengine/default

%files devel
%{_includedir}/*
%{_datadir}/gridengine/examples
%{_datadir}/gridengine/pvm/src
%{_mandir}/man3/*.3*

%files qmon
%{_bindir}/qmon
%{_libdir}/libXltree.so
%{_datadir}/X11/app-defaults/*
%{_datadir}/gridengine/bin/*/qmon
%{_datadir}/gridengine/qmon/
%{_mandir}/man1/qmon.1*

%files execd
%if 0%{?fedora} >= 15
%{_unitdir}/sge_execd.service
%else
%{_initrddir}/sge_execd
%endif
%{_bindir}/sge_execd
%{_bindir}/sge_*shepherd
%{_datadir}/gridengine/install_execd
%{_datadir}/gridengine/bin/*/sge_execd
%{_datadir}/gridengine/bin/*/sge_*shepherd
%{_mandir}/man8/sge_execd.8*
%{_mandir}/man8/sge_*shepherd.8*

%files qmaster
%if 0%{?fedora} >= 15
%{_unitdir}/sgemaster.service
%{_unitdir}/sge_shadowd.service
%else
%{_initrddir}/sgemaster
%endif
%{_bindir}/qacct
%{_bindir}/sge_qmaster
%{_bindir}/sge_shadowd
%{_datadir}/gridengine/bin/*/qacct
%{_datadir}/gridengine/bin/*/sge_qmaster
%{_datadir}/gridengine/bin/*/sge_shadowd
%{_datadir}/gridengine/install_qmaster
%{_datadir}/gridengine/utilbin/db_*
%{_mandir}/man8/sge_qmaster.8*
%{_mandir}/man8/sge_shadowd.8*
%attr(-,%username,%username) %dir %{_localstatedir}/sgeCA
%attr(-,%username,%username) %ghost %{_localstatedir}/spool/gridengine/default/qmaster
%attr(-,%username,%username) %ghost %{_localstatedir}/spool/gridengine/default/spool
%attr(-,%username,%username) %ghost %{_localstatedir}/spool/gridengine/default/spooldb


%changelog
* Thu Apr 9 2015 Nico Faerber <nico.faerber@id.unibe.ch> - 2011-11p1-23
- Provide sgemaster and sge_execd files for centos installation

* Thu Sep 4 2014 Orion Poplawski <orion@cora.nwra.com> - 2011.11p1-22
- Add PIDFile to sgemaster.service (bug #1082129)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.11p1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 7 2014 Orion Poplwski <orion@cora.nwra.com> - 2011.11p1-20
- Fix build with -Werror=format-security (bug #1037103)

* Mon Jul 14 2014 Orion Poplwski <orion@cora.nwra.com> - 2011.11p1-19
- Use After=network-online.target for service files

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.11p1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 3 2013 Orion Poplwski <orion@cora.nwra.com> - 2011.11p1-17
- Upload updated tarball without .svn dirs
- Drop non-functional url for libcore.c

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 2011.11p1-16
- Perl 5.18 rebuild

* Tue Jul 30 2013 Orion Poplwski <orion@cora.nwra.com> - 2011.11p1-15
- Ship libdrmaa.so in main package, needed for Java runtime (bug #671880)

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2011.11p1-14
- Perl 5.18 rebuild

* Tue May 21 2013 Orion Poplwski <orion@cora.nwra.com> - 2011.11p1-13
- Add sge_shadowd.service and move shadowd to qmaster package (bug #955768)

* Tue May 21 2013 Orion Poplwski <orion@cora.nwra.com> - 2011.11p1-12
- Add patch to add LDFLAGS to LFLAGS so _hardened_build actually works (bug #965479)

* Wed May 1 2013 Orion Poplawski <orion@cora.nwra.com> - 2011.11p1-11
- Fix user/group creation to use dynamic id allocation

* Wed Apr 24 2013 Orion Poplawski <orion@cora.nwra.com> - 2011.11p1-10
- Use updated systemd scriptlets (bug #850136)

* Mon Apr 22 2013 Orion Poplawski <orion@cora.nwra.com> - 2011.11p1-9
- Only BR ant-nodeps on RHEL

* Wed Apr 10 2013 Jon Ciesla <limburgher@gmail.com> - 2011.11p1-8
- Migrate from fedora-usermgmt to guideline scriptlets.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.11p1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 16 2012 Orion Poplawski <orion@cora.nwra.com> 2011.11p1-6
- Build java with source/target 1.5 to properly compile generics (bug 842595)

* Wed Oct 3 2012 Orion Poplawski <orion@cora.nwra.com> 2011.11p1-5
- Add patch to generate load sensor reports just before sending them
- Only BR hostname on Fedora
- Fix Fedora conditional for db4 support

* Fri Aug 3 2012 Orion Poplawski <orion@cora.nwra.com> 2011.11p1-4
- Support libdb4 in Fedora 18+

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.11p1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 9 2012 Orion Poplawski <orion@cora.nwra.com> 2011.11p1-2
- Do not remove spool directory in execd uninstall script (bug 836102)

* Mon Jul 9 2012 Orion Poplawski <orion@cora.nwra.com> 2011.11p1-1
- Update to 2011.11p1
- Drop env-code-injection, buffer-overflow, and symlink patches
- Rebase rctemplates patch

* Fri Jul 6 2012 Orion Poplawski <orion@cora.nwra.com> 2011.11-4.svn131
- Add patch to set JAVA_LIB_ARCH on arm (bug 837137)
- Add BR hostname

* Tue Apr 17 2012 Orion Poplawski <orion@cora.nwra.com> 2011.11-3.svn131
- Set _hardened_build
- Add two more upstream security patches
- Renumber patches

* Tue Apr 17 2012 Orion Poplawski <orion@cora.nwra.com> 2011.11-2.svn131
- Update to svn 131
- Add upstream env-code-injection security patch

* Wed Mar 21 2012 Orion Poplawski <orion@cora.nwra.com> 2011.11-1.svn115
- Update to svn 115
- Add back SysV init script handling for EL builds
- Drop inst, db, lesstif, libs, error, openssl, qtcsh patches fixed upstream
- Build with -sys-libssl
- Use sge_/SGE_ names in man pages

* Wed Mar 14 2012 Orion Poplawski <orion@cora.nwra.com> 2011.11-1.svn93
- Update to gridscheduler 2011.11 plus svn revision 93
- Rebase ssl, rctemplates, and rpath patches
- Drop Werror, quotes, ant, auto, jemalloc, paths, and add-missing
  patches fixed upstream
- Add qtcsh patch to avoid using -R when linking
- Add BR on hwloc-devel
- Make systemd conditional on Fedora >= 15
- Use -sys-hwloc and -sys-jemalloc aimk flags
- Remove qacct and sge_qmaster from BINFILES checks (Bug 803502)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2u5p2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 14 2011 Orion Poplawski <orion@cora.nwra.com> 6.2u5p2-6
- Update linux 3 patch to fix installed arch script as well

* Thu Sep 8 2011 Orion Poplawski <orion@cora.nwra.com> 6.2u5p2-5
- Add patch to properly quote m4 macros
- Add patch to hack linux 3 support - keeps arch as lx26-*
- Add patch to run automake with --add-missing to fix qmake build

* Tue Sep 6 2011 Orion Poplawski <orion@cora.nwra.com> 6.2u5p2-4
- Add SysV to systemd migration triggers

* Tue Sep 6 2011 Orion Poplawski <orion@cora.nwra.com> 6.2u5p2-3
- Add BR groff

* Tue Sep 6 2011 Orion Poplawski <orion@cora.nwra.com> 6.2u5p2-2
- Migrate to systemd unit files

* Tue Sep 6 2011 Orion Poplawski <orion@cora.nwra.com> 6.2u5p2-1
- Update to opengridscheduler release 6.2u5p2
- Drop patches applied upstream

* Fri Jul 29 2011 Orion Poplawski <orion@cora.nwra.com> 6.2u5-10
- Move sge_*shepherd to execd sub-package

* Thu Jun 23 2011 Orion Poplawski <orion@cora.nwra.com> 6.2u5-9
- Use system jemalloc library, fixes FTBFS bug 715676
- Cleanup some '//' in include paths triggering debugedit failures

* Fri May 6 2011 Orion Poplawski <orion@cora.nwra.com> 6.2u5-8
- Add patches from opengridscheduler to fix vmem reporting and
  slotwise preemption

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2u5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 6 2010 Orion Poplawski <orion@cora.nwra.com> 6.2u5-6
- Add Requires: xorg-x11-fonts-ISO8859-1-100dpi xorg-x11-fonts-ISO8859-1-75dpi
  to qmon package (bug 657406)
- Add patch to fix issue with hostnames (bug 654943)

* Wed Aug 25 2010 - Orion Poplawski <orion@cora.nwra.com> - 6.2u5-5
- Update instructions to referece ./my_configuration.conf (bug #557628)
- Don't set IFS when reading conf file, breaks lots of stuff
- Set SGE_JVM_LIB_PATH to none by default so we don't setup JMF

* Wed Aug 11 2010 - Orion Poplawski <orion@cora.nwra.com> - 6.2u5-4
- Use upstream my_configuration.conf as template for default one (bugs 557628,566294)
- Set SGE_CELL in sge.sh/sge.csh (bug 620907)

* Mon Jul 12 2010 - Orion Poplawski <orion@cora.nwra.com> - 6.2u5-3
- Exclude ppc64 - no java 1.6.0

* Tue Feb 16 2010 - Orion Poplawski <orion@cora.nwra.com> - 6.2u5-2
- Update ssl patch to add -lcrypt to fix FTBFS bug #565003

* Mon Dec 28 2009 - Orion Poplawski <orion@cora.nwra.com> - 6.2u5-1
- Update to 6.2u5

* Thu Oct 29 2009 - Orion Poplawski <orion@cora.nwra.com> - 6.2u4-1
- Update to 6.2u4
- Drop import patch fixed upstream
- Updated rctemplates and auto patches
- Add patch to call ant with appropriate library directory

* Tue Aug 25 2009 Tomas Mraz <tmraz@redhat.com> - 6.2u3-3
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2u3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 - Orion Poplawski <orion@cora.nwra.com> - 6.2u3-1
- Update to 6.2u3
- Drop ppc patch fixed upstream
- Update rctemplates patch

* Mon Apr 6 2009 - Orion Poplawski <orion@cora.nwra.com> - 6.2u2_1-1
- Update to 6.2u2_1
- Rebase several patches
- Add patch to rename getline()
- Add patch to compile with correct libs on ppc/ppc64

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2u1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 - Orion Poplawski <orion@cora.nwra.com> - 6.2u1-3
- Add patch to import specific classes to avoid pulling in other ones

* Thu Jan 15 2009 - Orion Poplawski <orion@cora.nwra.com> - 6.2u1-2
- Rebuild with openssl-0.9.8j

* Thu Dec 18 2008 - Orion Poplawski <orion@cora.nwra.com> - 6.2u1-1
- Update to 6.2u1

* Mon Nov 17 2008 - Orion Poplawski <orion@cora.nwra.com> - 6.2-5
- Leave qmake-ge in %{_bindir}
- Use system db_* utils in bdb_checkpoint script
- Fix xterm path in default setup
- Change java BR to >= 1.6.0 to allow building with other 1.6 javas

* Tue Nov 11 2008 - Orion Poplawski <orion@cora.nwra.com> - 6.2-4
- Add note to README about localhost line in /etc/hosts
- Cleanup setting.sh some, no more MAN stuff
- Add conditional build support for EL

* Wed Nov 5 2008 - Orion Poplawski <orion@cora.nwra.com> - 6.2-3
- Add Requires: ncurses for "clear"
- Add patch from CVS to update install scripts
- Patch sge_ca script not to use system openssl
- Modify code to dlopen runtime ssl library
- Patch install_qmaster to update /etc/sysconfig/gridengine
- Point install scripts to proper JAVA_HOME
- Have sgemaster init script use /etc/sysconfig/gridengine
- Add patch to point to jni library locations
- Make sure install_qmaster sets up default managers/operators

* Fri Sep 26 2008 - Orion Poplawski <orion@cora.nwra.com> - 6.2-2
- No more sge_schedd in 6.2, remove from startup script

* Mon Aug 11 2008 - Orion Poplawski <orion@cora.nwra.com> - 6.2-1
- Update to 6.2 final

* Tue Jul 15 2008 - Orion Poplawski <orion@cora.nwra.com> - 6.2beta2-0.1
- Provide some installation instructions for these RPMs
- Fix up some installation script issues
- Ghost more directories created later

* Thu Jun 5 2008 - Orion Poplawski <orion@cora.nwra.com> - 6.2beta-0
- Update to 6.2beta
- Use aimk.private and build_private.properties instead of patching
  aimk and build.properties
- Cleanup some extra /s in paths
- Shift to Java 1.6.0 because of new requirements in the source
- Move Java JNI libraries to proper location
- Drop several upstreamed patches
- Add patch to avoid linking unneeded libraries

* Fri Apr 11 2008 - Orion Poplawski <orion@cora.nwra.com> - 6.1u4-1
- Update to 6.1u4

* Tue Apr 1 2008 - Orion Poplawski <orion@cora.nwra.com> - 6.1u3-7
- Use alternatives to avoid conflicts with torque (bug #437613)
- Add patch to support stricter csh variable handling

* Fri Feb  8 2008 - Orion Poplawski <orion@cora.nwra.com> - 6.1u3-6
- Fixup subpackage License tags
- Service name change in scriptlets

* Thu Feb  7 2008 - Orion Poplawski <orion@cora.nwra.com> - 6.1u3-5
- Rewrite initscripts
- Remove spurious Requires(post): /sbin/ldconfig
- Add License explanation file and fix License tags

* Mon Feb  4 2008 - Orion Poplawski <orion@cora.nwra.com> - 6.1u3-4
- Drop arch from source
- Fix Requires() for main package
- Move man3 to -devel

* Fri Feb  1 2008 - Orion Poplawski <orion@cora.nwra.com> - 6.1u3-3
- Fix various review comments and rpmlint issues (bug #316141)

* Thu Jan 31 2008 - Orion Poplawski <orion@cora.nwra.com> - 6.1u3-2
- Actually ship sge_execd in the execd subpackage
- Don't complain about missing sge_execd during inst_sge -upd
- Link in db_dump and db_load into utilbin so that update scripts can find them

* Wed Jan  9 2008 - Orion Poplawski <orion@cora.nwra.com> - 6.1u3-1
- Update to 6.1u3
- Split execd into sub-package

* Thu Nov 15 2007 - Orion Poplawski <orion@cora.nwra.com> - 6.1u2-5
- Add BR net-tools for hostname for java build on devel

* Mon Nov 12 2007 - Orion Poplawski <orion@cora.nwra.com> - 6.1u2-4
- Add patch and source for ppc/ppc64 builds

* Fri Nov  2 2007 - Orion Poplawski <orion@cora.nwra.com> - 6.1u2-3
- Add patch to fix qstat xml output

* Thu Oct 18 2007 - Orion Poplawski <orion@cora.nwra.com> - 6.1u2-2
- Cleanup arch handling
- Install qevent

* Tue Oct  2 2007 - Orion Poplawski <orion@cora.nwra.com> - 6.1u2-1
- Fedora packaging
