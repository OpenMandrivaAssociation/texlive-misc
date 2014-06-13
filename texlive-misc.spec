# revision 32910
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-misc
Version:	20140214
Release:	2
Summary:	TeXLive misc package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/misc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive misc package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/misc/blackcx.mf
%{_texmfdistdir}/fonts/source/public/misc/graycx.mf
%{_texmfdistdir}/fonts/source/public/misc/grayf.mf
%{_texmfdistdir}/fonts/source/public/misc/manfnt.mf
%{_texmfdistdir}/fonts/source/public/misc/slant.mf
%{_texmfdistdir}/fonts/source/public/misc/slantcx4.mf
%{_texmfdistdir}/fonts/source/public/misc/slantcx6.mf
%{_texmfdistdir}/fonts/source/public/misc/slantlj6.mf
%{_texmfdistdir}/omega/ocp/misc/ebcdic.ocp
%{_texmfdistdir}/omega/ocp/misc/id.ocp
%{_texmfdistdir}/omega/otp/misc/ebcdic.otp
%{_texmfdistdir}/omega/otp/misc/id.otp
%{_texmfdistdir}/tex/generic/misc/bibnames.sty
%{_texmfdistdir}/tex/generic/misc/null.tex
%{_texmfdistdir}/tex/generic/misc/texnames.sty
%{_texmfdistdir}/tex/plain/misc/idxmac.tex
%{_texmfdistdir}/tex/plain/misc/pdfcolor.tex
%{_texmfdistdir}/tex/plain/misc/tugboat.def
%{_texmfdistdir}/tex/plain/misc/xepsf.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts omega tex %{buildroot}%{_texmfdistdir}
