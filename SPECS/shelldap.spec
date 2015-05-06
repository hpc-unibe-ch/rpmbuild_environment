%define         debug_package %{nil}
%define         __arch_install_post   %{nil}

Name:		shelldap
Version:	1.3.1
Release:	2%{?dist}
Summary:	Shell-like interface to LDAP servers
License:	BSD
URL:		http://projects.martini.nu/shelldap
Group:          Productivity/Networking/LDAP/Clients
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:       perl(Term::ReadLine::Gnu)

%description
A handy shell-like interface for browsing LDAP servers and editing their
content. It keeps command history, has sane autocompletes, credential caching,
site-wide and individual configs, and it's fun to say. Shelldap! Shelldap!
Shelldap!

%prep
%setup

%build
pod2man shelldap shelldap.1

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 shelldap %{buildroot}%{_bindir}
install -m 644 shelldap.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(755,root,root,-)
%{_bindir}/shelldap
%defattr(644,root,root,-)
%{_mandir}/man1/shelldap.1*

%changelog
* Wed May 06 2015 Michael Rolli <michael.rolli@id.unibe.ch> - 1.3.1
- Initial build from source@377bd38ab38c

