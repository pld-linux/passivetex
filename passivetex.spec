Summary:	Macros to process XSL formatting objects
Name:		passivetex
Version:	1.4
Release:	1
## sprawd
License:	LaTeX Project Public License (http://www.latex-project.org/lppl.txt)
Group:		Applications/Publishing/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Source0:	ftp://ftp.icm.edu.pl/pub/CTAN/macros/%{name}.tar.gz
##Source0:	ftp://ftp.tex.ac.uk/tex-archive/macros/passivetex.zip
Autoreqprov:	no
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	mydir	%{_datadir}/texmf/tex/latex/passivetex

%description
PassiveTeX is a library of TeX macros which can be used to process an
XML document which results from an XSL transformation to formatting
objects.


%prep
%setup -q -c %{name}-%{version}
mv -f %{name}/* .
rmdir %{name}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{mydir}

install *.sty $RPM_BUILD_ROOT%{mydir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

%postun
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

%files
%defattr(644,root,root,755)
%{mydir}
