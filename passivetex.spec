Summary:	Macros to process XSL formatting objects
Name:		passivetex
Version:	1.5
Release:	1
License:	LaTeX Project Public License (http://www.latex-project.org/lppl.txt)
Group:		Applications/Publishing/TeX
Group(de):	Applikationen/Publizieren/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
##Source0:	ftp://ftp.icm.edu.pl/pub/CTAN/macros/%{name}.tar.gz
Source0:	http://users.ox.ac.uk/~rahtz/passivetex/passivetex.zip
URL:		http://users.ox.ac.uk/~rahtz/passivetex/
Autoreqprov:	no
BuildArch:	noarch
Prereq:		tetex
Requires:	xmltex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	mydir	%{_datadir}/texmf/tex/xmltex/passivetex

%description
PassiveTeX is a library of TeX macros which can be used to process an
XML document which results from an XSL transformation to formatting
objects.


%prep
%setup -q -c %{name}-%{version} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{mydir}

install *.sty *.xmt *.cfg $RPM_BUILD_ROOT%{mydir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/texhash 1>&2

%postun
/usr/bin/texhash 1>&2

%files
%defattr(644,root,root,755)
%{mydir}
