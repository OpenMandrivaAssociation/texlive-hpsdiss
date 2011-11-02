Name:		texlive-hpsdiss
Version:	1.0
Release:	1
Summary:	A dissertation class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hpsdiss
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hpsdiss.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hpsdiss.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hpsdiss.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The class was developed to typeset a dissertation at ETH
Zurich. The requirements were to use A5 paper and 10pt type. A
sample of the output is shown in the PDF documentation link.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
