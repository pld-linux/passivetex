Summary:	Macros to process XSL formatting objects
Summary(pl):	Makra do obróbki obiektów formatuj±cych XSL
Name:		passivetex
Version:	1.19
Release:	2
License:	LaTeX Project Public License (http://www.latex-project.org/lppl.txt)
Group:		Applications/Publishing/TeX
##Source0:	ftp://ftp.icm.edu.pl/pub/CTAN/macros/%{name}.tar.gz
Source0:	http://users.ox.ac.uk/~rahtz/%{name}/passivetex.zip
URL:		http://users.ox.ac.uk/~rahtz/passivetex/
Autoreqprov:	no
BuildArch:	noarch
Prereq:		tetex
Requires:	xmltex
Requires:	tetex-ams
Requires:	tetex-fonts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	mydir	%{_datadir}/texmf/tex/xmltex/passivetex

%description
PassiveTeX is a library of TeX macros which can be used to process an
XML document which results from an XSL transformation to formatting
objects.

%description -l pl
PassiveTeX jest bibliotek± makr TeXa, których mo¿na u¿ywaæ do obróbki
dokumentu XML, który pochodzi z transformacji XSL do obiektów
formatuj±cych.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{mydir}

install *.sty *.xmt **.tex $RPM_BUILD_ROOT%{mydir}


%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/texhash 1>&2

%postun
/usr/bin/texhash 1>&2

%files
%defattr(644,root,root,755)
%doc README.passivetex LICENSE
%{mydir}
