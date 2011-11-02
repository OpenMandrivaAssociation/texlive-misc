Name:		texlive-misc
Version:	20111102
Release:	1
Summary:	TeXLive misc package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/misc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
TeXLive misc package.

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
%{_texmfdistdir}/fonts/source/public/misc/black.mf
%{_texmfdistdir}/fonts/source/public/misc/blackaps.mf
%{_texmfdistdir}/fonts/source/public/misc/blackcx.mf
%{_texmfdistdir}/fonts/source/public/misc/blackimagen.mf
%{_texmfdistdir}/fonts/source/public/misc/blacklino.mf
%{_texmfdistdir}/fonts/source/public/misc/blacklj.mf
%{_texmfdistdir}/fonts/source/public/misc/cmman.mf
%{_texmfdistdir}/fonts/source/public/misc/gray.mf
%{_texmfdistdir}/fonts/source/public/misc/grayaps.mf
%{_texmfdistdir}/fonts/source/public/misc/graycx.mf
%{_texmfdistdir}/fonts/source/public/misc/grayf.mf
%{_texmfdistdir}/fonts/source/public/misc/grayimagen.mf
%{_texmfdistdir}/fonts/source/public/misc/grayimagen3.mf
%{_texmfdistdir}/fonts/source/public/misc/grayimagenlight.mf
%{_texmfdistdir}/fonts/source/public/misc/graylj.mf
%{_texmfdistdir}/fonts/source/public/misc/manfnt.mf
%{_texmfdistdir}/fonts/source/public/misc/mfman.mf
%{_texmfdistdir}/fonts/source/public/misc/oneone.mf
%{_texmfdistdir}/fonts/source/public/misc/random.mf
%{_texmfdistdir}/fonts/source/public/misc/slant.mf
%{_texmfdistdir}/fonts/source/public/misc/slantaps4.mf
%{_texmfdistdir}/fonts/source/public/misc/slantcx4.mf
%{_texmfdistdir}/fonts/source/public/misc/slantcx6.mf
%{_texmfdistdir}/fonts/source/public/misc/slantimagen4.mf
%{_texmfdistdir}/fonts/source/public/misc/slantimagen6.mf
%{_texmfdistdir}/fonts/source/public/misc/slantlino4.mf
%{_texmfdistdir}/fonts/source/public/misc/slantlj4.mf
%{_texmfdistdir}/fonts/source/public/misc/slantlj6.mf
%{_texmfdistdir}/fonts/tfm/public/misc/black.tfm
%{_texmfdistdir}/fonts/tfm/public/misc/blackcx.tfm
%{_texmfdistdir}/fonts/tfm/public/misc/cmman.tfm
%{_texmfdistdir}/fonts/tfm/public/misc/gray.tfm
%{_texmfdistdir}/fonts/tfm/public/misc/graycx.tfm
%{_texmfdistdir}/fonts/tfm/public/misc/grayimagen3.tfm
%{_texmfdistdir}/fonts/tfm/public/misc/manfnt.tfm
%{_texmfdistdir}/fonts/tfm/public/misc/oneone.tfm
%{_texmfdistdir}/fonts/tfm/public/misc/slantcx4.tfm
%{_texmfdistdir}/fonts/tfm/public/misc/slantcx6.tfm
%{_texmfdistdir}/fonts/tfm/public/misc/slantlj4.tfm
%{_texmfdistdir}/fonts/tfm/public/misc/slantlj6.tfm
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
