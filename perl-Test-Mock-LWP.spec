#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	Mock-LWP
Summary:	Test::Mock::LWP - Easy mocking of LWP packages
Name:		perl-Test-Mock-LWP
Version:	0.06
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	367aef3c6c709db2442eb0f3a61dd772
URL:		http://search.cpan.org/dist/Test-Mock-LWP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::MockObject) >= 1.08
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package arises from duplicating the same code to mock LWP et al in
several different modules I've written.  This version is very minimalist, but
works for my needs so far.  I'm very open to new suggestions and improvements.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Test/Mock
%{perl_vendorlib}/Test/Mock/*.pm
%dir %{perl_vendorlib}/Test/Mock/LWP
%{perl_vendorlib}/Test/Mock/LWP/*.pm
%dir %{perl_vendorlib}/Test/Mock/HTTP
%{perl_vendorlib}/Test/Mock/HTTP/*.pm
%{_mandir}/man3/*
