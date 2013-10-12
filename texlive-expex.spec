# revision 31356
# category Package
# catalog-ctan /macros/plain/contrib/expex
# catalog-date 2013-08-05 23:52:23 +0200
# catalog-license lppl
# catalog-version 4.1e
Name:		texlive-expex
Version:	4.1e
Release:	1
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
and parts of examples. The package was written for use with
Plain TeX, but is usable with LaTeX with the wrapper .sty file.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/expex/epltxfn.sty
%{_texmfdistdir}/tex/generic/expex/eptexfn.tex
%{_texmfdistdir}/tex/generic/expex/expex-demo.tex
%{_texmfdistdir}/tex/generic/expex/expex.sty
%{_texmfdistdir}/tex/generic/expex/expex.tex
%doc %{_texmfdistdir}/doc/generic/expex/README
%doc %{_texmfdistdir}/doc/generic/expex/expex-doc.pdf
%doc %{_texmfdistdir}/doc/generic/expex/source/0-index.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/0-tags.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/0.idx
%doc %{_texmfdistdir}/doc/generic/expex/source/0.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/0.toc
%doc %{_texmfdistdir}/doc/generic/expex/source/000doc-cover.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/01_intro.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/02_Examples.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/03_XKV.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/04_Ex.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/05_MultiPart-Basics.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/06_MoreExamples.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/07_UserStyles.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/08_Judgments.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/09_Glosses-Basic.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/10_Glosses-Advanced.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/11_Refs.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/12_Tables.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/13_PSTricks.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/14_PageBreaks.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/README-manual.txt
%doc %{_texmfdistdir}/doc/generic/expex/source/X-code-beta.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/X-contents.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/X-lingdoc.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/X-local-doc.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/X-mkindex.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/X-mybasics.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/X-sections.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/X-timesfonts.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/example1.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/example2.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/example3.tex
%doc %{_texmfdistdir}/doc/generic/expex/source/example4.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
