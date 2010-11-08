# TODO:
# - Deal with unpackaged pod files
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Date
%define		pnam	Manip
Summary:	Date::Manip - date manipulation routines
Summary(pl.UTF-8):	Date::Manip - procedury do operowania na datach
Name:		perl-Date-Manip
Version:	6.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/S/SB/SBECK/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9119d2ef3612adb819fe9e814dec0e6a
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-DateManip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module Date::Manip contains a set of routines designed to make
any common date/time manipulation easy to do. Operations such as
comparing two times, calculating a time a given amount of time from
another, or parsing international times are all easily done.

%description -l pl.UTF-8
Moduł Perla Date::Manip zawiera zbiór procedur zaprojektowanych, aby
ułatwić często wykonywane operacje na datach/czasie. Operacje takie
jak porównywanie dwóch czasów, obliczanie czasu następującego po
zadanej ilości czasu od innego czasu, analiza czasów z podaną strefą
czasową - wszystkie łatwo wykonać.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc README
%{perl_vendorlib}/Date/*.pm
%dir %{perl_vendorlib}/Date/Manip
%{perl_vendorlib}/Date/Manip/*.pm
%dir %{perl_vendorlib}/Date/Manip/Lang
%{perl_vendorlib}/Date/Manip/Lang/*.pm
%dir %{perl_vendorlib}/Date/Manip/Offset
%{perl_vendorlib}/Date/Manip/Offset/*.pm
%dir %{perl_vendorlib}/Date/Manip/TZ
%{perl_vendorlib}/Date/Manip/TZ/*.pm
%{_mandir}/man3/*
