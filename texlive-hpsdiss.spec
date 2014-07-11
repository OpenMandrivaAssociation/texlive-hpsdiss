# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/hpsdiss
# catalog-date 2007-01-07 11:47:19 +0100
# catalog-license gpl
# catalog-version 1.0
Name:		texlive-hpsdiss
Version:	1.0
Release:	8
Summary:	A dissertation class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hpsdiss
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hpsdiss.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hpsdiss.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hpsdiss.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752584
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718622
- texlive-hpsdiss
- texlive-hpsdiss
- texlive-hpsdiss
- texlive-hpsdiss

