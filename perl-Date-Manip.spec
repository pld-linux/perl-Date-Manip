%include	/usr/lib/rpm/macros.perl
%define	pdir	Date
%define	pnam	Manip
Summary:	Date::Manip - date manipulation routines
Summary(pl):	Date::Manip - procedury do operowania na datach
Name:		perl-Date-Manip
Version:	5.42a
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	648386bbf46d021ae283811f75b07bdf
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-DateManip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module Date::Manip contains a set of routines designed to make
any common date/time manipulation easy to do.  Operations such as
comparing two times, calculating a time a given amount of time from
another, or parsing international times are all easily done.

%description -l pl
Modu³ Perla Date::Manip zawiera zbiór procedur zaprojektowanych, aby
u³atwiæ czêsto wykonywane operacje na datach/czasie. Operacje takie
jak porównywanie dwóch czasów, obliczanie czasu nastêpuj±cego po
zadanej ilo¶ci czasu od innego czasu, analiza czasów z podan± stref±
czasow± - wszystkie ³atwo wykonaæ.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO *.cnf
%{perl_vendorlib}/Date/Manip.pm
%{_mandir}/man3/*
