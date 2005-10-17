#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	CIDR-Lite
Summary:	Net::CIDR::Lite - parse, manipulate and lookup IP network blocks
Summary(pl):	Net::CIDR::Lite - analiza, przetwarzanie i wyszukiwanie blok�w sieci IP
Name:		perl-Net-CIDR-Lite
Version:	0.18
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c4c839713b701458e880bf2d058cbab4
BuildRequires:	perl-devel >= 1:5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-112.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::CIDR::Lite parses and understands IPv4 CIDR blocks.

%description -l pl
Modu� Net::CIDR::Lite analizuje bloki CIDR IPv4.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=site
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{perl_sitelib}/Net/CIDR
%{perl_sitelib}/Net/CIDR/Lite.pm
%{_mandir}/man3/*
