%include	/usr/lib/rpm/macros.perl
%define	pdir	Date
%define	pnam	Manip
Summary:	Date::Manip - date manipulation routines
Summary(pl):	Date::Manip - procedury do operowania na datach
Name:		perl-Date-Manip
Version:	5.40
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-DateManip

%description
Date::Manip - date manipulation routines.

%description -l pl
Date::Manip - procedury do operowania na datach.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO *.cnf
%{perl_vendorlib}/Date/Manip.pm
%{_mandir}/man3/*
