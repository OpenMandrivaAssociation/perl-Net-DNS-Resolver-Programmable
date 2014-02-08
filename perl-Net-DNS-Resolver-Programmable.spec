%define real_name Net-DNS-Resolver-Programmable

Summary:	Programmable DNS resolver class for offline emulation of DNS
Name:		perl-%{real_name}
Version:	0.003
Release:	8
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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.003-7mdv2012.0
+ Revision: 765525
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.003-6
+ Revision: 764041
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.003-5
+ Revision: 667271
- mass rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.003-4mdv2011.0
+ Revision: 426540
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.003-3mdv2009.0
+ Revision: 223851
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.003-2mdv2008.1
+ Revision: 180497
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 02 2007 Oden Eriksson <oeriksson@mandriva.com> 0.003-1mdv2008.0
+ Revision: 47036
- Import perl-Net-DNS-Resolver-Programmable



* Mon Jul 02 2007 Oden Eriksson <oeriksson@mandriva.com> 0.003-1mdv2008.0
- initial Mandriva package 
