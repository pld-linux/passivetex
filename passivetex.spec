
Summary:	Macros to process XSL formatting objects
Summary(pl):	Makra do obróbki obiektów formatuj±cych XSL
Name:		passivetex
Version:	1.25
Release:	4
License:	LaTeX Project Public License (http://www.latex-project.org/lppl.txt)
Group:		Applications/Publishing/TeX
Source0:	http://www.tei-c.org.uk/Software/passivetex/passivetex.zip
# Source0-md5:	03e05ab33d3abe1a316c8d9877c315d6
URL:		http://www.tei-c.org.uk/Software/passivetex/
BuildRequires:	unzip
Requires:	xmltex
Requires:	tetex-latex-ams
Requires:	tetex-fonts-jknappen
Requires:	tetex-fonts-stmaryrd
Requires:	tetex-latex-wasysym
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
AutoReqProv:	no
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	ptexmf	%{_datadir}/texmf/tex/xmltex/passivetex

%description
PassiveTeX is a library of TeX macros which can be used to process an
XML document which results from an XSL transformation to formatting
objects.

%description -l pl
PassiveTeX jest bibliotek± makr TeXa, których mo¿na u¿ywaæ do obróbki
dokumentu XML pochodz±cego z transformacji XSL-a do obiektów
formatuj±cych.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ptexmf}

install *.sty *.xmt $RPM_BUILD_ROOT%{ptexmf}
rm -f test/*.{aux,log}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/texhash 1>&2

%postun
/usr/bin/texhash 1>&2

%files
%defattr(644,root,root,755)
%doc README.passivetex LICENSE index.html test
%{ptexmf}
