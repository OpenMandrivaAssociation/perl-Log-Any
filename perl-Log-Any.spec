%define upstream_name    Log-Any
%define upstream_version 1.720

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Allows CPAN modules to safely and efficiently log messages
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/preaction/Log-Any
Source0:	https://cpan.metacpan.org/authors/id/P/PR/PREACTION/Log-Any-1.720.tar.gz

BuildRequires:	make
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

