%define	upstream_name	 libintl-perl
%define	upstream_version 1.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	A localization library for Perl
License:	LGPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/G/GU/GUIDO/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	db4-devel
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
BuildRequires:	perl-devel
#gw yes, this is required by the tests
BuildRequires:	locales-de
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
