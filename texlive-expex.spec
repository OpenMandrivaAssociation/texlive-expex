Name:		texlive-expex
Version:	44499
Release:	2
Summary:	Format linguistic examples and glosses, with reference capabilities
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/expex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expex.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
