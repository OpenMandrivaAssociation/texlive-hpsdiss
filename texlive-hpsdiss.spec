%global tl_name hpsdiss
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A dissertation class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hpsdiss
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hpsdiss.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hpsdiss.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hpsdiss.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class was developed to typeset a dissertation at ETH Zurich. The
requirements were to use A5 paper and 10pt type. A sample of the output
is shown in the PDF documentation link.

