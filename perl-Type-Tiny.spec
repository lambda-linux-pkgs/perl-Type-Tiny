%define _buildid .1

Name:           perl-Type-Tiny
Version:        1.000005
Release:        1%{?_buildid}%{?dist}
Summary:        Tiny, yet Moo(se)-compatible type constraint
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Type-Tiny/
Source0:        http://www.cpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-%{version}.tar.gz
BuildArch:      noarch

# --with reply_plugin
#	Default: --without
# Missing deps (perl(Reply::Plugin))
# Marked as unstable (cf. lib/Reply/Plugin/TypeTiny.pm)
%bcond_with reply_plugin

BuildRequires:  perl >= 0:5.006001
BuildRequires:  perl(B)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Exporter::Tiny) >= 0.026
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Tester) >= 0.109
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

# optional
# N/A in Fedora: BuildRequires:  perl(Class::InsideOut)
BuildRequires:  perl(Class::ISA)
BuildRequires:  perl(Devel::Hide)
BuildRequires:  perl(Devel::LexAlias) >= 0.05
BuildRequires:  perl(Devel::StackTrace)
# N/A in Fedora: BuildRequires:  perl(Function::Parameters)
BuildRequires:  perl(JSON::PP)
# N/A in Fedora: BuildRequires:  perl(Kavorka)
# N/A in Fedora: BuildRequires:  perl(match::simple)
BuildRequires:  perl(Moo)
# N/A in Fedora: BuildRequires:  perl(Moops)
BuildRequires:  perl(Object::Accessor)
%{?with_reply_plugin:BuildRequires:  perl(Reply::Plugin)}
# N/A in Fedora: BuildRequires:  perl(Return::Type)
BuildRequires:  perl(Role::Tiny)
# N/A in Fedora: BuildRequires:  perl(Sub::Exporter::Lexical)
# N/A in Fedora: BuildRequires:  perl(Switcheroo)
%{?with_reply_plugin:BuildRequires:  perl(Term::ANSIColor)}
BuildRequires:  perl(Type::Tie)
# N/A in Fedora: BuildRequires:  perl(Validation::Class)
BuildRequires:  perl(Type::Tiny::XS) >= 0.003

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

Type::Tiny is a tiny class for creating Moose-like type constraint objects
which are compatible with Moo, Moose and Mouse.

%package -n perl-Test-TypeTiny
Summary: Test::TypeTiny module

%description -n perl-Test-TypeTiny
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

Test::TypeTiny module.

%prep
%setup -q -n Type-Tiny-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes COPYRIGHT CREDITS LICENSE NEWS README
%{perl_vendorlib}/*
%{!?with_reply_plugin:%exclude %{perl_vendorlib}/Reply}
%{_mandir}/man3/*
%exclude %{perl_vendorlib}/Test
%exclude %{_mandir}/man3/Test::TypeTiny.3pm*

%files -n perl-Test-TypeTiny
%{perl_vendorlib}/Test
%{_mandir}/man3/Test::TypeTiny.3pm*

%changelog
* Fri Dec 26 2014 Rajiv M Ranganath <rajiv.ranganath@atihita.com> 1.000005-1
- Adapt for AL/LL
- Add package support URL
- Update spec file
- Import source package FC21/perl-Type-Tiny-1.000005-1.fc21

* Mon Oct 27 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000005-1
- Upstream update.

* Thu Sep 04 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000004-1
- Upstream update.

* Sun Aug 31 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000003-1
- Upstream update.

* Fri Aug 22 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000002-1
- Upstream update.
- Update deps.

* Mon Aug 18 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000000-1
- Upstream update.

* Thu Jul 24 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.046-1
- Upstream update.

* Mon Jun 23 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.044-1
- Upstream update.
- Spec file cosmetics.
- BR: perl(Test::Moose), perl(MooseX::Getopt).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.042-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 08 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.042-1
- Upstream update.
- Split out perl(Test::TypeTiny) to avoid deps on perl(Test::*).

* Fri Mar 21 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.040-1
- Initial Fedora package.
