%define	module	libintl-perl

Summary:	A localization library for Perl
Name:		perl-%{module}
Version:	1.16
Release:	%mkrel 5
License:	LGPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/authors/id/G/GU/GUIDO/%{module}-%{version}.tar.bz2
BuildRequires:	db4-devel
BuildRequires:	gdbm-devel
BuildRequires:	perl-devel
BuildRequires:	gettext-devel
#gw yes, this is required by the tests
BuildRequires:	locales-de
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}

%makeinstall_std

# fix attribs
find %{buildroot}%{perl_vendorlib} -name "*.pm" | xargs chmod 755

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog NEWS README THANKS TODO
%{perl_vendorlib}/Locale
%{perl_vendorarch}/auto/Locale
%{_mandir}/*/*
