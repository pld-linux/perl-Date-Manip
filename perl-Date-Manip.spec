%include	/usr/lib/rpm/macros.perl
Summary:	Date-Manip perl module
Summary(pl):	Modu³ perla Date-Manip
Name:		perl-Date-Manip
Version:	5.40
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Date/DateManip-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-DateManip

%description
Date-Manip - date manipulation routines.

%description -l pl
Date-Manip - rutyny do operowania na dacie.

%prep
%setup -q -n DateManip-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz *.cnf
%{perl_sitelib}/Date/Manip.pm
%{_mandir}/man3/*
