%define	upstream_name    libintl-perl
%define	upstream_version 1.20

%if %{_use_internal_dependency_generator}
%define __noautoreq '/bin/false'
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	A localization library for Perl
License:	LGPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/G/GU/GUIDO/%{upstream_name}-%{upstream_version}.tar.bz2

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog NEWS README THANKS TODO
%{perl_vendorlib}/Locale
%{perl_vendorarch}/auto/Locale
%{_mandir}/*/*

