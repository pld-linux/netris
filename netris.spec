Summary:	A free networked version of T*tris
Summary(pl):	Darmowa, sieciowa wersja T*trisa
Name:		netris
Version:	0.5
Release:	1
License:	GPL
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	ftp://ftp.netris.org/pub/netris/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://www.netris.org/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free networked version of T*tris.

%description -l pl
Darmowa, sieciowa wersja T*trisa.

%prep
%setup -q
%patch0 -p1

%build
./Configure \
	--copt "%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install netris	$RPM_BUILD_ROOT%{_bindir}
install sr	$RPM_BUILD_ROOT%{_bindir}

gzip -9nf README FAQ *_desc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
