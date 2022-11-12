Name:		texlive-hpsdiss
Version:	15878
Release:	1
Summary:	A dissertation class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hpsdiss
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hpsdiss.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hpsdiss.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hpsdiss.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class was developed to typeset a dissertation at ETH
Zurich. The requirements were to use A5 paper and 10pt type. A
sample of the output is shown in the PDF documentation link.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hpsdiss/hpsdiss.cls
%doc %{_texmfdistdir}/doc/latex/hpsdiss/hpsdiss.pdf
#- source
%doc %{_texmfdistdir}/source/latex/hpsdiss/hpsdiss.dtx
%doc %{_texmfdistdir}/source/latex/hpsdiss/hpsdiss.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
