%include	/usr/lib/rpm/macros.perl
Summary:	Date-Manip perl module
Summary(pl):	Modu³ perla Date-Manip
Name:		perl-Date-Manip
Version:	5.36
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Date/DateManip-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Date-Manip - date manipulation routines.

%description -l pl
Date-Manip - rutyny do operowania na dacie.

%prep
%setup -q -n DateManip-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Date/Manip
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO}.gz *.cnf

%{perl_sitelib}/Date/Manip.pm
%{perl_sitearch}/auto/Date/Manip

%{_mandir}/man3/*
