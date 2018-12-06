#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-CSS-DOM
Version  : 0.17
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/S/SP/SPROUT/CSS-DOM-0.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SP/SPROUT/CSS-DOM-0.17.tar.gz
Summary  : 'Document Object Model for Cascading Style Sheets'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0 GPL-2.0
Requires: perl-CSS-DOM-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Clone)

%description
CSS::DOM, version 0.17
This module implements a CSS-specific subset of the interfaces
described in the W3C DOM specification.

%package dev
Summary: dev components for the perl-CSS-DOM package.
Group: Development
Provides: perl-CSS-DOM-devel = %{version}-%{release}

%description dev
dev components for the perl-CSS-DOM package.


%package license
Summary: license components for the perl-CSS-DOM package.
Group: Default

%description license
license components for the perl-CSS-DOM package.


%prep
%setup -q -n CSS-DOM-0.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-CSS-DOM
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-CSS-DOM/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Array.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Constants.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Exception.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Interface.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/MediaList.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Parser.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/PropertyParser.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Rule.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Rule/Charset.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Rule/FontFace.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Rule/Import.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Rule/Media.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Rule/Page.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Rule/Style.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/RuleList.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Style.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/StyleSheetList.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Util.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Value.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Value/List.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Value/Primitive.pm
/usr/lib/perl5/vendor_perl/5.28.1CSS/DOM/Value/Primitive/colours.pl

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/CSS::DOM.3
/usr/share/man/man3/CSS::DOM::Array.3
/usr/share/man/man3/CSS::DOM::Constants.3
/usr/share/man/man3/CSS::DOM::Exception.3
/usr/share/man/man3/CSS::DOM::Interface.3
/usr/share/man/man3/CSS::DOM::MediaList.3
/usr/share/man/man3/CSS::DOM::Parser.3
/usr/share/man/man3/CSS::DOM::PropertyParser.3
/usr/share/man/man3/CSS::DOM::Rule.3
/usr/share/man/man3/CSS::DOM::Rule::Charset.3
/usr/share/man/man3/CSS::DOM::Rule::FontFace.3
/usr/share/man/man3/CSS::DOM::Rule::Import.3
/usr/share/man/man3/CSS::DOM::Rule::Media.3
/usr/share/man/man3/CSS::DOM::Rule::Page.3
/usr/share/man/man3/CSS::DOM::Rule::Style.3
/usr/share/man/man3/CSS::DOM::RuleList.3
/usr/share/man/man3/CSS::DOM::Style.3
/usr/share/man/man3/CSS::DOM::StyleSheetList.3
/usr/share/man/man3/CSS::DOM::Util.3
/usr/share/man/man3/CSS::DOM::Value.3
/usr/share/man/man3/CSS::DOM::Value::List.3
/usr/share/man/man3/CSS::DOM::Value::Primitive.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-CSS-DOM/LICENSE
