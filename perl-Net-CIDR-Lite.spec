%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	CIDR-Lite
Summary:	Net::CIDR::Lite - parse, manipulate and lookup IP network blocks
Name:		perl-Net-CIDR-Lite
Version:	0.15
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ecda840da7e401c96469e04083cc2af1
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::CIDR::Liste parses and understands IPv4 CIDR blocks.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc README
%{perl_vendorlib}/Net/CIDR/Lite.pm
%{_mandir}/man3/*
