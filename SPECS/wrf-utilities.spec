%define         debug_package %{nil}
%define         __arch_install_post   %{nil}

Name:		wrf-utilities
Version:	1.0
Release:	1%{?dist}
Summary:	Additional binaries for the WRF model

Group:          Application/Scientific
License:	WRF Public Domain
URL:		http://www.mmm.ucar.edu/wrf/users/utilities/util.htm
Source0:	/gpfs/software/packages/programs-wrf/wrf-utilities-%{version}.tar.gz

%description
Various utilities supporting the Weather Research & Forecasting Model (WRF Model).

%prep
%setup -q


%build
# prepare some variables
export LIBDIR=/usr/lib64
export INCDIR=/usr/include
export MPI="openmpi"
export MPI_VERSION="1.6.5"

# Intel compiler
module load intel $MPI/$MPI_VERSION-intel
ifort p_interp.F90 -L$LIBDIR -lnetcdff -lm -I$INCDIR -o p_interp_ser_intel
ifort z_interp.F90 -L$LIBDIR -lnetcdff -lm -I$INCDIR -o z_interp_ser_intel
ifort no_interp.F90 -L$LIBDIR -lnetcdff -lm -I$INCDIR -o no_interp_ser_intel
mpif90 p_interp.F90 -L$LIBDIR -lnetcdff -lm -I$INCDIR -o p_interp_par_intel
mpif90 z_interp.F90 -L$LIBDIR -lnetcdff -lm -I$INCDIR -o z_interp_par_intel
mpif90 no_interp.F90 -L$LIBDIR -lnetcdff -lm -I$INCDIR -o no_interp_par_intel
module unload intel $MPI

# PGI-Compiler
module load pgi $MPI/$MPI_VERSION-pgi
pgf90 p_interp.F90 -L$LIBDIR -lnetcdff -lm -I$INCDIR -Mfree -o p_interp_ser_pgi
pgf90 z_interp.F90 -L$LIBDIR -lnetcdff -lm -I$INCDIR -Mfree -o z_interp_ser_pgi
pgf90 no_interp.F90 -L$LIBDIR -lnetcdff -lm -I$INCDIR -Mfree -o no_interp_ser_pgi
mpif90 p_interp.F90 -L$LIBDIR -lnetcdff -lm -I$INCDIR -Mfree -o p_interp_par_pgi
mpif90 z_interp.F90 -L$LIBDIR -lnetcdff -lm -I$INCDIR -Mfree -o z_interp_par_pgi
mpif90 no_interp.F90 -L$LIBDIR -lnetcdff -lm -I$INCDIR -Mfree -o no_interp_par_pgi
module unload pgi $MPI


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/%{name}
cp namelist* %{buildroot}/opt/%{name}
cp *_intel %{buildroot}/opt/%{name}
cp *_pgi %{buildroot}/opt/%{name}


%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}


%files
%defattr(644,root,root,-)
/opt/%{name}/namelist*
%defattr(755,root,root,-)
/opt/%{name}/*_intel
/opt/%{name}/*_pgi


%changelog
* Tue Nov 05 2013 Michael Rolli <michael.rolli@id.unibe.ch> - 1.0-1
- Initial build with p_interp, z_interp and no_interp

