# revision 33163
# category Package
# catalog-ctan /macros/plain/contrib/expex
# catalog-date 2014-03-12 20:21:38 +0100
# catalog-license lppl
# catalog-version 5.0b
Name:		texlive-expex
Version:	5.0b
Release:	2
Summary:	Format linguistic examples and glosses, with reference capabilities
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/expex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros for typesetting linguistic examples
and glosses, with a refined mechanism for referencing examples
and parts of examples. The package can be used with LaTex using
the .sty wrapper or with PlainTex.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/expex/epltxchapno.sty
%{_texmfdistdir}/tex/generic/expex/epltxfn.sty
%{_texmfdistdir}/tex/generic/expex/eptexfn.tex
%{_texmfdistdir}/tex/generic/expex/expex-demo.tex
%{_texmfdistdir}/tex/generic/expex/expex.sty
%{_texmfdistdir}/tex/generic/expex/expex.tex
%doc %{_texmfdistdir}/doc/generic/expex/README
%doc %{_texmfdistdir}/doc/generic/expex/doc-source.zip
%doc %{_texmfdistdir}/doc/generic/expex/expex-doc.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
