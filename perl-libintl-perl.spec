%define modname libintl-perl
%define modver 1.31

%if %{_use_internal_dependency_generator}
%define __noautoreq '/bin/false'
%endif

Summary:	A localization library for Perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	LGPLv2
Group:		Development/Perl
Url:		https://metacpan.org/release/libintl-perl
Source0:	http://www.cpan.org/authors/id/G/GU/GUIDO/%{modname}-%{modver}.tar.gz
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
%setup -qn %{modname}-%{modver}

%build
# fix build with modules from ./lib/:
export PERL_USE_UNSAFE_INC=1

perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
# fix build with modules from ./lib/:
export PERL_USE_UNSAFE_INC=1
%makeinstall_std

%files
%doc NEWS README THANKS TODO
%{perl_vendorlib}/Locale
%{perl_vendorarch}/auto/Locale
%{_mandir}/man3/*
