%define real_name Net-DNS-Resolver-Programmable

Summary:	Programmable DNS resolver class for offline emulation of DNS
Name:		perl-%{real_name}
Version:	0.003
Release:	%mkrel 7
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JM/JMEHNLE/net-dns-resolver-programmable/%{real_name}-v%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Module-Build
BuildRequires:	perl-Net-DNS
BuildRequires:	perl-version
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Net::DNS::Resolver::Programmable is a Net::DNS::Resolver descendant class that
allows a virtual DNS to be emulated instead of querying the real DNS. A set of
static DNS records may be supplied, or arbitrary code may be specified as a
means for retrieving DNS records, or even generating them on the fly.

%prep

%setup -q -n %{real_name}-v%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES LICENSE README TODO
%{perl_vendorlib}/Net/DNS/Resolver/*.pm
%{_mandir}/*/*
