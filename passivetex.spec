
Summary:	Macros to process XSL formatting objects
Summary(pl.UTF-8):	Makra do obróbki obiektów formatujących XSL
Name:		passivetex
Version:	1.25
Release:	5
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
Requires(post,postun):	%{_bindir}/texhash
AutoReqProv:	no
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ptexmf	%{_datadir}/texmf/tex/xmltex/passivetex
%define		texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2;

%description
PassiveTeX is a library of TeX macros which can be used to process an
XML document which results from an XSL transformation to formatting
objects.

%description -l pl.UTF-8
PassiveTeX jest biblioteką makr TeXa, których można używać do obróbki
dokumentu XML pochodzącego z transformacji XSL-a do obiektów
formatujących.

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
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc README.passivetex LICENSE index.html test
%{ptexmf}
