%define upstream_name    Log-Any
%define upstream_version 0.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.15
Release:	3

Summary:	Allows CPAN modules to safely and efficiently log messages
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Log/Log-Any-0.15.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::Simple)
BuildArch:	noarch

%description
'Log::Any' allows CPAN modules to safely and efficiently log messages,
while letting the application choose (or decline to choose) a logging
mechanism such as 'Log::Dispatch' or 'Log::Log4perl'.

'Log::Any' has a very tiny footprint and no dependencies beyond Perl 5.6,
which makes it appropriate for even small CPAN modules to use. It defaults
to 'null' logging activity, so a module can safely log without worrying
about whether the application has chosen (or will ever choose) a logging
mechanism.

The application, in turn, may choose one or more logging mechanisms via
Log::Any::Adapter.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.120.0-2mdv2011.0
+ Revision: 657446
- rebuild for updated spec-helper

* Sat Mar 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.120.0-1
+ Revision: 648575
- update to new version 0.12

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 505267
- update to 0.11

* Wed Jan 06 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.1
+ Revision: 486603
- update to 0.10

* Tue Jan 05 2010 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.1
+ Revision: 486312
- import perl-Log-Any


* Tue Jan 05 2010 cpan2dist 0.08-1mdv
- initial mdv release, generated with cpan2dist

