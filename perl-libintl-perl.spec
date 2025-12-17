%define modname libintl-perl

Summary:	A localization library for Perl
Name:		perl-%{modname}
Version:	1.33
Release:	2
License:	LGPLv2
Group:		Development/Perl
Url:		https://metacpan.org/release/libintl-perl
Source0:	http://www.cpan.org/authors/id/G/GU/GUIDO/%{modname}-%{version}.tar.gz
BuildRequires:	perl(Test)
BuildRequires:	gettext-devel
BuildRequires:	perl-devel
#gw yes, this is required by the tests
BuildRequires:	locales-de

%description
libintl-perl is a library that supports message translation for
Perl, written in pure Perl (version 5.004 or better). A faster C
version is also built and installed if the system fulfills all
requirements. Its interface is very similar to the gettext family
of functions in C, and it uses the same file formats as GNU
gettext, making it possible to use all tools available for gettext
itself and to seamlessly integrate internationalized Perl code
into mixed-language projects. An alternative library with a
similar purpose is available as Locale::MakeText. 

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
# fix build with modules from ./lib/:
export PERL_USE_UNSAFE_INC=1

perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
# fix build with modules from ./lib/:
export PERL_USE_UNSAFE_INC=1
%make_install

%files
%doc NEWS README THANKS TODO
%{perl_vendorlib}/Locale
%{perl_vendorarch}/auto/Locale
%{_mandir}/man3/*
