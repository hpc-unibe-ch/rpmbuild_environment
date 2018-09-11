Name:		shelldap
Version:	1.4.0
Release:	3%{?dist}
Summary:	A shell-like interface for browsing LDAP servers

License:	BSD
URL:		https://bitbucket.org/mahlon/%{name}
Source0:	%{url}/downloads/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires:	perl-generators perl-interpreter perl(Config) perl-podlators
# perl-generators takes care of the 'Requires' tag.
Requires:       perl(YAML::Syck) perl(Term::Shell) perl(Digest::MD5) perl(Net::LDAP) perl(Algorithm::Diff)
Requires:	perl(IO::Socket::SSL) perl(Authen::SASL) perl(Term::ReadLine::Gnu)

%description
A handy shell-like interface for browsing LDAP servers and editing their
content. It keeps command history, has sane auto-completion, credential caching,
site-wide and individual configurations.

%prep
%setup -q
perl -MConfig -i -pe 's{^#!/usr/bin/env perl}{$Config{startperl}}' %{name}

%build
pod2man shelldap > shelldap.1
perl -n -e 'if(m/^#/){print if($. > 4)}else{exit 0}' shelldap > LICENSE.txt

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
install -p -m 755 shelldap %{buildroot}%{_bindir}/shelldap
install -p -m 644 shelldap.1 %{buildroot}%{_mandir}/man1/shelldap.1

%files
%license LICENSE.txt
%doc README.md CHANGELOG CONTRIBUTORS
%{_bindir}/shelldap
%{_mandir}/man1/shelldap.1.*

%changelog
* Wed Aug 29 2018 Rolli, Michael (ID) <michael.rolli@id.unibe.ch> - 1.4.0-3
- Rebuilt for http://id-mirror.unibe.ch/mrepo/centos7-x86_64/RPMS.ubelix/repoview/

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 27 2018 Timothée Floure <fnux@fedoraproject.org> - 1.4.0-1
- Let there be package.
