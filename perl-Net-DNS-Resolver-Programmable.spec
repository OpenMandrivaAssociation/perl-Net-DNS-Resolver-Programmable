%define modname Net-DNS-Resolver-Programmable

Summary:	Programmable DNS resolver class for offline emulation of DNS
Name:		perl-%{modname}
Version:	0.003
Release:	9
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JM/JMEHNLE/net-dns-resolver-programmable/%{modname}-v%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-Module-Build
BuildRequires:	perl-Net-DNS
BuildRequires:	perl-version

%description
Net::DNS::Resolver::Programmable is a Net::DNS::Resolver descendant class that
allows a virtual DNS to be emulated instead of querying the real DNS. A set of
static DNS records may be supplied, or arbitrary code may be specified as a
means for retrieving DNS records, or even generating them on the fly.

%prep

%setup -qn %{modname}-v%{version} 

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc CHANGES LICENSE README TODO
%{perl_vendorlib}/Net/DNS/Resolver/*.pm
%{_mandir}/man3/*

