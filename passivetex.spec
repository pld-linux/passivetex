Summary:	Macros to process XSL formatting objects
Name:		passivetex
Version:	1.4
Release:	1
License:	LaTeX Project Public License (http://www.latex-project.org/lppl.txt)
Group:		Applications/Publishing/TeX
Group(de):	Applikationen/Publizieren/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
##Source0:	ftp://ftp.icm.edu.pl/pub/CTAN/macros/%{name}.tar.gz
Source0:	ftp://ftp.tex.ac.uk/tex-archive/macros/%{name}.tar.gz
Source1:	ftp://ftp.tex.ac.uk/tex-archive/macros/xmltex.tar.gz
URL:		http://users.ox.ac.uk/~rahtz/passivetex/
Autoreqprov:	no
BuildArch:	noarch
Prereq:		tetex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	mydir	%{_datadir}/texmf/tex/latex/passivetex

%description
PassiveTeX is a library of TeX macros which can be used to process an
XML document which results from an XSL transformation to formatting
objects.


%prep
%setup -q -c %{name}-%{version} -a 1
mv -f %{name}/* .
rmdir %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{mydir}

install *.sty xmltex/contrib/passivetex/fotex* $RPM_BUILD_ROOT%{mydir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/texhash 1>&2

%postun
/usr/bin/texhash 1>&2

%files
%defattr(644,root,root,755)
%{mydir}
