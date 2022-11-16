Name:		texlive-nwafuthesis
Version:	63438
Release:	1
Summary:	A thesis template package for Northwest A&F University, China
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nwafuthesis
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nwafuthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nwafuthesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nwafuthesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This template supports doctoral and master dissertations and
undergraduate theses in Chinese. With the help of modern LaTeX3
technology, nwafuthesis aims to create a simple interface, a
normative format, as well as a hackable class for the users. At
present, nwafuthesis only supports XeTeX and LuaTeX engines.
nwafuthesis only allows UTF-8 encoding. nwafuthesis is based on
the fduthesis template.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/nwafuthesis
%{_texmfdistdir}/tex/latex/nwafuthesis
%doc %{_texmfdistdir}/doc/latex/nwafuthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
